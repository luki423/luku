import csv
import os
import sys
from random import choice, shuffle
from time import sleep

from PySide6.QtWidgets import QApplication

from main_window import MainWindow
from menu_window import MenuWindow


class Question:
    def __init__(
        self, question: str, right_ans: str, wrong_ans1: str, wrong_ans2: str, wrong_ans3: str
    ):
        self.question = question
        self.right_ans = right_ans
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3

        self.attempts = 0
        self.answered_right = 0

    def got_right(self):
        self.attempts += 1
        self.answered_right += 1

    def got_wrong(self):
        self.attempts += 1


if not os.path.isfile("questions.csv"):
    questions: list[Question] = [Question("Питання", "1", "2", "3", "4")]
else:
    with open("questions.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        questions: list[Question] = [Question(*row) for row in reader if row]


app = QApplication(sys.argv)

window = MainWindow()
menu_win = MenuWindow()


radio_buttons = window.RadioGroup.buttons()


def new_question():
    global cur_q

    cur_q = choice(questions)
    window.lb_question.setText(cur_q.question)
    window.lb_right_answer.setText(cur_q.right_ans)

    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.wrong_ans1)
    radio_buttons[1].setText(cur_q.wrong_ans2)
    radio_buttons[2].setText(cur_q.wrong_ans3)
    radio_buttons[3].setText(cur_q.right_ans)


new_question()


def check():
    window.RadioGroup.setExclusive(False)
    for radio_button in radio_buttons:
        if not radio_button.isChecked():
            continue
        radio_button.setChecked(False)
        if radio_button.text() == cur_q.right_ans:
            cur_q.got_right()
            window.lb_result.setText("Вірно!")
            break
    else:
        cur_q.got_wrong()
        window.lb_result.setText("Не вірно!")
    window.RadioGroup.setExclusive(True)


def click_on():
    if window.btn_next.text() == "Відповісти":
        check()
        window.gb_answers.hide()
        window.gb_result.show()
        window.btn_next.setText("Наступне питання")
    else:
        new_question()
        window.gb_result.hide()
        window.gb_answers.show()
        window.btn_next.setText("Відповісти")


def menu_generation():
    window.hide()
    c = cur_q.answered_right / cur_q.attempts if cur_q.attempts > 0 else 0
    menu_win.lb_statistic.setText(
        f"Разів відповіли: {cur_q.attempts}\n"
        f"Вірних відповідей: {cur_q.answered_right}\n"
        f"Успішність: {c:.2%}"  # f"{round(c * 100, 2)}%"
    )
    menu_win.show()


def rest():
    window.hide()
    sleep(window.spb_rest.value() * 60)
    window.show()


def back():
    menu_win.hide()
    window.show()


def clear():
    menu_win.le_question.clear()
    menu_win.le_right_ans.clear()
    menu_win.le_wrong_ans1.clear()
    menu_win.le_wrong_ans2.clear()
    menu_win.le_wrong_ans3.clear()


def add_question():
    row = [
        menu_win.le_question.text(),
        menu_win.le_right_ans.text(),
        menu_win.le_wrong_ans1.text(),
        menu_win.le_wrong_ans2.text(),
        menu_win.le_wrong_ans3.text(),
    ]
    questions.append(Question(*row))
    with open("questions.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(row)
    clear()


window.btn_menu.clicked.connect(menu_generation)
window.btn_rest.clicked.connect(rest)
window.btn_next.clicked.connect(click_on)

menu_win.btn_clear.clicked.connect(clear)
menu_win.btn_add_question.clicked.connect(add_question)
menu_win.btn_back.clicked.connect(back)

window.show()

with open("styles.qss", "r", encoding="utf-8") as styles:
    app.setStyleSheet(styles.read())

app.exec()
