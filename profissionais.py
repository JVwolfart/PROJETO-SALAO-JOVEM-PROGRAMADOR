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

#FUNÇÕES DE profissionais

def inserir_profissional():
    nome = profissional.Inome.text().strip().title()
    matricula = profissional.Imatricula.text().strip()
    cargo = profissional.Ifuncao.text().strip().title()
    func_banco = banco.busca_func_matricula(matricula)
    if nome == '' or len(nome)< 5:
        QMessageBox.about(profissional, 'ERRO', 'Campo Nome Não pode ser vazio e precisa pelo menos 5 caracteres')
    elif matricula == '' or cargo == '':
        QMessageBox.about(profissional, 'ERRO', 'Nenhum campo deve ficar vazio')
    elif len(func_banco) != 0:
        QMessageBox.about(profissional, 'ERRO', 'Já existe profissional com essa Matricula cadastrada')
    else:
        banco.inserir_funcionario(nome,cargo,matricula)
        QMessageBox.about(profissional, 'PROFISSIONAL CADASTRADO', f'Profissional {nome} cadastrado com sucesso')
        profissional.Inome.setText('')
        profissional.Ifuncao.setText('')
        profissional.Imatricula.setText('')
        carrega_profissionais()

def carrega_profissionais():
    tabela = profissional.TabelaProfissionais
    profissionais = banco.busca_todos_funcionarios_ordem()
    row = 0
    tabela.setRowCount(len(profissionais))
    tabela.setColumnWidth(0, 60)
    tabela.setColumnWidth(1, 350)
    tabela.setColumnWidth(2, 250)
    tabela.setColumnWidth(3, 130)
    tabela.setColumnWidth(4, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in profissionais:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{c[4]}'))
        row += 1
      


def pega_profissional():
    linha = profissional.TabelaProfissionais.currentRow()
    id = int(profissional.TabelaProfissionais.item(linha, 0).text())
    nome = profissional.TabelaProfissionais.item(linha, 1).text()
    cargo = profissional.TabelaProfissionais.item(linha, 2).text()
    matricula = profissional.TabelaProfissionais.item(linha, 3).text()
    status = profissional.TabelaProfissionais.item(linha, 4).text()
    if status == 'Desligado' and usuario1.root == False:
        QMessageBox.about(profissional, 'ERRO', f'Profissional já está desligado, solicite ao root para reativa-lo')
    else:
        manut_profissional.InputId.setValue(id)
        manut_profissional.Inome.setText(nome)
        manut_profissional.Ifuncao.setText(cargo)
        manut_profissional.Imatricula.setText(matricula)
        manut_profissional.show()

def desligar_profissional():
    id = manut_profissional.InputId.value()
    nome = manut_profissional.Inome.text()
    men = QMessageBox.question(manut_profissional, 'DESLIGAR PROFISSIONAL', f'ATENÇÃO, deseja realmente desligar o profissional {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.desligar_funcionario(id)
        QMessageBox.about(manut_profissional, 'PROFISSIONAL DESLIGADO', f'Profissional {nome} desligado com sucesso')
        carrega_profissionais()
        manut_profissional.close()
    else:
        return

def reativar_profissional():
    id = manut_profissional.InputId.value()
    nome = manut_profissional.Inome.text()
    men = QMessageBox.question(manut_profissional, 'REATIVAR PROFISSIONAL', f'ATENÇÃO, deseja realmente reativar o profissional {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.reativar_funcionario(id)
        QMessageBox.about(manut_profissional, 'PROFISSIONAL REATIVADO', f'Profissional {nome} reativado com sucesso')
        carrega_profissionais()
        manut_profissional.close()
    else:
        return


def alterar_profissional():
    id = manut_profissional.InputId.value()
    nome = manut_profissional.Inome.text().strip().title()
    cargo = manut_profissional.Ifuncao.text().strip().title()
    if nome == '' or len(nome)< 5:
        QMessageBox.about(manut_profissional, 'ERRO', 'Campo Nome Não pode ser vazio e precisa pelo menos 5 caracteres')
    elif cargo == '':
        QMessageBox.about(manut_profissional, 'ERRO', 'Cargo Inválido não pode ser vazio')
    else:    
        banco.alterar_funcionario(id,nome,cargo)
        QMessageBox.about(manut_profissional, 'PROFISSIONAL EDITADO', f'Profissional {nome} foi alterado com sucesso')
        manut_profissional.Inome.setText('')
        manut_profissional.Ifuncao.setText('')
        carrega_profissionais()
        manut_profissional.close()


if __name__ == '__main__':
    usuario1 = Usuarios
    usuario_banco = banco.buscar_usuario('JUNIOR')
    #print(usuario_banco)
    usuario1.banco_para_modelo(usuario1, usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS profissionais
    profissional = uic.loadUi('profissionais.ui')
    manut_profissional = uic.loadUi('manut_profissional.ui')
    
    
    #BOTÕES profissionais
    profissional.BtnInserir.clicked.connect(inserir_profissional)
    profissional.TabelaProfissionais.doubleClicked.connect(pega_profissional)
    manut_profissional.BtnSair.clicked.connect(manut_profissional.close)
    manut_profissional.BtnDesligar.clicked.connect(desligar_profissional)
    manut_profissional.BtnReativar.clicked.connect(reativar_profissional)
    manut_profissional.BtnAlterar.clicked.connect(alterar_profissional)

    ##############

    #menu.showMaximized()
    carrega_profissionais()
    profissional.show()
    banco.cria_tabelas()
    qt.exec_()