# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jrwolfart/projetos python jv/PROJETO-SAL-O-JOVEM-PROGRAMADOR/telas_duda/agenda2.ui'
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
        MainWindow.resize(1391, 889)
        MainWindow.setMinimumSize(QtCore.QSize(1391, 889))
        MainWindow.setMaximumSize(QtCore.QSize(1399, 899))
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
        self.tabWidget.setGeometry(QtCore.QRect(10, 220, 1371, 651))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 231, 249);")
        self.tabWidget.setObjectName("tabWidget")
        self.tabVendas = QtWidgets.QWidget()
        self.tabVendas.setObjectName("tabVendas")
        self.label_3 = QtWidgets.QLabel(self.tabVendas)
        self.label_3.setGeometry(QtCore.QRect(50, 10, 1021, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.TabelaAgenda = QtWidgets.QTableWidget(self.tabVendas)
        self.TabelaAgenda.setEnabled(True)
        self.TabelaAgenda.setGeometry(QtCore.QRect(10, 70, 1351, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabelaAgenda.sizePolicy().hasHeightForWidth())
        self.TabelaAgenda.setSizePolicy(sizePolicy)
        self.TabelaAgenda.setMinimumSize(QtCore.QSize(465, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.TabelaAgenda.setFont(font)
        self.TabelaAgenda.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TabelaAgenda.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TabelaAgenda.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TabelaAgenda.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TabelaAgenda.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TabelaAgenda.setColumnCount(9)
        self.TabelaAgenda.setObjectName("TabelaAgenda")
        self.TabelaAgenda.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgenda.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgenda.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgenda.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgenda.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgenda.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgenda.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgenda.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgenda.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TabelaAgenda.setHorizontalHeaderItem(8, item)
        self.TabelaAgenda.horizontalHeader().setDefaultSectionSize(150)
        self.TabelaAgenda.horizontalHeader().setSortIndicatorShown(False)
        self.TabelaAgenda.horizontalHeader().setStretchLastSection(True)
        self.TabelaAgenda.verticalHeader().setSortIndicatorShown(False)
        self.tabWidget.addTab(self.tabVendas, "")
        self.tabEmitidas = QtWidgets.QWidget()
        self.tabEmitidas.setObjectName("tabEmitidas")
        self.frame_3 = QtWidgets.QFrame(self.tabEmitidas)
        self.frame_3.setGeometry(QtCore.QRect(20, 590, 1111, 80))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lbl_total_emitidas = QtWidgets.QLabel(self.frame_3)
        self.lbl_total_emitidas.setGeometry(QtCore.QRect(20, 20, 1061, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_total_emitidas.setFont(font)
        self.lbl_total_emitidas.setStyleSheet("color: rgb(115, 210, 22);")
        self.lbl_total_emitidas.setText("")
        self.lbl_total_emitidas.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_total_emitidas.setObjectName("lbl_total_emitidas")
        self.label_2 = QtWidgets.QLabel(self.tabEmitidas)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 191, 17))
        self.label_2.setObjectName("label_2")
        self.comboProfi = QtWidgets.QComboBox(self.tabEmitidas)
        self.comboProfi.setGeometry(QtCore.QRect(20, 60, 381, 41))
        self.comboProfi.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-color: rgb(0,0,0);\n"
"color: black")
        self.comboProfi.setObjectName("comboProfi")
        self.TabelaAgendaProfi = QtWidgets.QTableWidget(self.tabEmitidas)
        self.TabelaAgendaProfi.setEnabled(True)
        self.TabelaAgendaProfi.setGeometry(QtCore.QRect(10, 160, 1351, 401))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabelaAgendaProfi.sizePolicy().hasHeightForWidth())
        self.TabelaAgendaProfi.setSizePolicy(sizePolicy)
        self.TabelaAgendaProfi.setMinimumSize(QtCore.QSize(465, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.TabelaAgendaProfi.setFont(font)
        self.TabelaAgendaProfi.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TabelaAgendaProfi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TabelaAgendaProfi.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TabelaAgendaProfi.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TabelaAgendaProfi.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TabelaAgendaProfi.setColumnCount(9)
        self.TabelaAgendaProfi.setObjectName("TabelaAgendaProfi")
        self.TabelaAgendaProfi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgendaProfi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgendaProfi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgendaProfi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgendaProfi.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgendaProfi.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgendaProfi.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgendaProfi.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaAgendaProfi.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TabelaAgendaProfi.setHorizontalHeaderItem(8, item)
        self.TabelaAgendaProfi.horizontalHeader().setDefaultSectionSize(150)
        self.TabelaAgendaProfi.horizontalHeader().setSortIndicatorShown(False)
        self.TabelaAgendaProfi.horizontalHeader().setStretchLastSection(True)
        self.TabelaAgendaProfi.verticalHeader().setSortIndicatorShown(False)
        self.label_6 = QtWidgets.QLabel(self.tabEmitidas)
        self.label_6.setGeometry(QtCore.QRect(510, 10, 361, 131))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("/home/jrwolfart/projetos python jv/PROJETO-SAL-O-JOVEM-PROGRAMADOR/telas_duda/../IMAGENS/PicsArt_10-18-10.18.32.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tabEmitidas, "")
        self.tabPendentes = QtWidgets.QWidget()
        self.tabPendentes.setObjectName("tabPendentes")
        self.TabelaPendentes = QtWidgets.QTableWidget(self.tabPendentes)
        self.TabelaPendentes.setEnabled(True)
        self.TabelaPendentes.setGeometry(QtCore.QRect(0, 60, 1361, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabelaPendentes.sizePolicy().hasHeightForWidth())
        self.TabelaPendentes.setSizePolicy(sizePolicy)
        self.TabelaPendentes.setMinimumSize(QtCore.QSize(465, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.TabelaPendentes.setFont(font)
        self.TabelaPendentes.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TabelaPendentes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TabelaPendentes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TabelaPendentes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TabelaPendentes.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TabelaPendentes.setColumnCount(9)
        self.TabelaPendentes.setObjectName("TabelaPendentes")
        self.TabelaPendentes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaPendentes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaPendentes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaPendentes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaPendentes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaPendentes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaPendentes.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaPendentes.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaPendentes.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TabelaPendentes.setHorizontalHeaderItem(8, item)
        self.TabelaPendentes.horizontalHeader().setDefaultSectionSize(150)
        self.TabelaPendentes.horizontalHeader().setSortIndicatorShown(False)
        self.TabelaPendentes.horizontalHeader().setStretchLastSection(True)
        self.TabelaPendentes.verticalHeader().setSortIndicatorShown(False)
        self.label_4 = QtWidgets.QLabel(self.tabPendentes)
        self.label_4.setGeometry(QtCore.QRect(30, 0, 1021, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tabPendentes, "")
        self.BtnAgendamento = QtWidgets.QPushButton(self.centralwidget)
        self.BtnAgendamento.setGeometry(QtCore.QRect(1050, 120, 191, 51))
        self.BtnAgendamento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnAgendamento.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(245, 121, 0);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 131, 0);\n"
"}\n"
"")
        self.BtnAgendamento.setObjectName("BtnAgendamento")
        self.lbl_dia = QtWidgets.QLabel(self.centralwidget)
        self.lbl_dia.setGeometry(QtCore.QRect(30, 120, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lbl_dia.setFont(font)
        self.lbl_dia.setText("")
        self.lbl_dia.setObjectName("lbl_dia")
        self.InputData = QtWidgets.QDateEdit(self.centralwidget)
        self.InputData.setGeometry(QtCore.QRect(540, 120, 251, 51))
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
        self.BtnHoje = QtWidgets.QPushButton(self.centralwidget)
        self.BtnHoje.setGeometry(QtCore.QRect(820, 120, 171, 51))
        self.BtnHoje.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnHoje.setStyleSheet("QPushButton {     \n"
"    background-color:rgb(78, 154, 6);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    \n"
"}\n"
"QPushButton:hover {   \n"
"    background-color:rgb(85, 165, 10);\n"
"}")
        self.BtnHoje.setObjectName("BtnHoje")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 20, 541, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.lbl_dia.raise_()
        self.lbl_id_user.raise_()
        self.tabWidget.raise_()
        self.BtnAgendamento.raise_()
        self.InputData.raise_()
        self.BtnHoje.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AGENDA DE ATENDIMENTOS"))
        self.label_3.setText(_translate("MainWindow", "Dê um duplo clique no agendamento para marca-lo como efetuado"))
        self.TabelaAgenda.setSortingEnabled(False)
        item = self.TabelaAgenda.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data"))
        item = self.TabelaAgenda.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Hora"))
        item = self.TabelaAgenda.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Minutos aprox."))
        item = self.TabelaAgenda.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Profissional"))
        item = self.TabelaAgenda.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cliente"))
        item = self.TabelaAgenda.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Telefone do Cliente"))
        item = self.TabelaAgenda.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Serviço agendado"))
        item = self.TabelaAgenda.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Situação"))
        item = self.TabelaAgenda.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVendas), _translate("MainWindow", "Todos a partir da data selecionada"))
        self.label_2.setText(_translate("MainWindow", "Selecione o Profissional"))
        self.TabelaAgendaProfi.setSortingEnabled(False)
        item = self.TabelaAgendaProfi.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data"))
        item = self.TabelaAgendaProfi.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Hora"))
        item = self.TabelaAgendaProfi.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tempo Minutos"))
        item = self.TabelaAgendaProfi.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cliente"))
        item = self.TabelaAgendaProfi.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Telefone do Cliente"))
        item = self.TabelaAgendaProfi.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Serviço agendado"))
        item = self.TabelaAgendaProfi.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Fidelizado"))
        item = self.TabelaAgendaProfi.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Situação"))
        item = self.TabelaAgendaProfi.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEmitidas), _translate("MainWindow", "Agenda do Profissional"))
        self.TabelaPendentes.setSortingEnabled(False)
        item = self.TabelaPendentes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data"))
        item = self.TabelaPendentes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Hora"))
        item = self.TabelaPendentes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Minutos aprox."))
        item = self.TabelaPendentes.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Profissional"))
        item = self.TabelaPendentes.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cliente"))
        item = self.TabelaPendentes.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Telefone do Cliente"))
        item = self.TabelaPendentes.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Serviço agendado"))
        item = self.TabelaPendentes.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Situação"))
        item = self.TabelaPendentes.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "ID"))
        self.label_4.setText(_translate("MainWindow", "Dê um duplo clique no agendamento para marca-lo como efetuado"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPendentes), _translate("MainWindow", "Serviços pendentes"))
        self.BtnAgendamento.setText(_translate("MainWindow", "Novo Agendamento"))
        self.BtnHoje.setText(_translate("MainWindow", "Seleciona o dia de Hoje"))
        self.label_5.setText(_translate("MainWindow", "Agenda de atendimentos:"))
