# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jrwolfart/projetos python jv/PROJETO-SAL-O-JOVEM-PROGRAMADOR/telas_duda/manut_profissional.ui'
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
        MainWindow.resize(937, 504)
        MainWindow.setMinimumSize(QtCore.QSize(937, 504))
        MainWindow.setMaximumSize(QtCore.QSize(947, 514))
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("background-color: rgb(216, 164, 194);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BtnDesligar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnDesligar.setGeometry(QtCore.QRect(710, 430, 181, 41))
        self.BtnDesligar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnDesligar.setStyleSheet("QPushButton {     \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(239, 41, 41);\n"
"    border-radius: 10px;\n"
"    \n"
"}\n"
"QPushButton:hover {   \n"
"    background-color: rgb(249, 51, 51);\n"
"}\n"
"")
        self.BtnDesligar.setObjectName("BtnDesligar")
        self.BtnAlterar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnAlterar.setGeometry(QtCore.QRect(20, 430, 311, 41))
        self.BtnAlterar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnAlterar.setStyleSheet("QPushButton {     \n"
"    background-color:rgb(78, 154, 6);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    \n"
"}\n"
"QPushButton:hover {   \n"
"    background-color:rgb(85, 165, 10);\n"
"}\n"
"")
        self.BtnAlterar.setObjectName("BtnAlterar")
        self.BtnSair = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSair.setGeometry(QtCore.QRect(360, 430, 131, 41))
        self.BtnSair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnSair.setStyleSheet("QPushButton {     \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(245, 121, 0);\n"
"    border-radius: 10px;\n"
"    \n"
"}\n"
"QPushButton:hover {   \n"
"    background-color: rgb(250, 131, 0)\n"
"}\n"
"")
        self.BtnSair.setObjectName("BtnSair")
        self.InputId = QtWidgets.QSpinBox(self.centralwidget)
        self.InputId.setEnabled(False)
        self.InputId.setGeometry(QtCore.QRect(20, 140, 181, 41))
        self.InputId.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.InputId.setReadOnly(True)
        self.InputId.setObjectName("InputId")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 110, 171, 22))
        self.label.setObjectName("label")
        self.BtnReativar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnReativar.setGeometry(QtCore.QRect(520, 430, 161, 41))
        self.BtnReativar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnReativar.setStyleSheet("QPushButton {     \n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(237, 212, 0);\n"
"    \n"
"}\n"
"QPushButton:hover {   \n"
"    background-color: rgb(247, 222, 0);\n"
"}\n"
"")
        self.BtnReativar.setObjectName("BtnReativar")
        self.Ifuncao = QtWidgets.QLineEdit(self.centralwidget)
        self.Ifuncao.setEnabled(True)
        self.Ifuncao.setGeometry(QtCore.QRect(400, 340, 491, 41))
        self.Ifuncao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.Ifuncao.setReadOnly(False)
        self.Ifuncao.setObjectName("Ifuncao")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 300, 161, 22))
        self.label_2.setObjectName("label_2")
        self.Inome = QtWidgets.QLineEdit(self.centralwidget)
        self.Inome.setEnabled(True)
        self.Inome.setGeometry(QtCore.QRect(20, 220, 871, 41))
        self.Inome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.Inome.setReadOnly(False)
        self.Inome.setObjectName("Inome")
        self.Imatricula = QtWidgets.QLineEdit(self.centralwidget)
        self.Imatricula.setEnabled(False)
        self.Imatricula.setGeometry(QtCore.QRect(20, 340, 291, 41))
        self.Imatricula.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.Imatricula.setText("")
        self.Imatricula.setFrame(True)
        self.Imatricula.setCursorPosition(0)
        self.Imatricula.setDragEnabled(False)
        self.Imatricula.setReadOnly(False)
        self.Imatricula.setPlaceholderText("")
        self.Imatricula.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Imatricula.setClearButtonEnabled(True)
        self.Imatricula.setObjectName("Imatricula")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 300, 201, 22))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 30, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(580, 20, 361, 161))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("/home/jrwolfart/projetos python jv/PROJETO-SAL-O-JOVEM-PROGRAMADOR/telas_duda/../IMAGENS/PicsArt_10-18-10.18.32.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setIndent(-1)
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.BtnDesligar.raise_()
        self.BtnAlterar.raise_()
        self.BtnSair.raise_()
        self.InputId.raise_()
        self.label.raise_()
        self.BtnReativar.raise_()
        self.Ifuncao.raise_()
        self.label_2.raise_()
        self.Inome.raise_()
        self.Imatricula.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manutenção de Profissionais"))
        self.BtnDesligar.setText(_translate("MainWindow", "Desligar Profissioal"))
        self.BtnAlterar.setText(_translate("MainWindow", "Alterar Dados do Profissional"))
        self.BtnSair.setText(_translate("MainWindow", "Sair"))
        self.label.setText(_translate("MainWindow", "Id do Profissional"))
        self.BtnReativar.setText(_translate("MainWindow", "Reativar Profissional"))
        self.Ifuncao.setPlaceholderText(_translate("MainWindow", "Função do Profissional/funcionário"))
        self.label_2.setText(_translate("MainWindow", "Matricula"))
        self.Inome.setPlaceholderText(_translate("MainWindow", "Nome do Profissional/funcionário"))
        self.Imatricula.setInputMask(_translate("MainWindow", "0000000000"))
        self.label_3.setText(_translate("MainWindow", "Função/especialidade :"))
        self.label_4.setText(_translate("MainWindow", "Manutenção de funcionário:"))
