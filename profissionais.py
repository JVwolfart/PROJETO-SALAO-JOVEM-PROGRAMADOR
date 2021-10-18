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
    telefone = profissional.Itelefone.text()
    sexo = profissional.CbSexo.currentText()
    if sexo == 'Selecione um Gênero':
        QMessageBox.about(profissional, 'ERRO', 'Selecione um Gênero')
    else:
        if nome == '' or len(nome)< 5:
            QMessageBox.about(profissional, 'ERRO', 'Campo Nome Não pode ser vazio e precisa pelo menos 5 caracteres')
        elif len(telefone)< 14:
            QMessageBox.about(profissional, 'ERRO', 'Telefone Inválido, pecisa pelo menos 10 digitos')
        else:
            banco.inserir_profissional(nome,telefone,sexo)
            QMessageBox.about(profissional, 'PROFISSIONAL CADASTRADO', f'Profissional {nome} cadastrado com sucesso')
            profissional.Inome.setText('')
            profissional.Itelefone.setText('')
            profissional.CbSexo.setCurrentIndex(0)
            carrega_profissionals()

def carrega_profissionals():
    tabela = profissional.TabelaProfissionals
    profissionals = banco.busca_todos_profissionals_ordem()
    row = 0
    tabela.setRowCount(len(profissionals))
    tabela.setColumnWidth(0, 60)
    tabela.setColumnWidth(1, 350)
    tabela.setColumnWidth(2, 190)
    tabela.setColumnWidth(3, 130)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in profissionals:
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
      


def pega_profissional():
    linha = profissional.TabelaProfissionals.currentRow()
    id = int(profissional.TabelaProfissionals.item(linha, 0).text())
    nome = profissional.TabelaProfissionals.item(linha, 1).text()
    telefone = profissional.TabelaProfissionals.item(linha, 2).text()
    sexo = profissional.TabelaProfissionals.item(linha, 3).text()
    status = profissional.TabelaProfissionals.item(linha, 4).text()
    fidelizado = profissional.TabelaProfissionals.item(linha, 5).text()
    if status == 'Desligado' and usuario1.root == False:
        QMessageBox.about(profissional, 'ERRO', f'Profissional já está desligado, solicite ao root para reativa-lo')
    else:
        manut_profissional.InputId.setValue(id)
        manut_profissional.Nome.setText(nome)
        manut_profissional.Itelefone.setText(telefone)
        if sexo == "Feminino":
            manut_profissional.CbSexo.setCurrentIndex(0)
        elif sexo == "Masculino":
            manut_profissional.CbSexo.setCurrentIndex(1)
        else:
            manut_profissional.CbSexo.setCurrentIndex(2)
        
        if status == 'Desligado':
            manut_profissional.CkAtivo.setChecked(False)
        else:
            manut_profissional.CkAtivo.setChecked(True)
        if fidelizado == 'Não':
            manut_profissional.CkFidelizado.setChecked(False)
        else:
            manut_profissional.CkFidelizado.setChecked(True)
        manut_profissional.show()

