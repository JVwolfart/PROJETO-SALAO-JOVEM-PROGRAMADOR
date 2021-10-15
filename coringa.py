import sqlite3
import sys
from PyQt5 import uic, QtWidgets
import banco
from PyQt5.QtWidgets import QMessageBox
from datetime import date, datetime
from classes import Usuarios

def teste():
    print('Tudo OK')

data_atual = date.today()








if __name__ == '__main__':

    qt = QtWidgets.QApplication(sys.argv)
    
    servico = uic.loadUi('servicos.ui')
    
    
    ##menu2
    servico.BtnInserir.clicked.connect(inserir_servico)
    
    ##############

    #menu.showMaximized()
    servico.show()
    banco.cria_tabelas()
    qt.exec_()