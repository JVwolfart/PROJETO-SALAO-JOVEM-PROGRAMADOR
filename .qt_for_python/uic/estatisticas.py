# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jrwolfart/projetos python jv/PROJETO-SAL-O-JOVEM-PROGRAMADOR/telas_duda/estatisticas.ui'
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
        MainWindow.resize(1198, 899)
        MainWindow.setMinimumSize(QtCore.QSize(1198, 899))
        MainWindow.setMaximumSize(QtCore.QSize(1198, 899))
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(215, 139, 185);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_id_user = QtWidgets.QLabel(self.centralwidget)
        self.lbl_id_user.setGeometry(QtCore.QRect(1080, 0, 41, 51))
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
        self.tabWidget.setGeometry(QtCore.QRect(20, 190, 1161, 691))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 231, 249);")
        self.tabWidget.setObjectName("tabWidget")
        self.tabVendas = QtWidgets.QWidget()
        self.tabVendas.setObjectName("tabVendas")
        self.frame_2 = QtWidgets.QFrame(self.tabVendas)
        self.frame_2.setGeometry(QtCore.QRect(10, 560, 1111, 80))
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
        self.TabelaVendasDia = QtWidgets.QTableWidget(self.tabVendas)
        self.TabelaVendasDia.setEnabled(True)
        self.TabelaVendasDia.setGeometry(QtCore.QRect(10, 70, 1111, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabelaVendasDia.sizePolicy().hasHeightForWidth())
        self.TabelaVendasDia.setSizePolicy(sizePolicy)
        self.TabelaVendasDia.setMinimumSize(QtCore.QSize(465, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.TabelaVendasDia.setFont(font)
        self.TabelaVendasDia.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TabelaVendasDia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TabelaVendasDia.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TabelaVendasDia.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TabelaVendasDia.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TabelaVendasDia.setObjectName("TabelaVendasDia")
        self.TabelaVendasDia.setColumnCount(5)
        self.TabelaVendasDia.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaVendasDia.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaVendasDia.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaVendasDia.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaVendasDia.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaVendasDia.setHorizontalHeaderItem(4, item)
        self.TabelaVendasDia.horizontalHeader().setDefaultSectionSize(150)
        self.TabelaVendasDia.horizontalHeader().setSortIndicatorShown(False)
        self.TabelaVendasDia.horizontalHeader().setStretchLastSection(True)
        self.TabelaVendasDia.verticalHeader().setSortIndicatorShown(False)
        self.label_9 = QtWidgets.QLabel(self.tabVendas)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 1021, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tabVendas, "")
        self.tabServicos = QtWidgets.QWidget()
        self.tabServicos.setObjectName("tabServicos")
        self.frame_3 = QtWidgets.QFrame(self.tabServicos)
        self.frame_3.setGeometry(QtCore.QRect(10, 560, 1181, 80))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lbl_total_servicos = QtWidgets.QLabel(self.frame_3)
        self.lbl_total_servicos.setGeometry(QtCore.QRect(20, 20, 1061, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_total_servicos.setFont(font)
        self.lbl_total_servicos.setStyleSheet("color: rgb(115, 210, 22);")
        self.lbl_total_servicos.setText("")
        self.lbl_total_servicos.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_total_servicos.setObjectName("lbl_total_servicos")
        self.label_4 = QtWidgets.QLabel(self.tabServicos)
        self.label_4.setGeometry(QtCore.QRect(40, 0, 1021, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.TabelaServicos = QtWidgets.QTableWidget(self.tabServicos)
        self.TabelaServicos.setEnabled(True)
        self.TabelaServicos.setGeometry(QtCore.QRect(10, 70, 1181, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabelaServicos.sizePolicy().hasHeightForWidth())
        self.TabelaServicos.setSizePolicy(sizePolicy)
        self.TabelaServicos.setMinimumSize(QtCore.QSize(465, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.TabelaServicos.setFont(font)
        self.TabelaServicos.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TabelaServicos.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.TabelaServicos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TabelaServicos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TabelaServicos.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TabelaServicos.setObjectName("TabelaServicos")
        self.TabelaServicos.setColumnCount(8)
        self.TabelaServicos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaServicos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaServicos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaServicos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaServicos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaServicos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaServicos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaServicos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaServicos.setHorizontalHeaderItem(7, item)
        self.TabelaServicos.horizontalHeader().setDefaultSectionSize(150)
        self.TabelaServicos.horizontalHeader().setSortIndicatorShown(False)
        self.TabelaServicos.horizontalHeader().setStretchLastSection(True)
        self.TabelaServicos.verticalHeader().setSortIndicatorShown(False)
        self.tabWidget.addTab(self.tabServicos, "")
        self.tabClientes = QtWidgets.QWidget()
        self.tabClientes.setObjectName("tabClientes")
        self.frame_4 = QtWidgets.QFrame(self.tabClientes)
        self.frame_4.setGeometry(QtCore.QRect(20, 560, 1111, 80))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lbl_total_clientes = QtWidgets.QLabel(self.frame_4)
        self.lbl_total_clientes.setGeometry(QtCore.QRect(20, 20, 1061, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_total_clientes.setFont(font)
        self.lbl_total_clientes.setStyleSheet("color: rgb(115, 210, 22);")
        self.lbl_total_clientes.setText("")
        self.lbl_total_clientes.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_total_clientes.setObjectName("lbl_total_clientes")
        self.TabelaClientes = QtWidgets.QTableWidget(self.tabClientes)
        self.TabelaClientes.setEnabled(True)
        self.TabelaClientes.setGeometry(QtCore.QRect(20, 70, 1101, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabelaClientes.sizePolicy().hasHeightForWidth())
        self.TabelaClientes.setSizePolicy(sizePolicy)
        self.TabelaClientes.setMinimumSize(QtCore.QSize(465, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.TabelaClientes.setFont(font)
        self.TabelaClientes.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TabelaClientes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TabelaClientes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TabelaClientes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TabelaClientes.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TabelaClientes.setObjectName("TabelaClientes")
        self.TabelaClientes.setColumnCount(7)
        self.TabelaClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
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
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaClientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaClientes.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaClientes.setHorizontalHeaderItem(6, item)
        self.TabelaClientes.horizontalHeader().setDefaultSectionSize(150)
        self.TabelaClientes.horizontalHeader().setSortIndicatorShown(False)
        self.TabelaClientes.horizontalHeader().setStretchLastSection(True)
        self.TabelaClientes.verticalHeader().setSortIndicatorShown(False)
        self.label_6 = QtWidgets.QLabel(self.tabClientes)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 1021, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tabClientes, "")
        self.tabProfissionais = QtWidgets.QWidget()
        self.tabProfissionais.setObjectName("tabProfissionais")
        self.frame_5 = QtWidgets.QFrame(self.tabProfissionais)
        self.frame_5.setGeometry(QtCore.QRect(10, 560, 1111, 80))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.lbl_total_profi = QtWidgets.QLabel(self.frame_5)
        self.lbl_total_profi.setGeometry(QtCore.QRect(20, 20, 1061, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_total_profi.setFont(font)
        self.lbl_total_profi.setStyleSheet("color: rgb(115, 210, 22);")
        self.lbl_total_profi.setText("")
        self.lbl_total_profi.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_total_profi.setObjectName("lbl_total_profi")
        self.TabelaProfi = QtWidgets.QTableWidget(self.tabProfissionais)
        self.TabelaProfi.setEnabled(True)
        self.TabelaProfi.setGeometry(QtCore.QRect(10, 70, 1111, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabelaProfi.sizePolicy().hasHeightForWidth())
        self.TabelaProfi.setSizePolicy(sizePolicy)
        self.TabelaProfi.setMinimumSize(QtCore.QSize(465, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.TabelaProfi.setFont(font)
        self.TabelaProfi.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TabelaProfi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TabelaProfi.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TabelaProfi.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TabelaProfi.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TabelaProfi.setObjectName("TabelaProfi")
        self.TabelaProfi.setColumnCount(7)
        self.TabelaProfi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaProfi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaProfi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaProfi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaProfi.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaProfi.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaProfi.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaProfi.setHorizontalHeaderItem(6, item)
        self.TabelaProfi.horizontalHeader().setDefaultSectionSize(150)
        self.TabelaProfi.horizontalHeader().setSortIndicatorShown(False)
        self.TabelaProfi.horizontalHeader().setStretchLastSection(True)
        self.TabelaProfi.verticalHeader().setSortIndicatorShown(False)
        self.label_7 = QtWidgets.QLabel(self.tabProfissionais)
        self.label_7.setGeometry(QtCore.QRect(60, 10, 1021, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tabProfissionais, "")
        self.tabFpag = QtWidgets.QWidget()
        self.tabFpag.setObjectName("tabFpag")
        self.frame_6 = QtWidgets.QFrame(self.tabFpag)
        self.frame_6.setGeometry(QtCore.QRect(10, 560, 1111, 80))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.lbl_total_fpag = QtWidgets.QLabel(self.frame_6)
        self.lbl_total_fpag.setGeometry(QtCore.QRect(20, 20, 1061, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_total_fpag.setFont(font)
        self.lbl_total_fpag.setStyleSheet("color: rgb(115, 210, 22);")
        self.lbl_total_fpag.setText("")
        self.lbl_total_fpag.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_total_fpag.setObjectName("lbl_total_fpag")
        self.TabelaFpag = QtWidgets.QTableWidget(self.tabFpag)
        self.TabelaFpag.setEnabled(True)
        self.TabelaFpag.setGeometry(QtCore.QRect(10, 70, 1111, 471))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabelaFpag.sizePolicy().hasHeightForWidth())
        self.TabelaFpag.setSizePolicy(sizePolicy)
        self.TabelaFpag.setMinimumSize(QtCore.QSize(465, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.TabelaFpag.setFont(font)
        self.TabelaFpag.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TabelaFpag.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TabelaFpag.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TabelaFpag.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TabelaFpag.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TabelaFpag.setObjectName("TabelaFpag")
        self.TabelaFpag.setColumnCount(6)
        self.TabelaFpag.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaFpag.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaFpag.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaFpag.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaFpag.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaFpag.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaFpag.setHorizontalHeaderItem(5, item)
        self.TabelaFpag.horizontalHeader().setDefaultSectionSize(150)
        self.TabelaFpag.horizontalHeader().setSortIndicatorShown(False)
        self.TabelaFpag.horizontalHeader().setStretchLastSection(True)
        self.TabelaFpag.verticalHeader().setSortIndicatorShown(False)
        self.label_8 = QtWidgets.QLabel(self.tabFpag)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 1021, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tabFpag, "")
        self.RbTodas = QtWidgets.QRadioButton(self.centralwidget)
        self.RbTodas.setGeometry(QtCore.QRect(840, 130, 151, 28))
        self.RbTodas.setChecked(True)
        self.RbTodas.setObjectName("RbTodas")
        self.lbl_escolha = QtWidgets.QLabel(self.centralwidget)
        self.lbl_escolha.setGeometry(QtCore.QRect(20, 120, 791, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lbl_escolha.setFont(font)
        self.lbl_escolha.setText("")
        self.lbl_escolha.setObjectName("lbl_escolha")
        self.RbIntervaloDatas = QtWidgets.QRadioButton(self.centralwidget)
        self.RbIntervaloDatas.setGeometry(QtCore.QRect(1010, 130, 171, 28))
        self.RbIntervaloDatas.setObjectName("RbIntervaloDatas")
        self.lbl_status_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_status_2.setGeometry(QtCore.QRect(190, 30, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_status_2.setFont(font)
        self.lbl_status_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status_2.setObjectName("lbl_status_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Estatísticas do negócio"))
        self.TabelaVendasDia.setSortingEnabled(False)
        item = self.TabelaVendasDia.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data da venda"))
        item = self.TabelaVendasDia.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Total bruto"))
        item = self.TabelaVendasDia.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Total faturado com descontos"))
        item = self.TabelaVendasDia.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Percentual médio de desconto"))
        item = self.TabelaVendasDia.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total de descontos no dia"))
        self.label_9.setText(_translate("MainWindow", "Total faturado por dia (ordem de data decrescente)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVendas), _translate("MainWindow", "Total de vendas"))
        self.label_4.setText(_translate("MainWindow", "Ranking de serviços por valor faturado"))
        self.TabelaServicos.setSortingEnabled(False)
        item = self.TabelaServicos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Posição no ranking"))
        item = self.TabelaServicos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quant"))
        item = self.TabelaServicos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Serviço"))
        item = self.TabelaServicos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total bruto"))
        item = self.TabelaServicos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total com desconto"))
        item = self.TabelaServicos.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Média desc %"))
        item = self.TabelaServicos.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Total aprox de minutos em atendimento"))
        item = self.TabelaServicos.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Média de valor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabServicos), _translate("MainWindow", "Ranking por serviço"))
        self.TabelaClientes.setSortingEnabled(False)
        item = self.TabelaClientes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Posição no ranking"))
        item = self.TabelaClientes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome do cliente"))
        item = self.TabelaClientes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quant serviços usados"))
        item = self.TabelaClientes.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total bruto"))
        item = self.TabelaClientes.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total com desconto"))
        item = self.TabelaClientes.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "% de desc (médio)"))
        item = self.TabelaClientes.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Fidelizado"))
        self.label_6.setText(_translate("MainWindow", "Ranking de clientes por valor faturado"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabClientes), _translate("MainWindow", "Ranking por cliente"))
        self.TabelaProfi.setSortingEnabled(False)
        item = self.TabelaProfi.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Posição no ranking"))
        item = self.TabelaProfi.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "N° de atendimentos"))
        item = self.TabelaProfi.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nome do profissional"))
        item = self.TabelaProfi.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Especialidade"))
        item = self.TabelaProfi.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total bruto"))
        item = self.TabelaProfi.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Total com desconto"))
        item = self.TabelaProfi.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "% desc (médio)"))
        self.label_7.setText(_translate("MainWindow", "Ranking de profissionais por valor faturado"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProfissionais), _translate("MainWindow", "Ranking por profissionais"))
        self.TabelaFpag.setSortingEnabled(False)
        item = self.TabelaFpag.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Posição no ranking"))
        item = self.TabelaFpag.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "N° de utilizações"))
        item = self.TabelaFpag.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Forma de pagamento"))
        item = self.TabelaFpag.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total bruto"))
        item = self.TabelaFpag.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total com desconto"))
        item = self.TabelaFpag.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "% desc (médio)"))
        self.label_8.setText(_translate("MainWindow", "Ranking de formas de pagamento por valor faturado"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFpag), _translate("MainWindow", "Ranking por formas de pagamento"))
        self.RbTodas.setText(_translate("MainWindow", "Todo o período"))
        self.RbIntervaloDatas.setText(_translate("MainWindow", "Intervalo de datas"))
        self.lbl_status_2.setText(_translate("MainWindow", "Estatísticas"))
