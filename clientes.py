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

#FUNÇÕES DE clienteS

def inserir_cliente():
    nome = cliente.Inome.text().strip().title()
    telefone = cliente.Itelefone.text()
    sexo = cliente.CbSexo.currentText()
    if sexo == 'Selecione um Gênero':
        QMessageBox.about(cliente, 'ERRO', 'Selecione um Gênero')
    else:
        if nome == '' or len(nome)< 5:
            QMessageBox.about(cliente, 'ERRO', 'Campo Nome Não pode ser vazio e precisa pelo menos 5 caracteres')
        elif len(telefone)< 14:
            QMessageBox.about(cliente, 'ERRO', 'Telefone Inválido, pecisa pelo menos 10 digitos')
        else:
            banco.inserir_cliente(nome,telefone,sexo)
            QMessageBox.about(cliente, 'CLIENTE CADASTRADO', f'Cliente {nome} cadastrado com sucesso')
            cliente.Inome.setText('')
            cliente.Itelefone.setText('')
            cliente.CbSexo.setCurrentIndex(0)
            carrega_clientes()

def carrega_clientes():
    tabela = cliente.TabelaClientes
    clientes = banco.busca_todos_clientes_ordem()
    row = 0
    tabela.setRowCount(len(clientes))
    tabela.setColumnWidth(0, 60)
    tabela.setColumnWidth(1, 350)
    tabela.setColumnWidth(2, 190)
    tabela.setColumnWidth(3, 130)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in clientes:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{c[4]}'))
        if c[5] == 0:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'Não'))
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'Sim'))
        row += 1
      


def pega_cliente():
    linha = cliente.TabelaClientes.currentRow()
    id = int(cliente.TabelaClientes.item(linha, 0).text())
    nome = cliente.TabelaClientes.item(linha, 1).text()
    telefone = cliente.TabelaClientes.item(linha, 2).text()
    sexo = cliente.TabelaClientes.item(linha, 3).text()
    status = cliente.TabelaClientes.item(linha, 4).text()
    fidelizado = cliente.TabelaClientes.item(linha, 5).text()
    if status == 'Desligado' and usuario1.root == False:
        QMessageBox.about(cliente, 'ERRO', f'Cliente já está desligado, solicite ao root para reativa-lo')
    else:
        manut_cliente.InputId.setValue(id)
        manut_cliente.Nome.setText(nome)
        manut_cliente.Itelefone.setText(telefone)
        if sexo == "Feminino":
            manut_cliente.CbSexo.setCurrentIndex(0)
        elif sexo == "Masculino":
            manut_cliente.CbSexo.setCurrentIndex(1)
        else:
            manut_cliente.CbSexo.setCurrentIndex(2)
        
        if status == 'Desligado':
            manut_cliente.CkAtivo.setChecked(False)
        else:
            manut_cliente.CkAtivo.setChecked(True)
        if fidelizado == 'Não':
            manut_cliente.CkFidelizado.setChecked(False)
        else:
            manut_cliente.CkFidelizado.setChecked(True)
        manut_cliente.show()

