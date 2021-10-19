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

#FUNÇÕES DE SERVIÇOS

def inserir_fpag():
    descricao = fpag.InputNome.text().strip().title()
    if descricao == '':
        QMessageBox.about(fpag, 'ERRO', 'Campo não pode ficar vazio')
    else:
        banco.inserir_fpag(descricao)
        QMessageBox.about(fpag, 'FORMA DE PAGAMENTO CADASTRADA', f'Forma de pagamento {descricao} cadastrado com sucesso')
        fpag.InputNome.setText('')
        carrega_fpags()

def carrega_fpags():
    tabela = fpag.TabelaFpag
    f_pag = banco.busca_todos_fpags()
    row = 0
    tabela.setRowCount(len(f_pag))
    tabela.setColumnWidth(0, 100)
    tabela.setColumnWidth(1, 400)
    tabela.setColumnWidth(2, 150)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in f_pag:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        row += 1
      
    fpag.show()


def pega_fpag():
    linha = fpag.TabelaFpag.currentRow()
    id = int(fpag.TabelaFpag.item(linha, 0).text())
    descricao = fpag.TabelaFpag.item(linha, 1).text()
    status = fpag.TabelaFpag.item(linha, 2).text()
    if status == 'Desligado' and usuario1.root == False:
        QMessageBox.about(fpag, 'ERRO', f'Forma de pagamento já está desligada, solicite ao root para reativa-la')
    else:
        manut_fpag.InputId.setValue(id)
        manut_fpag.Nome.setText(descricao)
        manut_fpag.show()

def desligar_fpag():
    codigo = manut_fpag.InputId.value()
    nome = manut_fpag.Nome.text()
    men = QMessageBox.question(manut_fpag, 'DESLIGAR FORMA DE PAGAMENTO', f'ATENÇÃO, deseja realmente desligar a forma de pagamento {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.desligar_fpag(codigo)
        QMessageBox.about(manut_fpag, 'FORMA DE PAGAMENTO DESLIGADO', f'Forma de pagamento {nome} desligada com sucesso')
        carrega_fpags()
        manut_fpag.close()
    else:
        return


def reativar_fpag():
    codigo = manut_fpag.InputId.value()
    nome = manut_fpag.Nome.text()
    men = QMessageBox.question(manut_fpag, 'REATIVAR FORMA DE PAGAMENTO', f'ATENÇÃO, deseja realmente reativar a forma de pagamento {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.reativar_fpag(codigo)
        QMessageBox.about(manut_fpag, 'FORMA DE PAGAMENTO REATIVADO', f'Forma de pagamento {nome} reativada com sucesso')
        carrega_fpags()
        manut_fpag.close()
    else:
        return

def alterar_fpag():
    codigo = manut_fpag.InputId.value()
    nome = manut_fpag.Nome.text().strip().title()
    if nome == '':
        QMessageBox.about(manut_fpag, 'ERRO', 'Campo não pode ficar vazio')
    else:
        banco.alterar_fpag(codigo, nome)
        QMessageBox.about(fpag, 'FORMA DE PAGAMENTO ALTERADO', f'Forma de pagamento {nome} alterada com sucesso')
        manut_fpag.Nome.setText('')
        manut_fpag.close()
        carrega_fpags()

if __name__ == '__main__':
    usuario1 = Usuarios
    usuario_banco = banco.buscar_usuario('JUNIOR')
    #print(usuario_banco)
    usuario1.banco_para_modelo(usuario1, usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS FPAGS
    fpag = uic.loadUi('fpag.ui')
    manut_fpag = uic.loadUi('manut_fpag.ui')
    
    
    #BOTÕES FPAGS
    fpag.BtnInserir.clicked.connect(inserir_fpag)
    fpag.TabelaFpag.doubleClicked.connect(pega_fpag)
    manut_fpag.BtnSair.clicked.connect(manut_fpag.close)
    manut_fpag.BtnDesligar.clicked.connect(desligar_fpag)
    manut_fpag.BtnReativar.clicked.connect(reativar_fpag)
    manut_fpag.BtnAlterar.clicked.connect(alterar_fpag)

    ##############

    #menu.showMaximized()
    carrega_fpags()
    banco.cria_tabelas()
    qt.exec_()