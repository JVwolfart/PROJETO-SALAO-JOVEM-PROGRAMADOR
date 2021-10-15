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

def inserir_servico():
    descricao = servico.InputNome.text().strip().title()
    valor = servico.InputValor.value()
    tempo = servico.InputTempo.value()
    if descricao == '' or valor == 0 or tempo == 0:
        QMessageBox.about(servico, 'ERRO', 'Nenhum campo pode ficar vazio')
    else:
        banco.inserir_servico(descricao, valor, tempo)
        QMessageBox.about(servico, 'SERVIÇO CADASTRADO', f'Serviço {descricao} cadastrado com sucesso')
        servico.InputNome.setText('')
        servico.InputValor.setValue(0)
        servico.InputTempo.setValue(0)
        carrega_servicos()

def carrega_servicos():
    tabela = servico.TabelaServicos
    servicos = banco.busca_todos_servicos()
    row = 0
    tabela.setRowCount(len(servicos))
    tabela.setColumnWidth(0, 30)
    tabela.setColumnWidth(1, 400)
    tabela.setColumnWidth(2, 150)
    tabela.setColumnWidth(3, 150)
    tabela.setColumnWidth(4, 200)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in servicos:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'R$ {c[2]:.2f}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{c[4]}'))
        row += 1
      
    servico.show()


def pega_servico():
    linha = servico.TabelaServicos.currentRow()
    codigo = int(servico.TabelaServicos.item(linha, 0).text())
    descricao = servico.TabelaServicos.item(linha, 1).text()
    valor = servico.TabelaServicos.item(linha, 2).text()
    valor = valor.replace('R$ ', '')
    valor = float(valor)
    tempo = int(servico.TabelaServicos.item(linha, 3).text())
    status = servico.TabelaServicos.item(linha, 4).text()
    if status == 'Desligado' and usuario1.root == False:
        QMessageBox.about(servico, 'ERRO', f'Serviço já está desligado, solicite ao root para reativa-lo')
    else:
        manut_servico.InputId.setValue(codigo)
        manut_servico.Nome.setText(descricao)
        manut_servico.Valor.setValue(valor)
        manut_servico.Tempo.setValue(tempo)
        manut_servico.show()

def desligar_servico():
    codigo = manut_servico.InputId.value()
    nome = manut_servico.Nome.text()
    men = QMessageBox.question(manut_servico, 'DESLIGAR SERVIÇO', f'ATENÇÃO, deseja realmente desligar o serviço {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.desligar_servico(codigo)
        QMessageBox.about(manut_servico, 'SERVIÇO DESLIGADO', f'Serviço {nome} desligado com sucesso')
        carrega_servicos()
        manut_servico.close()
    else:
        return


def reativar_servico():
    codigo = manut_servico.InputId.value()
    nome = manut_servico.Nome.text()
    men = QMessageBox.question(manut_servico, 'REATIVAR SERVIÇO', f'ATENÇÃO, deseja realmente reativar o serviço {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.reativar_servico(codigo)
        QMessageBox.about(manut_servico, 'SERVIÇO REATIVADO', f'Serviço {nome} reativado com sucesso')
        carrega_servicos()
        manut_servico.close()
    else:
        return

def alterar_servico():
    codigo = manut_servico.InputId.value()
    nome = manut_servico.Nome.text().strip().title()
    tempo = manut_servico.Tempo.value()
    valor = manut_servico.Valor.value()
    if nome == '' or valor == 0 or tempo == 0:
        QMessageBox.about(manut_servico, 'ERRO', 'Nenhum campo pode ficar vazio')
    else:
        banco.alterar_servico(codigo, nome, valor, tempo)
        QMessageBox.about(servico, 'SERVIÇO ALTERADO', f'Serviço {nome} alterado com sucesso')
        manut_servico.Nome.setText('')
        manut_servico.Valor.setValue(0)
        manut_servico.Tempo.setValue(0)
        manut_servico.close()
        carrega_servicos()

if __name__ == '__main__':
    usuario1 = Usuarios
    usuario_banco = banco.buscar_usuario('ADMIN')
    #print(usuario_banco)
    usuario1.banco_para_modelo(usuario1, usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS SERVIÇOS
    servico = uic.loadUi('servicos.ui')
    manut_servico = uic.loadUi('manut_servico.ui')
    
    
    #BOTÕES SERVIÇOS
    servico.BtnInserir.clicked.connect(inserir_servico)
    servico.TabelaServicos.doubleClicked.connect(pega_servico)
    manut_servico.BtnSair.clicked.connect(manut_servico.close)
    manut_servico.BtnDesligar.clicked.connect(desligar_servico)
    manut_servico.BtnReativar.clicked.connect(reativar_servico)
    manut_servico.BtnAlterar.clicked.connect(alterar_servico)

    ##############

    #menu.showMaximized()
    carrega_servicos()
    banco.cria_tabelas()
    qt.exec_()