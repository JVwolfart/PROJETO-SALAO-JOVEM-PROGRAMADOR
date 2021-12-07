# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jrwolfart/projetos python jv/PROJETO-SAL-O-JOVEM-PROGRAMADOR/telas_duda/tela_login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        MainWindow.setMaximumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 231, 249);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.BtnEntrar = QtWidgets.QPushButton(self.frame)
        self.BtnEntrar.setGeometry(QtCore.QRect(490, 280, 111, 41))
        self.BtnEntrar.setStyleSheet("QPushButton {     \n"
"    background-color: rgb(0, 170, 0);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {   \n"
"    background-color: rgb(0, 190, 0);\n"
"}\n"
"QPushButton:pressed {   \n"
"    background-color: rgb(0, 200, 0);\n"
"}")
        self.BtnEntrar.setObjectName("BtnEntrar")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 0, 541, 221))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/jrwolfart/projetos python jv/PROJETO-SAL-O-JOVEM-PROGRAMADOR/telas_duda/../IMAGENS/PicsArt_10-18-10.18.32.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.InputUsuario = QtWidgets.QLineEdit(self.frame)
        self.InputUsuario.setGeometry(QtCore.QRect(200, 240, 261, 41))
        self.InputUsuario.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    border-color: 2px solid rgb(0,0,0);\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    border: 3px solid rgb(215, 139, 185);\n"
"}\n"
"")
        self.InputUsuario.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.InputUsuario.setObjectName("InputUsuario")
        self.InputSenha = QtWidgets.QLineEdit(self.frame)
        self.InputSenha.setGeometry(QtCore.QRect(200, 320, 261, 41))
        self.InputSenha.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    border-color: 2px solid rgb(0,0,0);\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    border: 3px solid rgb(215, 139, 185);\n"
"}")
        self.InputSenha.setInputMask("")
        self.InputSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.InputSenha.setObjectName("InputSenha")
        self.IconeUsuario = QtWidgets.QLabel(self.frame)
        self.IconeUsuario.setGeometry(QtCore.QRect(130, 230, 61, 51))
        self.IconeUsuario.setText("")
        self.IconeUsuario.setPixmap(QtGui.QPixmap("/home/jrwolfart/projetos python jv/PROJETO-SAL-O-JOVEM-PROGRAMADOR/telas_duda/../IMAGENS/User_icon_BLACK-01.png"))
        self.IconeUsuario.setScaledContents(True)
        self.IconeUsuario.setObjectName("IconeUsuario")
        self.IconeSenha = QtWidgets.QLabel(self.frame)
        self.IconeSenha.setGeometry(QtCore.QRect(130, 310, 51, 51))
        self.IconeSenha.setText("")
        self.IconeSenha.setPixmap(QtGui.QPixmap("/home/jrwolfart/projetos python jv/PROJETO-SAL-O-JOVEM-PROGRAMADOR/telas_duda/../IMAGENS/pngwing.com.png"))
        self.IconeSenha.setScaledContents(True)
        self.IconeSenha.setObjectName("IconeSenha")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela de Login"))
        self.BtnEntrar.setText(_translate("MainWindow", "Login"))
        self.InputUsuario.setPlaceholderText(_translate("MainWindow", "Usuário:"))
        self.InputSenha.setPlaceholderText(_translate("MainWindow", "Senha:"))
