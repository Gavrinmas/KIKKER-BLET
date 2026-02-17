#создай приложение для запоминания информации
#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout,QGroupBox,QButtonGroup
from random import *
#создание элементов интерфейса
app = QApplication([])
# Создаем окно приложения
main_win = QWidget()
main_win.resize(500,250)
main_win.setWindowTitle('Memory card')

#----------------------------создание класса------------------------------
class Question():
    def __init__(self, question_parametr, right_answer, wrong1, wrong2, wrong3):
        self.question_parametr = question_parametr
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
_list_ = []
_list_.append(Question('Сколько планет в Солнечной системе?', '8', '9', '10', '7'))
_list_.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
_list_.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
_list_.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
#создание QGroupBox
group_box = QGroupBox('Варианты ответов')
radio1 = QRadioButton('Dream')
radio2 = QRadioButton('Daquavis')
radio3 = QRadioButton('Marlow')
radio4 = QRadioButton('ClodePearce')

#cоздание вопроса
qwestion = QLabel('Вопрос')

#создание группы для кнопки
button_group = QButtonGroup()
button_group.addButton(radio1)
button_group.addButton(radio2)
button_group.addButton(radio3)
button_group.addButton(radio4)

#cоздание кнопки
btn_ok = QPushButton('Ответить')

line_v1 = QVBoxLayout()#вертикальная groupbox
line_v2 = QVBoxLayout()#вертикальная groupbox

line_h1 = QHBoxLayout()#горизонатльная groupbox

#добавление radio к вертикальным линиям groupbox
line_v1.addWidget(radio1)
line_v1.addWidget(radio2)
line_v2.addWidget(radio3)
line_v2.addWidget(radio4)

#добавление вертикальных к горизонтальеым линиям 
line_h1.addLayout(line_v1)
line_h1.addLayout(line_v2)


group_box.setLayout(line_h1)



#----------второе задание 1 дня-----------------
#cоздаём groupbox (второй с результатом)
result_box = QGroupBox('Результат теста')
result_label = QLabel('Правильно/Неправильно')
correct_answer = QLabel('Правильный ответ')

#создаём вертикалльную линии для groupbox2
layout_res = QVBoxLayout()
layout_res.addWidget(result_label, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(correct_answer, alignment=Qt.AlignHCenter, stretch=2)
result_box.setLayout(layout_res)
#------------------------------------------------

line_question = QHBoxLayout() #линия для вопроса
line_group = QHBoxLayout()#линия для вариантов ответа
line_button = QHBoxLayout()#линия для кнопки

line_question.addWidget(qwestion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line_group.addWidget(group_box)
line_group.addWidget(result_box)#добавиил второй #groupbox к линии
result_box.hide()#скрываем первый #groupbox

line_button.addStretch(1)
line_button.addWidget(btn_ok, stretch=2)
line_button.addStretch(1)


#создание основной вертикальной линии для размещения
line_card = QVBoxLayout()
line_card.addLayout(line_question, stretch=1)
line_card.addLayout(line_group, stretch=8)
line_card.addStretch(1)
line_card.addLayout(line_button, stretch=1)
line_card.addStretch(1)
line_card.setSpacing(10)

main_win.setLayout(line_card)

def show_result():
    group_box.hide()
    result_box.show()
    btn_ok.setText('Следующий вопрос')
def show_question():
    result_box.hide()
    group_box.show()
    btn_ok.setText('Ответить')
    button_group.setExclusive(False)
    radio1.setChecked(False)
    radio2.setChecked(False)
    radio3.setChecked(False)
    radio4.setChecked(False)
    button_group.setExclusive(True)



#----------создаем список-----------------
answer = [radio1, radio2, radio3, radio4]

#-------------функция ask--------------

def ask(q):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    qwestion.setText(q.question_parametr)
    correct_answer.setText(q.right_answer)
    show_question()
#-------------------функция show_correct----------------

def show_correct(ras):
    result_label.setText(ras)
    show_result()

#-------------------функция check_answer----------------

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно)')
        main_win.true_score += 1
        print('-Статистика\n -Всего вопросов', main_win.total_score, '\n, -Правильных ответов', main_win.true_score)
        print('Рейтинг:', (main_win.true_score / main_win.total_score) * 100)
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неправильно(')
            print('Рейтинг:', (main_win.true_score / main_win.total_score) * 100)
            


def next_question(): 
    main_win.total_score += 1
    print('-Статистика\n -Всего вопросов', main_win.total_score, '\n, -Правильных ответов', main_win.true_score)
    ezzz = randint(0, len(_list_) -1)
    q = _list_[ezzz]
    ask(q)
def click_ok():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()

main_win.total_score = 0
main_win.true_score = 0

main_win.count = -1
btn_ok.clicked.connect(click_ok)
next_question()


main_win.show()
app.exec_()
