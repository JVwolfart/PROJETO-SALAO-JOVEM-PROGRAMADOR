# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jrwolfart/projetos python jv/PROJETO-SAL-O-JOVEM-PROGRAMADOR/telas_duda/manut_agendamento.ui'
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
        MainWindow.resize(877, 600)
        MainWindow.setMinimumSize(QtCore.QSize(877, 600))
        MainWindow.setMaximumSize(QtCore.QSize(887, 610))
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"background-color: rgb(255, 231, 249);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_id_user = QtWidgets.QLabel(self.centralwidget)
        self.lbl_id_user.setGeometry(QtCore.QRect(1080, 30, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lbl_id_user.setFont(font)
        self.lbl_id_user.setStyleSheet("color: rgb(62, 132, 238);")
        self.lbl_id_user.setText("")
        self.lbl_id_user.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_id_user.setObjectName("lbl_id_user")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(520, 230, 411, 41))
        self.label_11.setObjectName("label_11")
        self.BtnAlterar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnAlterar.setGeometry(QtCore.QRect(40, 500, 151, 51))
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
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 240, 121, 22))
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 240, 271, 22))
        self.label_6.setObjectName("label_6")
        self.cliente = QtWidgets.QLineEdit(self.centralwidget)
        self.cliente.setEnabled(False)
        self.cliente.setGeometry(QtCore.QRect(40, 180, 241, 41))
        self.cliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(32, 74, 135);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.cliente.setText("")
        self.cliente.setReadOnly(False)
        self.cliente.setObjectName("cliente")
        self.hora = QtWidgets.QTimeEdit(self.centralwidget)
        self.hora.setEnabled(True)
        self.hora.setGeometry(QtCore.QRect(40, 270, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.hora.setFont(font)
        self.hora.setMouseTracking(True)
        self.hora.setTabletTracking(True)
        self.hora.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.hora.setProperty("showGroupSeparator", False)
        self.hora.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(8, 0, 0)))
        self.hora.setCalendarPopup(True)
        self.hora.setCurrentSectionIndex(0)
        self.hora.setTimeSpec(QtCore.Qt.LocalTime)
        self.hora.setObjectName("hora")
        self.data_agendamento = QtWidgets.QLineEdit(self.centralwidget)
        self.data_agendamento.setEnabled(False)
        self.data_agendamento.setGeometry(QtCore.QRect(40, 110, 241, 41))
        self.data_agendamento.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(32, 74, 135);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.data_agendamento.setReadOnly(False)
        self.data_agendamento.setObjectName("data_agendamento")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 221, 17))
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(390, 160, 201, 20))
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 160, 201, 20))
        self.label_9.setObjectName("label_9")
        self.BtnSair = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSair.setGeometry(QtCore.QRect(200, 500, 141, 51))
        self.BtnSair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnSair.setStyleSheet("QPushButton {     \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(239, 41, 41);\n"
"    border-radius: 10px;\n"
"    \n"
"}\n"
"QPushButton:hover {   \n"
"    background-color: rgb(249, 51, 51);\n"
"}\n"
"")
        self.BtnSair.setObjectName("BtnSair")
        self.comboServicos = QtWidgets.QComboBox(self.centralwidget)
        self.comboServicos.setGeometry(QtCore.QRect(190, 270, 301, 41))
        self.comboServicos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.comboServicos.setObjectName("comboServicos")
        self.InputTempo = QtWidgets.QLineEdit(self.centralwidget)
        self.InputTempo.setEnabled(False)
        self.InputTempo.setGeometry(QtCore.QRect(520, 270, 101, 41))
        self.InputTempo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(32, 74, 135);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.InputTempo.setText("")
        self.InputTempo.setReadOnly(False)
        self.InputTempo.setObjectName("InputTempo")
        self.telefone = QtWidgets.QLineEdit(self.centralwidget)
        self.telefone.setEnabled(False)
        self.telefone.setGeometry(QtCore.QRect(390, 180, 291, 41))
        self.telefone.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(32, 74, 135);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.telefone.setText("")
        self.telefone.setReadOnly(False)
        self.telefone.setObjectName("telefone")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 370, 271, 22))
        self.label_7.setObjectName("label_7")
        self.comboStatus = QtWidgets.QComboBox(self.centralwidget)
        self.comboStatus.setGeometry(QtCore.QRect(40, 400, 301, 41))
        self.comboStatus.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.comboStatus.setObjectName("comboStatus")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.InputIdAgenda = QtWidgets.QLineEdit(self.centralwidget)
        self.InputIdAgenda.setEnabled(False)
        self.InputIdAgenda.setGeometry(QtCore.QRect(390, 110, 281, 41))
        self.InputIdAgenda.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(32, 74, 135);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.InputIdAgenda.setReadOnly(False)
        self.InputIdAgenda.setObjectName("InputIdAgenda")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(390, 70, 411, 41))
        self.label_12.setObjectName("label_12")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 330, 511, 241))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("/home/jrwolfart/projetos python jv/PROJETO-SAL-O-JOVEM-PROGRAMADOR/telas_duda/../IMAGENS/PicsArt_10-18-10.18.32.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 10, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MANUTENÇÃO DE AGENDAMENTOS"))
        self.label_11.setText(_translate("MainWindow", "Tempo médio estimado em minutos do serviço: "))
        self.BtnAlterar.setText(_translate("MainWindow", "Alterar"))
        self.label_8.setText(_translate("MainWindow", "Informe a Hora:"))
        self.label_6.setText(_translate("MainWindow", "Selecione o serviço Desejado"))
        self.cliente.setPlaceholderText(_translate("MainWindow", "Nome do Cliente"))
        self.data_agendamento.setPlaceholderText(_translate("MainWindow", "Data do agendamento"))
        self.label_3.setText(_translate("MainWindow", "Data do agendamento:"))
        self.label_10.setText(_translate("MainWindow", "Telefone do Cliente:"))
        self.label_9.setText(_translate("MainWindow", "Nome do Cliente:"))
        self.BtnSair.setText(_translate("MainWindow", "Sair"))
        self.InputTempo.setPlaceholderText(_translate("MainWindow", "Minutos"))
        self.telefone.setPlaceholderText(_translate("MainWindow", "Telefone do Cliente"))
        self.label_7.setText(_translate("MainWindow", "Status do agendamento"))
        self.comboStatus.setItemText(0, _translate("MainWindow", "Agendado"))
        self.comboStatus.setItemText(1, _translate("MainWindow", "Cancelado pelo cliente"))
        self.comboStatus.setItemText(2, _translate("MainWindow", "Serviço efetuado"))
        self.comboStatus.setItemText(3, _translate("MainWindow", "Eliminado"))
        self.comboStatus.setItemText(4, _translate("MainWindow", "Cliente não compareceu"))
        self.InputIdAgenda.setText(_translate("MainWindow", "Id do agendamento"))
        self.InputIdAgenda.setPlaceholderText(_translate("MainWindow", "Minutos"))
        self.label_12.setText(_translate("MainWindow", "Id do agendamento"))
        self.label_5.setText(_translate("MainWindow", "Manutenção de agendamento:"))
