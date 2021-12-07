# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/nf_por_data.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(816, 480)
        MainWindow.setMinimumSize(QtCore.QSize(816, 480))
        MainWindow.setMaximumSize(QtCore.QSize(826, 490))
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("background-color: rgb(62, 132, 238);\n"
"background-color: rgb(216, 164, 194);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BtnConfirmar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnConfirmar.setGeometry(QtCore.QRect(440, 150, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.BtnConfirmar.setFont(font)
        self.BtnConfirmar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnConfirmar.setStyleSheet("QPushButton {     \n"
"    background-color:rgb(78, 154, 6);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    \n"
"}\n"
"QPushButton:hover {   \n"
"    background-color:rgb(85, 165, 10);\n"
"}")
        self.BtnConfirmar.setObjectName("BtnConfirmar")
        self.InputData = QtWidgets.QDateEdit(self.centralwidget)
        self.InputData.setGeometry(QtCore.QRect(160, 150, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.InputData.setFont(font)
        self.InputData.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"font: 21pt \"Ubuntu\";\n"
"color: black;\n"
"")
        self.InputData.setAlignment(QtCore.Qt.AlignCenter)
        self.InputData.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.InputData.setCalendarPopup(True)
        self.InputData.setTimeSpec(QtCore.Qt.LocalTime)
        self.InputData.setObjectName("InputData")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 50, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 751, 391))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/../IMAGENS/marca d\'agua.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.BtnConfirmar.raise_()
        self.InputData.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Selecionar notas por data de emissão"))
        self.BtnConfirmar.setText(_translate("MainWindow", "Confirmar"))
        self.label_4.setText(_translate("MainWindow", "Informe a data de emissão da nota para consulta"))
