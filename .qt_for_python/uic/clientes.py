# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/clientes.ui'
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
        MainWindow.resize(1026, 728)
        MainWindow.setMinimumSize(QtCore.QSize(1026, 728))
        MainWindow.setMaximumSize(QtCore.QSize(1036, 738))
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(215, 139, 185);")
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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 991, 691))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 231, 249);")
        self.tabWidget.setObjectName("tabWidget")
        self.tabClientes = QtWidgets.QWidget()
        self.tabClientes.setObjectName("tabClientes")
        self.BtnInserir = QtWidgets.QPushButton(self.tabClientes)
        self.BtnInserir.setGeometry(QtCore.QRect(250, 310, 311, 41))
        self.BtnInserir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnInserir.setStyleSheet("QPushButton {     \n"
"    background-color: rgb(0, 170, 0);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {   \n"
"    background-color: rgb(0, 190, 0);\n"
"}\n"
"QPushButton:pressed {   \n"
"    background-color: rgb(0, 200, 0);\n"
"}")
        self.BtnInserir.setObjectName("BtnInserir")
        self.label = QtWidgets.QLabel(self.tabClientes)
        self.label.setGeometry(QtCore.QRect(30, 180, 171, 22))
        self.label.setObjectName("label")
        self.Inome = QtWidgets.QLineEdit(self.tabClientes)
        self.Inome.setEnabled(True)
        self.Inome.setGeometry(QtCore.QRect(20, 120, 861, 41))
        self.Inome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.Inome.setReadOnly(False)
        self.Inome.setObjectName("Inome")
        self.Itelefone = QtWidgets.QLineEdit(self.tabClientes)
        self.Itelefone.setEnabled(True)
        self.Itelefone.setGeometry(QtCore.QRect(20, 210, 291, 41))
        self.Itelefone.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.Itelefone.setFrame(True)
        self.Itelefone.setCursorPosition(15)
        self.Itelefone.setDragEnabled(False)
        self.Itelefone.setReadOnly(False)
        self.Itelefone.setPlaceholderText("")
        self.Itelefone.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Itelefone.setClearButtonEnabled(True)
        self.Itelefone.setObjectName("Itelefone")
        self.CbSexo = QtWidgets.QComboBox(self.tabClientes)
        self.CbSexo.setGeometry(QtCore.QRect(380, 210, 311, 41))
        self.CbSexo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(46, 52, 54);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.CbSexo.setObjectName("CbSexo")
        self.CbSexo.addItem("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/../IMAGENS/genero feminino.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CbSexo.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/../IMAGENS/genero masculino.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CbSexo.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/../IMAGENS/genero outros.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CbSexo.addItem(icon2, "")
        self.label_2 = QtWidgets.QLabel(self.tabClientes)
        self.label_2.setGeometry(QtCore.QRect(390, 180, 171, 22))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tabClientes)
        self.label_3.setGeometry(QtCore.QRect(420, 390, 531, 241))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/../IMAGENS/PicsArt_10-18-10.18.32.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tabClientes)
        self.label_5.setGeometry(QtCore.QRect(260, 40, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tabClientes, "")
        self.tabManut = QtWidgets.QWidget()
        self.tabManut.setObjectName("tabManut")
        self.label_4 = QtWidgets.QLabel(self.tabManut)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 921, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.TabelaClientes = QtWidgets.QTableWidget(self.tabManut)
        self.TabelaClientes.setEnabled(True)
        self.TabelaClientes.setGeometry(QtCore.QRect(10, 160, 961, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabelaClientes.sizePolicy().hasHeightForWidth())
        self.TabelaClientes.setSizePolicy(sizePolicy)
        self.TabelaClientes.setMinimumSize(QtCore.QSize(465, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.TabelaClientes.setFont(font)
        self.TabelaClientes.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TabelaClientes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TabelaClientes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TabelaClientes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TabelaClientes.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TabelaClientes.setObjectName("TabelaClientes")
        self.TabelaClientes.setColumnCount(6)
        self.TabelaClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaClientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaClientes.setHorizontalHeaderItem(5, item)
        self.TabelaClientes.horizontalHeader().setDefaultSectionSize(150)
        self.TabelaClientes.horizontalHeader().setSortIndicatorShown(False)
        self.TabelaClientes.horizontalHeader().setStretchLastSection(True)
        self.label_6 = QtWidgets.QLabel(self.tabManut)
        self.label_6.setGeometry(QtCore.QRect(260, 30, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tabManut, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro e Manutenção de Clientes"))
        self.BtnInserir.setText(_translate("MainWindow", "Inserir novo Cliente"))
        self.label.setText(_translate("MainWindow", "Telefone/Whatsapp:"))
        self.Inome.setPlaceholderText(_translate("MainWindow", "Nome do Cliente"))
        self.Itelefone.setInputMask(_translate("MainWindow", "(99) 09999-9999"))
        self.Itelefone.setText(_translate("MainWindow", "() -"))
        self.CbSexo.setItemText(0, _translate("MainWindow", "Selecione um Gênero"))
        self.CbSexo.setItemText(1, _translate("MainWindow", "Feminino"))
        self.CbSexo.setItemText(2, _translate("MainWindow", "Masculino"))
        self.CbSexo.setItemText(3, _translate("MainWindow", "Outro"))
        self.label_2.setText(_translate("MainWindow", "Gênero (sexo) :"))
        self.label_5.setText(_translate("MainWindow", "Cadastro de novo cliente:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabClientes), _translate("MainWindow", "Cadastro de Clientes"))
        self.label_4.setText(_translate("MainWindow", "Dê um duplo clique no Cliente para alterar seu cadastro."))
        self.TabelaClientes.setSortingEnabled(False)
        item = self.TabelaClientes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.TabelaClientes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome do Cliente"))
        item = self.TabelaClientes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Telefone de contato"))
        item = self.TabelaClientes.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Gênero/Sexo"))
        item = self.TabelaClientes.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        item = self.TabelaClientes.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fidelizado"))
        self.label_6.setText(_translate("MainWindow", "Manutenção de cliente:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabManut), _translate("MainWindow", "Manutenção de Clientes"))
