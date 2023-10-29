from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):  # класс родит.

    def __init__(self):  # конструктор
        super(Window, self).__init__()

        self.setWindowTitle("Расчет треугольника")  # наследуем из QMainWindow
        self.setGeometry(600, 450, 450, 600)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Введите три стороны треугольника")
        self.main_text.move(100, 50)  # двигаем сам обьект в пределах окна
        self.main_text.adjustSize()

        self.lineEdit1 = QtWidgets.QLineEdit(self)
        self.lineEdit1.setGeometry(QtCore.QRect(100, 70, 200, 26))
        self.lineEdit1.setObjectName("textEdit")

        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.lineEdit2.setGeometry(QtCore.QRect(100, 100, 200, 26))
        self.lineEdit2.setObjectName("textEdit")

        self.lineEdit3 = QtWidgets.QLineEdit(self)
        self.lineEdit3.setGeometry(QtCore.QRect(100, 130, 200, 26))
        self.lineEdit3.setObjectName("textEdit")

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.move(100, 160)
        self.btn1.setText("Выполнить проверку")
        self.btn1.setFixedWidth(200)
        self.btn1.clicked.connect(self.collect_sides)

    def add_label(self):
        self.new_text.setText("Вторая надпись")  # появляется при нажатии на кнопку
        self.new_text.move(100, 50)
        self.new_text.adjustSize()

    @QtCore.pyqtSlot()
    def collect_sides(self):
        a = int(self.lineEdit1.text())
        b = int(self.lineEdit2.text())
        c = int(self.lineEdit3.text())
        self.proverka(a, b, c)
        self.cleaner()

    def proverka(self, a, b, c):
        if (a + b > c) and (b + c > a) and (a + c > b):
            print("Треугольник существует")
        else:
            print("Треугольник не существует")

    def cleaner(self):
        self.lineEdit1.clear()
        self.lineEdit2.clear()
        self.lineEdit3.clear()

def application():
    app = QApplication(sys.argv)  # передаем настройки компьютера из пакета sys
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()