# The app GUI was made by QtDesigner
# 21.05.2021

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QDialog, object):
    def __init__(self, MainWindow):
        super(Ui_MainWindow, self).__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StrokaVvoda = QtWidgets.QLabel(self.centralwidget)
        self.StrokaVvoda.setGeometry(QtCore.QRect(10, 10, 800, 150))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.StrokaVvoda.setFont(font)
        self.StrokaVvoda.setStyleSheet("font: 75 23pt \"Malgun Gothic\";\n"
"background-color: rgb(92, 122, 255);")
        self.StrokaVvoda.setObjectName("StrokaVvoda")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(10, 650, 160, 160))
        self.btn0.setStyleSheet("background-color: rgb(255, 159, 48);\n"
"font: 87 13pt \"Qanelas\";")
        self.btn0.setObjectName("btn0")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(10, 170, 160, 160))
        self.btn1.setStyleSheet("background-color: rgb(255, 159, 48);\n"
"font: 87 13pt \"Qanelas\";")
        self.btn1.setObjectName("btn1")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(170, 330, 160, 160))
        self.btn5.setStyleSheet("background-color: rgb(255, 159, 48);\n"
"font: 87 13pt \"Qanelas\";\n"
"")
        self.btn5.setObjectName("btn5")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(10, 330, 160, 160))
        self.btn4.setStyleSheet("background-color: rgb(255, 159, 48);\n"
"font: 87 13pt \"Qanelas\";")
        self.btn4.setObjectName("btn4")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(330, 170, 160, 160))
        self.btn3.setStyleSheet("background-color: rgb(255, 159, 48);\n"
"font: 87 13pt \"Qanelas\";")
        self.btn3.setObjectName("btn3")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(170, 170, 160, 160))
        self.btn2.setStyleSheet("background-color: rgb(255, 159, 48);\n"
"font: 87 13pt \"Qanelas\";")
        self.btn2.setObjectName("btn2")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(330, 330, 160, 160))
        self.btn6.setStyleSheet("background-color: rgb(255, 159, 48);\n"
"font: 87 13pt \"Qanelas\";\n"
"")
        self.btn6.setObjectName("btn6")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(10, 490, 160, 160))
        self.btn7.setStyleSheet("background-color: rgb(255, 159, 48);\n"
"font: 87 13pt \"Qanelas\";")
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(170, 490, 160, 160))
        self.btn8.setStyleSheet("background-color: rgb(255, 159, 48);\n"
"font: 87 13pt \"Qanelas\";")
        self.btn8.setObjectName("btn8")
        self.btnPlus = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlus.setGeometry(QtCore.QRect(500, 440, 155, 185))
        self.btnPlus.setStyleSheet("font: 87 11pt \"Qanelas\";\n"
"background-color: rgb(170, 170, 255);")
        self.btnPlus.setObjectName("btnPlus")
        self.btnRavno = QtWidgets.QPushButton(self.centralwidget)
        self.btnRavno.setGeometry(QtCore.QRect(170, 650, 320, 160))
        self.btnRavno.setStyleSheet("background-color: rgb(255, 66, 29);\n"
"font: 87 20pt \"Qanelas Heavy\";")
        self.btnRavno.setObjectName("btnRavno")
        self.btnMinus = QtWidgets.QPushButton(self.centralwidget)
        self.btnMinus.setGeometry(QtCore.QRect(655, 440, 155, 185))
        self.btnMinus.setStyleSheet("font: 87 11pt \"Qanelas\";\n"
"background-color: rgb(170, 170, 255);")
        self.btnMinus.setObjectName("btnMinus")
        self.btnUmnozhit = QtWidgets.QPushButton(self.centralwidget)
        self.btnUmnozhit.setGeometry(QtCore.QRect(500, 625, 155, 185))
        self.btnUmnozhit.setStyleSheet("font: 87 11pt \"Qanelas\";\n"
"background-color: rgb(170, 170, 255);")
        self.btnUmnozhit.setObjectName("btnUmnozhit")
        self.btnRazdelit = QtWidgets.QPushButton(self.centralwidget)
        self.btnRazdelit.setGeometry(QtCore.QRect(655, 625, 155, 185))
        self.btnRazdelit.setStyleSheet("font: 87 11pt \"Qanelas\";\n"
"background-color: rgb(170, 170, 255);")
        self.btnRazdelit.setObjectName("btnRazdelit")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(330, 490, 160, 160))
        self.btn9.setStyleSheet("background-color: rgb(255, 159, 48);\n"
"font: 87 13pt \"Qanelas\";\n"
"")
        self.btn9.setObjectName("btn9")
        self.btnSteret = QtWidgets.QPushButton(self.centralwidget)
        self.btnSteret.setGeometry(QtCore.QRect(500, 300, 310, 130))
        self.btnSteret.setStyleSheet("font: 87 20pt \"Qanelas\";\n"
"background-color: rgb(170, 170, 255);")
        self.btnSteret.setObjectName("btnSteret")
        self.CentrUp = QtWidgets.QWidget(self.centralwidget)
        self.CentrUp.setGeometry(QtCore.QRect(10, 160, 800, 10))
        self.CentrUp.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.CentrUp.setObjectName("CentrUp")
        self.CentrRight = QtWidgets.QWidget(self.centralwidget)
        self.CentrRight.setGeometry(QtCore.QRect(490, 170, 10, 640))
        self.CentrRight.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.CentrRight.setObjectName("CentrRight")
        self.Up = QtWidgets.QWidget(self.centralwidget)
        self.Up.setGeometry(QtCore.QRect(0, 0, 820, 10))
        self.Up.setStyleSheet("background-color: rgb(79, 79, 79);\n"
"")
        self.Up.setObjectName("Up")
        self.down = QtWidgets.QWidget(self.centralwidget)
        self.down.setGeometry(QtCore.QRect(0, 810, 820, 10))
        self.down.setStyleSheet("background-color: rgb(79, 79, 79);\n"
"")
        self.down.setObjectName("down")
        self.Left = QtWidgets.QFrame(self.centralwidget)
        self.Left.setGeometry(QtCore.QRect(0, 10, 10, 800))
        self.Left.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.Left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Left.setObjectName("Left")
        self.Right = QtWidgets.QFrame(self.centralwidget)
        self.Right.setGeometry(QtCore.QRect(810, 10, 10, 800))
        self.Right.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.Right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Right.setObjectName("Right")
        self.btnSteretVse = QtWidgets.QPushButton(self.centralwidget)
        self.btnSteretVse.setGeometry(QtCore.QRect(500, 170, 310, 130))
        self.btnSteretVse.setStyleSheet("font: 75 15pt \"Malgun Gothic\";\n"
"background-color: rgb(170, 170, 255);")
        self.btnSteretVse.setObjectName("btnSteret_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(500, 430, 310, 10))
        self.frame.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.StrokaVvoda.setText(_translate("MainWindow", "0"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btnPlus.setText(_translate("MainWindow", "+"))
        self.btnRavno.setText(_translate("MainWindow", "="))
        self.btnMinus.setText(_translate("MainWindow", "-"))
        self.btnUmnozhit.setText(_translate("MainWindow", "*"))
        self.btnRazdelit.setText(_translate("MainWindow", "/"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btnSteret.setText(_translate("MainWindow", "←"))
        self.btnSteretVse.setText(_translate("MainWindow", "Cut All"))

    def start(self):
        self.btn0.clicked.connect(lambda x: self.write_number(self.btn0.text()))
        self.btn1.clicked.connect(lambda x: self.write_number(self.btn1.text()))
        self.btn2.clicked.connect(lambda x: self.write_number(self.btn2.text()))
        self.btn3.clicked.connect(lambda x: self.write_number(self.btn3.text()))
        self.btn4.clicked.connect(lambda x: self.write_number(self.btn4.text()))
        self.btn5.clicked.connect(lambda x: self.write_number(self.btn5.text()))
        self.btn6.clicked.connect(lambda x: self.write_number(self.btn6.text()))
        self.btn7.clicked.connect(lambda x: self.write_number(self.btn7.text()))
        self.btn8.clicked.connect(lambda x: self.write_number(self.btn8.text()))
        self.btn9.clicked.connect(lambda x: self.write_number(self.btn9.text()))

        self.btnRavno.clicked.connect(lambda x: self.do_exercise(self.btnRavno.text()))
        self.btnSteretVse.clicked.connect(lambda x: self.do_exercise(self.btnSteretVse.text()))
        self.btnSteret.clicked.connect(lambda x: self.do_exercise(self.btnSteret.text()))
        self.btnPlus.clicked.connect(lambda x: self.do_exercise(self.btnPlus.text()))
        self.btnMinus.clicked.connect(lambda x: self.do_exercise(self.btnMinus.text()))
        self.btnUmnozhit.clicked.connect(lambda x: self.do_exercise(self.btnUmnozhit.text()))
        self.btnRazdelit.clicked.connect(lambda x: self.do_exercise(self.btnRazdelit.text()))

    def write_number(self, number):
        if number == '0' and (self.StrokaVvoda.text() == '0' or self.StrokaVvoda.text() == ''):
            return

        elif number == '0' and self.StrokaVvoda.text()[-1] == ' ':
            return

        elif self.StrokaVvoda.text() == '0' or self.StrokaVvoda.text()[0] == 'R':
            self.StrokaVvoda.setText(number)

        else:
            self.StrokaVvoda.setText(self.StrokaVvoda.text() + number)

    def do_exercise(self, exercise):
        if self.StrokaVvoda.text() == '':
            return

        elif (self.StrokaVvoda.text() == '0' or \
             self.StrokaVvoda.text()[0] == 'R' or\
             self.StrokaVvoda.text()[-1] == ' ') and \
             exercise != 'Cut All':
            return

        elif exercise == '=' and ' ' not in self.StrokaVvoda.text():
            return

        elif exercise == '=':
            result = eval(self.StrokaVvoda.text())
            self.StrokaVvoda.setText(f'Result: {result}')

        elif exercise == '←':
            if len(self.StrokaVvoda.text()) == 1:
                self.StrokaVvoda.setText('0')
            elif self.StrokaVvoda.text()[-1] == ' ':
                self.StrokaVvoda.setText(self.StrokaVvoda.text()[:-3])
            else:
                self.StrokaVvoda.setText(self.StrokaVvoda.text()[:-1])

        elif exercise == 'Cut All':
            self.StrokaVvoda.setText('0')

        else:
            self.StrokaVvoda.setText(self.StrokaVvoda.text() + f' {exercise} ')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(820, 820)
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
