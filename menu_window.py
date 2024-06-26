from PySide6.QtWidgets import (
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("menu_win")
        self.setWindowTitle("Memory Card")
        self.resize(400, 300)

        self.lb_question = QLabel("Введіть запитання:")
        self.lb_right_ans = QLabel("Введіть вірну відповідь:")
        self.lb_wrong_ans1 = QLabel("Введіть першу хибну відповідь:")
        self.lb_wrong_ans2 = QLabel("Введіть другу хибну відповідь:")
        self.lb_wrong_ans3 = QLabel("Введіть третю хибну відповідь:")

        self.le_question = QLineEdit()
        self.le_right_ans = QLineEdit()
        self.le_wrong_ans1 = QLineEdit()
        self.le_wrong_ans2 = QLineEdit()
        self.le_wrong_ans3 = QLineEdit()

        self.lb_header_stat = QLabel("Статистика")
        self.lb_header_stat.setStyleSheet("font-size: 19px; font-weight: bold;")
        self.lb_statistic = QLabel()

        self.btn_add_question = QPushButton("Додати запитання")
        self.btn_clear = QPushButton("Очистити")
        self.btn_back = QPushButton("Назад")

        self.fl_add_question = QFormLayout()
        self.fl_add_question.addRow(self.lb_question, self.le_question)
        self.fl_add_question.addRow(self.lb_right_ans, self.le_right_ans)
        self.fl_add_question.addRow(self.lb_wrong_ans1, self.le_wrong_ans1)
        self.fl_add_question.addRow(self.lb_wrong_ans2, self.le_wrong_ans2)
        self.fl_add_question.addRow(self.lb_wrong_ans3, self.le_wrong_ans3)

        self.hl_form_controls = QHBoxLayout()
        self.hl_form_controls.addWidget(self.btn_add_question)
        self.hl_form_controls.addWidget(self.btn_clear)

        self.vl_main = QVBoxLayout()
        self.vl_main.addLayout(self.fl_add_question)
        self.vl_main.addLayout(self.hl_form_controls)
        self.vl_main.addWidget(self.lb_header_stat)
        self.vl_main.addWidget(self.lb_statistic)
        self.vl_main.addWidget(self.btn_back)

        self.setLayout(self.vl_main)
