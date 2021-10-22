import sqlite3
import sys
from PyQt5 import uic,QtWidgets





if __name__ == '__main__':

    qt = QtWidgets.QApplication(sys.argv)
    menu = uic.loadUi('telas_duda/tela_login.ui')

    menu.show()
    qt.exec_()