# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/emissao_nf.ui'
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
        MainWindow.resize(1125, 835)
        MainWindow.setMinimumSize(QtCore.QSize(1125, 835))
        MainWindow.setMaximumSize(QtCore.QSize(1135, 845))
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(216, 164, 194);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_id_user = QtWidgets.QLabel(self.centralwidget)
        self.lbl_id_user.setGeometry(QtCore.QRect(930, 30, 41, 51))
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
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 1101, 751))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 231, 249);")
        self.tabWidget.setObjectName("tabWidget")
        self.tabNf = QtWidgets.QWidget()
        self.tabNf.setObjectName("tabNf")
        self.BtnGerarNf = QtWidgets.QPushButton(self.tabNf)
        self.BtnGerarNf.setGeometry(QtCore.QRect(530, 120, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.BtnGerarNf.setFont(font)
        self.BtnGerarNf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnGerarNf.setStyleSheet("QPushButton {     \n"
"    background-color:rgb(78, 154, 6);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    \n"
"}\n"
"QPushButton:hover {   \n"
"    background-color:rgb(85, 165, 10);\n"
"}\n"
"")
        self.BtnGerarNf.setObjectName("BtnGerarNf")
        self.comboClientes = QtWidgets.QComboBox(self.tabNf)
        self.comboClientes.setGeometry(QtCore.QRect(60, 120, 421, 41))
        self.comboClientes.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.comboClientes.setObjectName("comboClientes")
        self.comboClientes.addItem("")
        self.label_2 = QtWidgets.QLabel(self.tabNf)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.tabNf)
        self.label_4.setGeometry(QtCore.QRect(290, 280, 751, 371))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/../IMAGENS/PicsArt_10-18-10.18.32.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.vip = QtWidgets.QLabel(self.tabNf)
        self.vip.setEnabled(True)
        self.vip.setGeometry(QtCore.QRect(700, 60, 191, 131))
        self.vip.setText("")
        self.vip.setTextFormat(QtCore.Qt.AutoText)
        self.vip.setPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/../IMAGENS/logo-cliente-vip_Prancheta-1-cópia-3-768x384.png"))
        self.vip.setScaledContents(True)
        self.vip.setObjectName("vip")
        self.label_4.raise_()
        self.BtnGerarNf.raise_()
        self.comboClientes.raise_()
        self.label_2.raise_()
        self.vip.raise_()
        self.tabWidget.addTab(self.tabNf, "")
        self.tabItens = QtWidgets.QWidget()
        self.tabItens.setObjectName("tabItens")
        self.TabelaItensNf = QtWidgets.QTableWidget(self.tabItens)
        self.TabelaItensNf.setEnabled(True)
        self.TabelaItensNf.setGeometry(QtCore.QRect(10, 320, 1081, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabelaItensNf.sizePolicy().hasHeightForWidth())
        self.TabelaItensNf.setSizePolicy(sizePolicy)
        self.TabelaItensNf.setMinimumSize(QtCore.QSize(465, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TabelaItensNf.setFont(font)
        self.TabelaItensNf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TabelaItensNf.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TabelaItensNf.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TabelaItensNf.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TabelaItensNf.setObjectName("TabelaItensNf")
        self.TabelaItensNf.setColumnCount(7)
        self.TabelaItensNf.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaItensNf.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaItensNf.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaItensNf.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaItensNf.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaItensNf.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaItensNf.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaItensNf.setHorizontalHeaderItem(6, item)
        self.TabelaItensNf.horizontalHeader().setDefaultSectionSize(150)
        self.TabelaItensNf.horizontalHeader().setSortIndicatorShown(True)
        self.TabelaItensNf.horizontalHeader().setStretchLastSection(True)
        self.BtnCalcularNf = QtWidgets.QPushButton(self.tabItens)
        self.BtnCalcularNf.setGeometry(QtCore.QRect(430, 650, 231, 51))
        self.BtnCalcularNf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnCalcularNf.setStyleSheet("QPushButton {     \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(245, 121, 0);\n"
"    border-radius: 10px;\n"
"    \n"
"}\n"
"QPushButton:hover {   \n"
"    background-color: rgb(250, 131, 0)\n"
"}\n"
"")
        self.BtnCalcularNf.setObjectName("BtnCalcularNf")
        self.label_3 = QtWidgets.QLabel(self.tabItens)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 141, 31))
        self.label_3.setObjectName("label_3")
        self.comboServicos = QtWidgets.QComboBox(self.tabItens)
        self.comboServicos.setGeometry(QtCore.QRect(20, 120, 321, 41))
        self.comboServicos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.comboServicos.setObjectName("comboServicos")
        self.label_5 = QtWidgets.QLabel(self.tabItens)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 191, 22))
        self.label_5.setObjectName("label_5")
        self.InputPtab = QtWidgets.QDoubleSpinBox(self.tabItens)
        self.InputPtab.setEnabled(False)
        self.InputPtab.setGeometry(QtCore.QRect(50, 230, 171, 41))
        self.InputPtab.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: rgb(202, 136, 175);")
        self.InputPtab.setMaximum(99999.99)
        self.InputPtab.setObjectName("InputPtab")
        self.InputPfat = QtWidgets.QDoubleSpinBox(self.tabItens)
        self.InputPfat.setEnabled(False)
        self.InputPfat.setGeometry(QtCore.QRect(260, 230, 171, 41))
        self.InputPfat.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: rgb(203, 137, 176);")
        self.InputPfat.setMaximum(99999.99)
        self.InputPfat.setObjectName("InputPfat")
        self.BtnInserir = QtWidgets.QPushButton(self.tabItens)
        self.BtnInserir.setGeometry(QtCore.QRect(830, 220, 171, 51))
        self.BtnInserir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnInserir.setStyleSheet("QPushButton {     \n"
"    background-color:rgb(78, 154, 6);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    \n"
"}\n"
"QPushButton:hover {   \n"
"    background-color:rgb(85, 165, 10);\n"
"}\n"
"")
        self.BtnInserir.setObjectName("BtnInserir")
        self.NumeroNf = QtWidgets.QSpinBox(self.tabItens)
        self.NumeroNf.setEnabled(False)
        self.NumeroNf.setGeometry(QtCore.QRect(170, 20, 161, 41))
        self.NumeroNf.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.NumeroNf.setReadOnly(True)
        self.NumeroNf.setMaximum(2147483647)
        self.NumeroNf.setObjectName("NumeroNf")
        self.frame_2 = QtWidgets.QFrame(self.tabItens)
        self.frame_2.setGeometry(QtCore.QRect(10, 560, 1081, 80))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lbl_total = QtWidgets.QLabel(self.frame_2)
        self.lbl_total.setGeometry(QtCore.QRect(20, 20, 931, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_total.setFont(font)
        self.lbl_total.setStyleSheet("color: rgb(115, 210, 22);")
        self.lbl_total.setText("")
        self.lbl_total.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_total.setObjectName("lbl_total")
        self.label_8 = QtWidgets.QLabel(self.tabItens)
        self.label_8.setGeometry(QtCore.QRect(360, 90, 221, 22))
        self.label_8.setObjectName("label_8")
        self.comboProfi = QtWidgets.QComboBox(self.tabItens)
        self.comboProfi.setGeometry(QtCore.QRect(360, 120, 381, 41))
        self.comboProfi.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.comboProfi.setObjectName("comboProfi")
        self.label_9 = QtWidgets.QLabel(self.tabItens)
        self.label_9.setGeometry(QtCore.QRect(750, 80, 241, 31))
        self.label_9.setObjectName("label_9")
        self.comboFpag = QtWidgets.QComboBox(self.tabItens)
        self.comboFpag.setGeometry(QtCore.QRect(750, 120, 281, 41))
        self.comboFpag.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.comboFpag.setObjectName("comboFpag")
        self.label_7 = QtWidgets.QLabel(self.tabItens)
        self.label_7.setGeometry(QtCore.QRect(50, 200, 191, 22))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.tabItens)
        self.label_6.setGeometry(QtCore.QRect(260, 200, 191, 22))
        self.label_6.setObjectName("label_6")
        self.frame_vip = QtWidgets.QFrame(self.tabItens)
        self.frame_vip.setGeometry(QtCore.QRect(460, 199, 311, 91))
        self.frame_vip.setStyleSheet("background-color: rgb(203, 137, 176);")
        self.frame_vip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_vip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_vip.setObjectName("frame_vip")
        self.lbhs_2 = QtWidgets.QLabel(self.frame_vip)
        self.lbhs_2.setGeometry(QtCore.QRect(230, 40, 41, 20))
        self.lbhs_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbhs_2.setObjectName("lbhs_2")
        self.lbhs = QtWidgets.QLabel(self.frame_vip)
        self.lbhs.setGeometry(QtCore.QRect(60, 10, 241, 20))
        self.lbhs.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbhs.setObjectName("lbhs")
        self.lbhs_3 = QtWidgets.QLabel(self.frame_vip)
        self.lbhs_3.setGeometry(QtCore.QRect(25, 40, 31, 20))
        self.lbhs_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbhs_3.setObjectName("lbhs_3")
        self.VipSlider = QtWidgets.QSlider(self.frame_vip)
        self.VipSlider.setEnabled(True)
        self.VipSlider.setGeometry(QtCore.QRect(60, 40, 160, 21))
        self.VipSlider.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.VipSlider.setMaximum(20)
        self.VipSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VipSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.VipSlider.setObjectName("VipSlider")
        self.Id_Cliente = QtWidgets.QSpinBox(self.tabItens)
        self.Id_Cliente.setEnabled(False)
        self.Id_Cliente.setGeometry(QtCore.QRect(430, 20, 121, 41))
        self.Id_Cliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.Id_Cliente.setReadOnly(True)
        self.Id_Cliente.setMaximum(2147483647)
        self.Id_Cliente.setObjectName("Id_Cliente")
        self.label_10 = QtWidgets.QLabel(self.tabItens)
        self.label_10.setGeometry(QtCore.QRect(360, 20, 71, 31))
        self.label_10.setObjectName("label_10")
        self.Inome = QtWidgets.QLineEdit(self.tabItens)
        self.Inome.setEnabled(False)
        self.Inome.setGeometry(QtCore.QRect(560, 20, 471, 41))
        self.Inome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(32, 74, 135);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.Inome.setReadOnly(False)
        self.Inome.setObjectName("Inome")
        self.tabWidget.addTab(self.tabItens, "")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(230, 10, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FATURAMENTO - VENDAS (Emissão de Nota Fiscal Avulsa)"))
        self.BtnGerarNf.setText(_translate("MainWindow", "Gerar nota fiscal"))
        self.comboClientes.setItemText(0, _translate("MainWindow", "Selecione um Cliente"))
        self.label_2.setText(_translate("MainWindow", "Selecione o cliente:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNf), _translate("MainWindow", "Dados da nota fiscal"))
        self.TabelaItensNf.setSortingEnabled(True)
        item = self.TabelaItensNf.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID do item"))
        item = self.TabelaItensNf.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Descrição"))
        item = self.TabelaItensNf.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Profissional"))
        item = self.TabelaItensNf.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Preço faturado"))
        item = self.TabelaItensNf.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fidelidade"))
        item = self.TabelaItensNf.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Desconto %"))
        item = self.TabelaItensNf.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Forma de pagamento"))
        self.BtnCalcularNf.setText(_translate("MainWindow", "Emitir nota fiscal"))
        self.label_3.setText(_translate("MainWindow", "Número da nota fiscal:"))
        self.label_5.setText(_translate("MainWindow", "Selecione o serviço"))
        self.BtnInserir.setText(_translate("MainWindow", "Inserir serviço"))
        self.label_8.setText(_translate("MainWindow", "Selecione o profissional"))
        self.label_9.setText(_translate("MainWindow", "Selecione a forma de pagamento"))
        self.label_7.setText(_translate("MainWindow", "Preço tabela"))
        self.label_6.setText(_translate("MainWindow", "Preço faturado"))
        self.lbhs_2.setText(_translate("MainWindow", "20%"))
        self.lbhs.setText(_translate("MainWindow", "Desconto Fidelidade"))
        self.lbhs_3.setText(_translate("MainWindow", "0%"))
        self.label_10.setText(_translate("MainWindow", "ID Cliente:"))
        self.Inome.setPlaceholderText(_translate("MainWindow", "Nome do Cliente"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabItens), _translate("MainWindow", "Itens da nota fiscal"))
        self.label_11.setText(_translate("MainWindow", "Emissão de nota fiscal Avulsa (Venda Direta):"))