def desligar_cliente():
    id = manut_cliente.InputId.value()
    nome = manut_cliente.Nome.text()
    ativo = manut_cliente.CkAtivo.isChecked()
    if not ativo:
        QMessageBox.about(manut_cliente, 'ERRO', f'O Cliente {nome} já está desligado')
    else:
        men = QMessageBox.question(manut_cliente, 'DESLIGAR CLIENTE', f'ATENÇÃO, deseja realmente desligar o cliente {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            banco.desligar_cliente(id)
            QMessageBox.about(manut_cliente, 'CLIENTE DESLIGADO', f'Cliente {nome} desligado com sucesso')
            carrega_clientes()
            manut_cliente.close()
        else:
            return

def reativar_cliente():
    id = manut_cliente.InputId.value()
    nome = manut_cliente.Nome.text()
    ativo = manut_cliente.CkAtivo.isChecked()
    if ativo:
        QMessageBox.about(manut_cliente, 'ERRO', f'O Cliente {nome} já está ativo')
    else:
        men = QMessageBox.question(manut_cliente, 'REATIVAR CLIENTE', f'ATENÇÃO, deseja realmente reativar o cliente {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            banco.reativar_cliente(id)
            QMessageBox.about(manut_cliente, 'CLIENTE REATIVADO', f'Cliente {nome} reativado com sucesso')
            carrega_clientes()
            manut_cliente.close()
        else:
            return


def fidelizar_cliente():
    id = manut_cliente.InputId.value()
    nome = manut_cliente.Nome.text()
    fidelizado = manut_cliente.CkFidelizado.isChecked()
    if fidelizado:
        QMessageBox.about(manut_cliente, 'ERRO', f'O Cliente {nome} já é fidelizado')
    else:
        men = QMessageBox.question(manut_cliente, 'FIDELIZAR CLIENTE', f'ATENÇÃO, deseja realmente FIDELIZAR o cliente {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            banco.fidelizar_cliente(id)
            QMessageBox.about(manut_cliente, 'CLIENTE FIDELIZADO', f'O Cliente {nome} foi fidelizado com sucesso e a partir de agora pode receber os descontos de fidelidade')
            carrega_clientes()
            manut_cliente.close()
        else:
            return

def desfidelizar_cliente():
    id = manut_cliente.InputId.value()
    nome = manut_cliente.Nome.text()
    fidelizado = manut_cliente.CkFidelizado.isChecked()
    if not fidelizado:
        QMessageBox.about(manut_cliente, 'ERRO', f'O Cliente {nome} não é fidelizado')
    else:
        men = QMessageBox.question(manut_cliente, 'DESFIDELIZAR CLIENTE', f'ATENÇÃO, deseja realmente DESFIDELIZAR o cliente {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            banco.desfidelizar_cliente(id)
            QMessageBox.about(manut_cliente, 'CLIENTE DESFIDELIZADO', f'O Cliente {nome} foi desfidelizado e não contará mais com os descontos de fidelidade')
            carrega_clientes()
            manut_cliente.close()
        else:
            return


def alterar_cliente():
    id = manut_cliente.InputId.value()
    nome = manut_cliente.Nome.text().strip().title()
    telefone = manut_cliente.Itelefone.text()
    sexo = manut_cliente.CbSexo.currentText()
    if sexo == 'Selecione um Gênero':
        QMessageBox.about(manut_cliente, 'ERRO', 'Selecione um Gênero')
    else:
        if nome == '' or len(nome)< 5:
            QMessageBox.about(manut_cliente, 'ERRO', 'Campo Nome Não pode ser vazio e precisa pelo menos 5 caracteres')
        elif len(telefone)< 14:
            QMessageBox.about(manut_cliente, 'ERRO', 'Telefone Inválido, pecisa pelo menos 10 digitos')
        else:
            
            banco.alterar_cliente(id,nome,telefone,sexo)
            QMessageBox.about(manut_cliente, 'CLIENTE EDITADO', f'Cliente {nome} foi alterado com sucesso')
            manut_cliente.Nome.setText('')
            manut_cliente.Itelefone.setText('')
            manut_cliente.CbSexo.setCurrentIndex(0)
            carrega_clientes()
            manut_cliente.close()


if __name__ == '__main__':
    usuario1 = Usuarios
    usuario_banco = banco.buscar_usuario('JUNIOR')
    #print(usuario_banco)
    usuario1.banco_para_modelo(usuario1, usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS clienteS
    cliente = uic.loadUi('clientes.ui')
    manut_cliente = uic.loadUi('manut_cliente.ui')
    
    
    #BOTÕES clienteS
    cliente.BtnInserir.clicked.connect(inserir_cliente)
    cliente.TabelaClientes.doubleClicked.connect(pega_cliente)
    manut_cliente.BtnSair.clicked.connect(manut_cliente.close)
    manut_cliente.BtnDesligar.clicked.connect(desligar_cliente)
    manut_cliente.BtnReativar.clicked.connect(reativar_cliente)
    manut_cliente.BtnFidelizar.clicked.connect(fidelizar_cliente)
    manut_cliente.BtnDesfidelizar.clicked.connect(desfidelizar_cliente)
    manut_cliente.BtnAlterar.clicked.connect(alterar_cliente)

    ##############

    #menu.showMaximized()
    carrega_clientes()
    banco.cria_tabelas()
    qt.exec_()