def desligar_profissional():
    id = manut_profissional.InputId.value()
    nome = manut_profissional.Nome.text()
    ativo = manut_profissional.CkAtivo.isChecked()
    if not ativo:
        QMessageBox.about(manut_profissional, 'ERRO', f'O Profissional {nome} já está desligado')
    else:
        men = QMessageBox.question(manut_profissional, 'DESLIGAR PROFISSIONAL', f'ATENÇÃO, deseja realmente desligar o profissional {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            banco.desligar_profissional(id)
            QMessageBox.about(manut_profissional, 'PROFISSIONAL DESLIGADO', f'Profissional {nome} desligado com sucesso')
            carrega_profissionals()
            manut_profissional.close()
        else:
            return

def reativar_profissional():
    id = manut_profissional.InputId.value()
    nome = manut_profissional.Nome.text()
    ativo = manut_profissional.CkAtivo.isChecked()
    if ativo:
        QMessageBox.about(manut_profissional, 'ERRO', f'O Profissional {nome} já está ativo')
    else:
        men = QMessageBox.question(manut_profissional, 'REATIVAR PROFISSIONAL', f'ATENÇÃO, deseja realmente reativar o profissional {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            banco.reativar_profissional(id)
            QMessageBox.about(manut_profissional, 'PROFISSIONAL REATIVADO', f'Profissional {nome} reativado com sucesso')
            carrega_profissionals()
            manut_profissional.close()
        else:
            return


def fidelizar_profissional():
    id = manut_profissional.InputId.value()
    nome = manut_profissional.Nome.text()
    fidelizado = manut_profissional.CkFidelizado.isChecked()
    if fidelizado:
        QMessageBox.about(manut_profissional, 'ERRO', f'O Profissional {nome} já é fidelizado')
    else:
        men = QMessageBox.question(manut_profissional, 'FIDELIZAR PROFISSIONAL', f'ATENÇÃO, deseja realmente FIDELIZAR o profissional {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            banco.fidelizar_profissional(id)
            QMessageBox.about(manut_profissional, 'PROFISSIONAL FIDELIZADO', f'O Profissional {nome} foi fidelizado com sucesso e a partir de agora pode receber os descontos de fidelidade')
            carrega_profissionals()
            manut_profissional.close()
        else:
            return

def desfidelizar_profissional():
    id = manut_profissional.InputId.value()
    nome = manut_profissional.Nome.text()
    fidelizado = manut_profissional.CkFidelizado.isChecked()
    if not fidelizado:
        QMessageBox.about(manut_profissional, 'ERRO', f'O Profissional {nome} não é fidelizado')
    else:
        men = QMessageBox.question(manut_profissional, 'DESFIDELIZAR PROFISSIONAL', f'ATENÇÃO, deseja realmente DESFIDELIZAR o profissional {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            banco.desfidelizar_profissional(id)
            QMessageBox.about(manut_profissional, 'PROFISSIONAL DESFIDELIZADO', f'O Profissional {nome} foi desfidelizado e não contará mais com os descontos de fidelidade')
            carrega_profissionals()
            manut_profissional.close()
        else:
            return


def alterar_profissional():
    id = manut_profissional.InputId.value()
    nome = manut_profissional.Nome.text().strip().title()
    telefone = manut_profissional.Itelefone.text()
    sexo = manut_profissional.CbSexo.currentText()
    if sexo == 'Selecione um Gênero':
        QMessageBox.about(manut_profissional, 'ERRO', 'Selecione um Gênero')
    else:
        if nome == '' or len(nome)< 5:
            QMessageBox.about(manut_profissional, 'ERRO', 'Campo Nome Não pode ser vazio e precisa pelo menos 5 caracteres')
        elif len(telefone)< 14:
            QMessageBox.about(manut_profissional, 'ERRO', 'Telefone Inválido, pecisa pelo menos 10 digitos')
        else:
            
            banco.alterar_profissional(id,nome,telefone,sexo)
            QMessageBox.about(manut_profissional, 'PROFISSIONAL EDITADO', f'Profissional {nome} foi alterado com sucesso')
            manut_profissional.Nome.setText('')
            manut_profissional.Itelefone.setText('')
            manut_profissional.CbSexo.setCurrentIndex(0)
            carrega_profissionals()
            manut_profissional.close()


if __name__ == '__main__':
    usuario1 = Usuarios
    usuario_banco = banco.buscar_usuario('JUNIOR')
    #print(usuario_banco)
    usuario1.banco_para_modelo(usuario1, usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS profissionalS
    profissional = uic.loadUi('profissionals.ui')
    manut_profissional = uic.loadUi('manut_profissional.ui')
    
    
    #BOTÕES profissionalS
    profissional.BtnInserir.clicked.connect(inserir_profissional)
    profissional.TabelaProfissionals.doubleClicked.connect(pega_profissional)
    manut_profissional.BtnSair.clicked.connect(manut_profissional.close)
    manut_profissional.BtnDesligar.clicked.connect(desligar_profissional)
    manut_profissional.BtnReativar.clicked.connect(reativar_profissional)
    manut_profissional.BtnFidelizar.clicked.connect(fidelizar_profissional)
    manut_profissional.BtnDesfidelizar.clicked.connect(desfidelizar_profissional)
    manut_profissional.BtnAlterar.clicked.connect(alterar_profissional)

    ##############

    #menu.showMaximized()
    carrega_profissionals()
    banco.cria_tabelas()
    qt.exec_()