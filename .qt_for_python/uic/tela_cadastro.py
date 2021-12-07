# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/tela_cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(665, 796)
        MainWindow.setMinimumSize(QtCore.QSize(665, 796))
        MainWindow.setStyleSheet("background-color: rgb(254, 230, 248);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InputUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.InputUsuario.setGeometry(QtCore.QRect(230, 370, 221, 41))
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
        self.InputUsuario.setObjectName("InputUsuario")
        self.InputSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.InputSenha.setGeometry(QtCore.QRect(230, 450, 221, 41))
        self.InputSenha.setStyleSheet("QLineEdit{\n"
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
        self.InputSenha.setInputMask("")
        self.InputSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.InputSenha.setObjectName("InputSenha")
        self.BtnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnCadastrar.setGeometry(QtCore.QRect(190, 640, 141, 41))
        self.BtnCadastrar.setStyleSheet("QPushButton {     \n"
"    background-color: rgb(244, 163, 0);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {   \n"
"    background-color: rgb(250, 170, 0);\n"
"}\n"
"QPushButton:pressed {   \n"
"    background-color: rgb(255, 175, 0);\n"
"}")
        self.BtnCadastrar.setObjectName("BtnCadastrar")
        self.BtnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.BtnLogin.setGeometry(QtCore.QRect(350, 640, 131, 41))
        self.BtnLogin.setStyleSheet("QPushButton {     \n"
"    background-color: rgb(0, 170, 0);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {   \n"
"    background-color: rgb(0, 190, 0);\n"
"}\n"
"QPushButton:pressed {   \n"
"    background-color: rgb(0, 200, 0);\n"
"}")
        self.BtnLogin.setObjectName("BtnLogin")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 240, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.InputConfirmar = QtWidgets.QLineEdit(self.centralwidget)
        self.InputConfirmar.setGeometry(QtCore.QRect(230, 520, 221, 41))
        self.InputConfirmar.setStyleSheet("QLineEdit{\n"
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
        self.InputConfirmar.setInputMask("")
        self.InputConfirmar.setEchoMode(QtWidgets.QLineEdit.Password)
        self.InputConfirmar.setObjectName("InputConfirmar")
        self.BtnPermissao = QtWidgets.QPushButton(self.centralwidget)
        self.BtnPermissao.setGeometry(QtCore.QRect(170, 700, 321, 41))
        self.BtnPermissao.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnPermissao.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(245, 121, 0);\n"
"border-radius: 10px;")
        self.BtnPermissao.setObjectName("BtnPermissao")
        self.IconeSenha_2 = QtWidgets.QLabel(self.centralwidget)
        self.IconeSenha_2.setGeometry(QtCore.QRect(160, 510, 51, 51))
        self.IconeSenha_2.setText("")
        self.IconeSenha_2.setPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/../IMAGENS/pngwing.com.png"))
        self.IconeSenha_2.setScaledContents(True)
        self.IconeSenha_2.setObjectName("IconeSenha_2")
        self.IconeSenha_3 = QtWidgets.QLabel(self.centralwidget)
        self.IconeSenha_3.setGeometry(QtCore.QRect(160, 440, 51, 51))
        self.IconeSenha_3.setText("")
        self.IconeSenha_3.setPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/../IMAGENS/pngwing.com.png"))
        self.IconeSenha_3.setScaledContents(True)
        self.IconeSenha_3.setObjectName("IconeSenha_3")
        self.IconeUsuario_2 = QtWidgets.QLabel(self.centralwidget)
        self.IconeUsuario_2.setGeometry(QtCore.QRect(160, 360, 61, 51))
        self.IconeUsuario_2.setText("")
        self.IconeUsuario_2.setPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/../IMAGENS/User_icon_BLACK-01.png"))
        self.IconeUsuario_2.setScaledContents(True)
        self.IconeUsuario_2.setObjectName("IconeUsuario_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 20, 531, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/../IMAGENS/PicsArt_10-18-10.18.32.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.InputUsuario, self.InputSenha)
        MainWindow.setTabOrder(self.InputSenha, self.InputConfirmar)
        MainWindow.setTabOrder(self.InputConfirmar, self.BtnCadastrar)
        MainWindow.setTabOrder(self.BtnCadastrar, self.BtnLogin)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela de cadastro"))
        self.InputUsuario.setPlaceholderText(_translate("MainWindow", "Usuário:"))
        self.InputSenha.setPlaceholderText(_translate("MainWindow", "Senha:"))
        self.BtnCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.BtnLogin.setText(_translate("MainWindow", "Fazer Login"))
        self.label.setText(_translate("MainWindow", "Cadastro de novo usuário:"))
        self.InputConfirmar.setPlaceholderText(_translate("MainWindow", "Confirme a senha:"))
        self.BtnPermissao.setText(_translate("MainWindow", "Configurar permissões de usuários"))
