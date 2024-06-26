from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QButtonGroup,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

AlignCenter = Qt.AlignmentFlag.AlignCenter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("main_win")
        self.setWindowTitle("Memory Card")
        self.resize(600, 500)
        self.move(300, 300)

        self.lb_question = QLabel("Питання")
        self.lb_rest = QLabel("хвилин")
        self.lb_result = QLabel("Правильно")
        self.lb_right_answer = QLabel("Правильна відповідь")

        self.spb_rest = QSpinBox()

        self.btn_menu = QPushButton("Меню")
        self.btn_rest = QPushButton("Відпочити")
        self.btn_next = QPushButton("Відповісти")

        self.gb_answers = QGroupBox("Варіанти відповідей")
        self.gb_result = QGroupBox("Результат тесту")

        self.rb_ans1 = QRadioButton("1")
        self.rb_ans2 = QRadioButton("2")
        self.rb_ans3 = QRadioButton("3")
        self.rb_ans4 = QRadioButton("4")

        self.RadioGroup = QButtonGroup()
        self.RadioGroup.addButton(self.rb_ans1)
        self.RadioGroup.addButton(self.rb_ans2)
        self.RadioGroup.addButton(self.rb_ans3)
        self.RadioGroup.addButton(self.rb_ans4)

        self.hl_panel = QHBoxLayout()
        self.hl_panel.addWidget(self.btn_menu)
        self.hl_panel.addStretch(1)
        self.hl_panel.addWidget(self.btn_rest)
        self.hl_panel.addWidget(self.spb_rest)
        self.hl_panel.addWidget(self.lb_rest)

        self.vl_rb_col1 = QVBoxLayout()
        self.vl_rb_col1.addWidget(self.rb_ans1)
        self.vl_rb_col1.addWidget(self.rb_ans2)

        self.vl_rb_col2 = QVBoxLayout()
        self.vl_rb_col2.addWidget(self.rb_ans3)
        self.vl_rb_col2.addWidget(self.rb_ans4)

        self.hl_answers = QHBoxLayout()
        self.hl_answers.addLayout(self.vl_rb_col1)
        self.hl_answers.addLayout(self.vl_rb_col2)

        self.gb_answers.setLayout(self.hl_answers)

        self.vl_result = QVBoxLayout()
        self.vl_result.addWidget(self.lb_result)
        self.vl_result.addWidget(self.lb_right_answer, stretch=1, alignment=AlignCenter)

        self.gb_result.setLayout(self.vl_result)

        self.vl_main = QVBoxLayout()
        self.vl_main.addLayout(self.hl_panel, stretch=1)
        self.vl_main.addWidget(self.lb_question, stretch=2, alignment=AlignCenter)
        self.vl_main.addWidget(self.gb_answers, stretch=8)
        self.vl_main.addWidget(self.gb_result, stretch=8)
        self.vl_main.addWidget(self.btn_next, stretch=3, alignment=AlignCenter)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.vl_main)

        self.setCentralWidget(self.central_widget)

        self.gb_result.hide()
