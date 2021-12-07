# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/manut_nf.ui'
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
        MainWindow.resize(1131, 794)
        MainWindow.setMinimumSize(QtCore.QSize(1131, 794))
        MainWindow.setMaximumSize(QtCore.QSize(1141, 800))
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 141, 31))
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 620, 1081, 80))
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
        self.Id_Cliente = QtWidgets.QSpinBox(self.centralwidget)
        self.Id_Cliente.setEnabled(False)
        self.Id_Cliente.setGeometry(QtCore.QRect(420, 80, 111, 41))
        self.Id_Cliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.Id_Cliente.setReadOnly(True)
        self.Id_Cliente.setMaximum(2147483647)
        self.Id_Cliente.setObjectName("Id_Cliente")
        self.frame_vip = QtWidgets.QFrame(self.centralwidget)
        self.frame_vip.setGeometry(QtCore.QRect(510, 260, 311, 91))
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
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 260, 191, 22))
        self.label_6.setObjectName("label_6")
        self.BtnInserir = QtWidgets.QPushButton(self.centralwidget)
        self.BtnInserir.setGeometry(QtCore.QRect(870, 280, 161, 51))
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
        self.Inome = QtWidgets.QLineEdit(self.centralwidget)
        self.Inome.setEnabled(False)
        self.Inome.setGeometry(QtCore.QRect(580, 80, 531, 41))
        self.Inome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(32, 74, 135);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.Inome.setReadOnly(False)
        self.Inome.setObjectName("Inome")
        self.comboProfi = QtWidgets.QComboBox(self.centralwidget)
        self.comboProfi.setGeometry(QtCore.QRect(350, 180, 401, 41))
        self.comboProfi.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.comboProfi.setObjectName("comboProfi")
        self.InputPfat = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.InputPfat.setEnabled(False)
        self.InputPfat.setGeometry(QtCore.QRect(280, 290, 171, 41))
        self.InputPfat.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: rgb(203, 137, 176);")
        self.InputPfat.setMaximum(99999.99)
        self.InputPfat.setObjectName("InputPfat")
        self.InputPtab = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.InputPtab.setEnabled(False)
        self.InputPtab.setGeometry(QtCore.QRect(30, 290, 181, 41))
        self.InputPtab.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: rgb(203, 137, 176);")
        self.InputPtab.setMaximum(99999.99)
        self.InputPtab.setObjectName("InputPtab")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(770, 140, 291, 31))
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 191, 22))
        self.label_5.setObjectName("label_5")
        self.comboServicos = QtWidgets.QComboBox(self.centralwidget)
        self.comboServicos.setGeometry(QtCore.QRect(30, 180, 311, 41))
        self.comboServicos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.comboServicos.setObjectName("comboServicos")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 260, 191, 22))
        self.label_7.setObjectName("label_7")
        self.TabelaItensNf = QtWidgets.QTableWidget(self.centralwidget)
        self.TabelaItensNf.setEnabled(True)
        self.TabelaItensNf.setGeometry(QtCore.QRect(30, 380, 1081, 231))
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
        self.NumeroNf = QtWidgets.QSpinBox(self.centralwidget)
        self.NumeroNf.setEnabled(False)
        self.NumeroNf.setGeometry(QtCore.QRect(190, 80, 131, 41))
        self.NumeroNf.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.NumeroNf.setReadOnly(True)
        self.NumeroNf.setMaximum(2147483647)
        self.NumeroNf.setObjectName("NumeroNf")
        self.BtnCalcularNf = QtWidgets.QPushButton(self.centralwidget)
        self.BtnCalcularNf.setGeometry(QtCore.QRect(480, 710, 231, 51))
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
        self.comboFpag = QtWidgets.QComboBox(self.centralwidget)
        self.comboFpag.setGeometry(QtCore.QRect(770, 180, 341, 41))
        self.comboFpag.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.comboFpag.setObjectName("comboFpag")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(350, 150, 221, 22))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(350, 80, 71, 31))
        self.label_10.setObjectName("label_10")
        self.BtnCancelarNf = QtWidgets.QPushButton(self.centralwidget)
        self.BtnCancelarNf.setGeometry(QtCore.QRect(830, 710, 191, 51))
        self.BtnCancelarNf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnCancelarNf.setStyleSheet("QPushButton {     \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(239, 41, 41);\n"
"    border-radius: 10px;\n"
"    \n"
"}\n"
"QPushButton:hover {   \n"
"    background-color: rgb(249, 51, 51);\n"
"}\n"
"")
        self.BtnCancelarNf.setObjectName("BtnCancelarNf")
        self.Istatus = QtWidgets.QLineEdit(self.centralwidget)
        self.Istatus.setEnabled(False)
        self.Istatus.setGeometry(QtCore.QRect(770, 20, 341, 41))
        self.Istatus.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(32, 74, 135);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"")
        self.Istatus.setReadOnly(False)
        self.Istatus.setObjectName("Istatus")
        self.BtnSair = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSair.setGeometry(QtCore.QRect(190, 710, 171, 51))
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 10, 511, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manutenção de nota fiscal"))
        self.label_3.setText(_translate("MainWindow", "Número da nota fiscal:"))
        self.lbhs_2.setText(_translate("MainWindow", "20%"))
        self.lbhs.setText(_translate("MainWindow", "Desconto Fidelidade"))
        self.lbhs_3.setText(_translate("MainWindow", "0%"))
        self.label_6.setText(_translate("MainWindow", "Preço faturado"))
        self.BtnInserir.setText(_translate("MainWindow", "Inserir serviço"))
        self.Inome.setPlaceholderText(_translate("MainWindow", "Nome do Cliente"))
        self.label_9.setText(_translate("MainWindow", "Selecione a forma de pagamento"))
        self.label_5.setText(_translate("MainWindow", "Selecione o serviço"))
        self.label_7.setText(_translate("MainWindow", "Preço tabela"))
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
        self.label_8.setText(_translate("MainWindow", "Selecione o profissional"))
        self.label_10.setText(_translate("MainWindow", "ID Cliente:"))
        self.BtnCancelarNf.setText(_translate("MainWindow", "Cancelar nota fiscal"))
        self.Istatus.setPlaceholderText(_translate("MainWindow", "Status da nota"))
        self.BtnSair.setText(_translate("MainWindow", "Sair"))
        self.label_4.setText(_translate("MainWindow", "Manutenção de nota fiscal:"))
