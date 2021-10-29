import sqlite3
import sys
from PyQt5 import uic, QtWidgets
import banco
from PyQt5.QtWidgets import QMessageBox
from datetime import date, datetime
from classes import Usuarios
from PyQt5.QtCore import QVariant
import funcoes


def teste():
    print('Tudo OK')

data_atual = date.today()

#FUNÇÕES ESTATÍSTICAS GÊNERO REALIZADO

def carrega_estat_genero():
    tabela = estat_genero.TabelaVendasGenero
    row = 0
    nfs = banco.vendas_realizadas_genero()
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 120)
    tabela.setColumnWidth(1, 150)
    tabela.setColumnWidth(2, 150)
    tabela.setColumnWidth(3, 300)
    tabela.setColumnWidth(4, 200)
    tabela.setColumnWidth(5, 150)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    media_atendimento = 0
    media_minuto = 0
    for c in nfs:
        total += c[1]
        media_atendimento = c[1]/c[2]
        media_minuto = c[1]/c[3]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'R$ {c[1]:.2f}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]} min = {c[3]//60} horas e {c[3]%60} minutos'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {media_atendimento:.2f}'))
        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'R$ {media_minuto:.2f}'))
        row += 1
        estat_genero.lbl_total.setText(f'Total do valor faturado líquido: R$ {total:.2f}')
    estat_genero.show()


def carrega_estat_genero_intervalo(data_inicial, data_final):
    tabela = estat_genero.TabelaVendasGenero
    row = 0
    nfs = banco.vendas_realizadas_genero_intervalo(data_inicial, data_final)
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 120)
    tabela.setColumnWidth(1, 150)
    tabela.setColumnWidth(2, 150)
    tabela.setColumnWidth(3, 300)
    tabela.setColumnWidth(4, 200)
    tabela.setColumnWidth(5, 150)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    media_atendimento = 0
    media_minuto = 0
    for c in nfs:
        total += c[1]
        media_atendimento = c[1]/c[2]
        media_minuto = c[1]/c[3]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'R$ {c[1]:.2f}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]} min = {c[3]//60} horas e {c[3]%60} minutos'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {media_atendimento:.2f}'))
        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'R$ {media_minuto:.2f}'))
        row += 1
        estat_genero.lbl_total.setText(f'Total do valor faturado líquido: R$ {total:.2f}')
    estat_genero.show()





def verificar_intervalo_estat_genero():
    data_inicial = data_estat_genero.DataInicial.text()
    data_final = data_estat_genero.DataFinal.text()
    data_inicial = funcoes.data_banco(data_inicial)
    data_final = funcoes.data_banco(data_final)
    ok = funcoes.inicial_maior_final(data_inicial, data_final)
    if not ok:
        QMessageBox.about(data_estat_genero, 'ERRO', 'Data inválida, a data inicial precisa ser menor ou igual a data final')
    else:
        estat_genero.lbl_total.setText('')
        carrega_estat_genero_intervalo(data_inicial, data_final)
        estat_genero.lbl_escolha.setText(f'Data inicial = {data_estat_genero.DataInicial.text()}, data final = {data_estat_genero.DataFinal.text()}')
        data_estat_genero.close()


    

if __name__ == '__main__':
    usuario1 = Usuarios
    usuario_banco = banco.buscar_usuario('ADMIN')
    #print(usuario_banco)
    usuario1.banco_para_modelo(usuario1, usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS ESTATISTICAS GÊNERO REALIZADO
    estat_genero = uic.loadUi('estatisticas_genero.ui')
    data_estat_genero = uic.loadUi('estatisticas_por_intervalo_de_data.ui')
    
    #BOTÕES ESTATÍSTICAS GÊNERO REALIZADO
    estat_genero.RbTodas.clicked.connect(carrega_estat_genero)
    estat_genero.RbIntervaloDatas.clicked.connect(data_estat_genero.show)
    
    data_estat_genero.DataInicial.setDate(data_atual)
    data_estat_genero.DataFinal.setDate(data_atual)
    data_estat_genero.BtnConfirmar.clicked.connect(verificar_intervalo_estat_genero)
    ##############
    
    carrega_estat_genero()
    banco.cria_tabelas()
    qt.exec_()