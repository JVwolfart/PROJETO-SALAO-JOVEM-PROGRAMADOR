# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/estatisticas_genero_futuro.ui'
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
        MainWindow.resize(1179, 966)
        MainWindow.setMinimumSize(QtCore.QSize(1179, 966))
        MainWindow.setMaximumSize(QtCore.QSize(1179, 966))
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
        self.RbTodas = QtWidgets.QRadioButton(self.centralwidget)
        self.RbTodas.setGeometry(QtCore.QRect(750, 250, 151, 28))
        self.RbTodas.setChecked(True)
        self.RbTodas.setObjectName("RbTodas")
        self.lbl_escolha = QtWidgets.QLabel(self.centralwidget)
        self.lbl_escolha.setGeometry(QtCore.QRect(50, 240, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lbl_escolha.setFont(font)
        self.lbl_escolha.setText("")
        self.lbl_escolha.setObjectName("lbl_escolha")
        self.RbIntervaloDatas = QtWidgets.QRadioButton(self.centralwidget)
        self.RbIntervaloDatas.setGeometry(QtCore.QRect(950, 250, 171, 28))
        self.RbIntervaloDatas.setObjectName("RbIntervaloDatas")
        self.TabelaVendasGenero = QtWidgets.QTableWidget(self.centralwidget)
        self.TabelaVendasGenero.setEnabled(True)
        self.TabelaVendasGenero.setGeometry(QtCore.QRect(40, 340, 1111, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabelaVendasGenero.sizePolicy().hasHeightForWidth())
        self.TabelaVendasGenero.setSizePolicy(sizePolicy)
        self.TabelaVendasGenero.setMinimumSize(QtCore.QSize(465, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.TabelaVendasGenero.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        self.TabelaVendasGenero.setFont(font)
        self.TabelaVendasGenero.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TabelaVendasGenero.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.TabelaVendasGenero.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TabelaVendasGenero.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TabelaVendasGenero.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TabelaVendasGenero.setObjectName("TabelaVendasGenero")
        self.TabelaVendasGenero.setColumnCount(6)
        self.TabelaVendasGenero.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaVendasGenero.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaVendasGenero.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaVendasGenero.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaVendasGenero.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaVendasGenero.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaVendasGenero.setHorizontalHeaderItem(5, item)
        self.TabelaVendasGenero.horizontalHeader().setDefaultSectionSize(150)
        self.TabelaVendasGenero.horizontalHeader().setSortIndicatorShown(False)
        self.TabelaVendasGenero.horizontalHeader().setStretchLastSection(True)
        self.TabelaVendasGenero.verticalHeader().setSortIndicatorShown(False)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(40, 860, 1111, 80))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lbl_total = QtWidgets.QLabel(self.frame_2)
        self.lbl_total.setGeometry(QtCore.QRect(20, 20, 1061, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_total.setFont(font)
        self.lbl_total.setStyleSheet("color: rgb(115, 210, 22);")
        self.lbl_total.setText("")
        self.lbl_total.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_total.setObjectName("lbl_total")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(810, 20, 361, 161))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/JP/PROJETO SALÃO/telas_duda/../IMAGENS/PicsArt_10-18-10.18.32.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 70, 751, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Faturamento previsto por gênero baseado na agenda"))
        self.RbTodas.setText(_translate("MainWindow", "Todo o período"))
        self.RbIntervaloDatas.setText(_translate("MainWindow", "Intervalo de datas"))
        self.TabelaVendasGenero.setSortingEnabled(False)
        item = self.TabelaVendasGenero.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Gênero"))
        item = self.TabelaVendasGenero.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Total faturado"))
        item = self.TabelaVendasGenero.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "N° de atendimentos"))
        item = self.TabelaVendasGenero.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tempo aproximado minutos"))
        item = self.TabelaVendasGenero.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Valor médio por atendimento"))
        item = self.TabelaVendasGenero.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Valor médio por minuto"))
        self.label_5.setText(_translate("MainWindow", "Total previsto de faturamento por gênero de cliente baseado na agenda:"))
