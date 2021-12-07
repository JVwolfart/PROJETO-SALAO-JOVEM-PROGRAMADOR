# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jrwolfart/projetos python jv/PROJETO-SAL-O-JOVEM-PROGRAMADOR/telas_duda/estatisticas_por_intervalo_de_data.ui'
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
        MainWindow.resize(928, 466)
        MainWindow.setMinimumSize(QtCore.QSize(928, 466))
        MainWindow.setMaximumSize(QtCore.QSize(938, 476))
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("background-color: rgb(216, 164, 194);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BtnConfirmar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnConfirmar.setGeometry(QtCore.QRect(280, 360, 171, 41))
        self.BtnConfirmar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnConfirmar.setStyleSheet("QPushButton {     \n"
"    background-color: rgb(0, 170, 0);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {   \n"
"    background-color: rgb(0, 190, 0);\n"
"}\n"
"QPushButton:pressed {   \n"
"    background-color: rgb(0, 200, 0);\n"
"}")
        self.BtnConfirmar.setObjectName("BtnConfirmar")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 751, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.DataInicial = QtWidgets.QDateEdit(self.centralwidget)
        self.DataInicial.setGeometry(QtCore.QRect(240, 170, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DataInicial.setFont(font)
        self.DataInicial.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"font: 21pt \"Ubuntu\";\n"
"color: black;\n"
"")
        self.DataInicial.setAlignment(QtCore.Qt.AlignCenter)
        self.DataInicial.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.DataInicial.setCalendarPopup(True)
        self.DataInicial.setTimeSpec(QtCore.Qt.LocalTime)
        self.DataInicial.setObjectName("DataInicial")
        self.DataFinal = QtWidgets.QDateEdit(self.centralwidget)
        self.DataFinal.setGeometry(QtCore.QRect(240, 270, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DataFinal.setFont(font)
        self.DataFinal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"font: 21pt \"Ubuntu\";\n"
"color: black;\n"
"")
        self.DataFinal.setAlignment(QtCore.Qt.AlignCenter)
        self.DataFinal.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.DataFinal.setCalendarPopup(True)
        self.DataFinal.setTimeSpec(QtCore.Qt.LocalTime)
        self.DataFinal.setObjectName("DataFinal")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 140, 121, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 240, 121, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 140, 391, 191))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("/home/jrwolfart/projetos python jv/PROJETO-SAL-O-JOVEM-PROGRAMADOR/telas_duda/../IMAGENS/PicsArt_10-18-10.18.32.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Selecionar intervalo de datas para estatísticas"))
        self.BtnConfirmar.setText(_translate("MainWindow", "Confirmar"))
        self.label_5.setText(_translate("MainWindow", "Informe o intervalo de datas para consultar os dados estatísticos"))
        self.label.setText(_translate("MainWindow", "Data inicial"))
        self.label_2.setText(_translate("MainWindow", "Data final"))
