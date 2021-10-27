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
    QMessageBox.about(estat_futuro, 'Tudo OK', 'Tudo Ok até aqui, mas falta implementar')

data_atual = date.today()

#FUNÇÕES ESTATÍSTICAS FUTURO AGENDA


def carrega_total_dia_intervalo_futuro(data_inicial, data_final):
    tabela = estat_futuro.TabelaVendasDia
    row = 0
    nfs = banco.previsao_fat_dia(data_inicial, data_final)
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 350)
    tabela.setColumnWidth(1, 200)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[1]
        data = funcoes.banco_data(c[0])
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'Total previsto para o dia {data}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'R$ {c[1]:.2f}'))
        row += 1
        estat_futuro.lbl_total.setText(f'Total do valor previsto bruto: R$ {total:.2f}')


def carrega_servicos_previstos_intervalo_futuro(data_inicial, data_final):
    tabela = estat_futuro.TabelaServicos
    row = 0
    nfs = banco.previsao_fat_servico_futuro(data_inicial, data_final)
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 130)
    tabela.setColumnWidth(1, 70)
    tabela.setColumnWidth(2, 250)
    tabela.setColumnWidth(3, 200)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[2]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{row+1}° no ranking'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'R$ {c[2]:.2f}'))
        row += 1
        estat_futuro.lbl_total_servicos.setText(f'Total do valor previsto bruto: R$ {total:.2f}')

def carrega_clientes_previstos_intervalo_futuro(data_inicial, data_final):
    tabela = estat_futuro.TabelaClientes
    row = 0
    nfs = banco.previsao_fat_cliente_futuro(data_inicial, data_final)
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 150)
    tabela.setColumnWidth(1, 250)
    tabela.setColumnWidth(2, 200)
    tabela.setColumnWidth(3, 150)
    tabela.setColumnWidth(4, 140)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[2]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{row+1}° no ranking'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'R$ {c[2]:.2f}'))
        if c[3] == 1:
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'NÃO'))
        row += 1
        estat_futuro.lbl_total_clientes.setText(f'Total do valor previsto bruto: R$ {total:.2f}')

def carrega_funcionarios_previstos_intervalo_futuro(data_inicial, data_final):
    tabela = estat_futuro.TabelaProfi
    row = 0
    nfs = banco.previsao_fat_profi_futuro(data_inicial, data_final)
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 130)
    tabela.setColumnWidth(1, 150)
    tabela.setColumnWidth(2, 250)
    tabela.setColumnWidth(3, 180)
    tabela.setColumnWidth(4, 140)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[2]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{row+1}° no ranking'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[2]:.2f}'))
        row += 1
        estat_futuro.lbl_total_profi.setText(f'Total do valor previsto bruto: R$ {total:.2f}')

def carrega_lista_negra():
    tabela = estat_futuro.TabelaCancelados
    row = 0
    nfs = banco.lista_negra_cancelamentos()
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 250)
    tabela.setColumnWidth(1, 150)
    tabela.setColumnWidth(2, 250)
    tabela.setColumnWidth(3, 180)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in nfs:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        if c[2] == 1:
            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'NÃO'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        row += 1
        



def verificar_intervalo_futuro():
    global data_atual
    data_inicial = estat_futuro.DataInicial.text()
    data_final = estat_futuro.DataFinal.text()
    data_inicial = funcoes.data_banco(data_inicial)
    data_final = funcoes.data_banco(data_final)
    dia_hoje = datetime.strftime(data_atual, '%Y-%m-%d')
    ok = funcoes.inicial_maior_final(data_inicial, data_final)
    dt_valida = funcoes.valida_data_servico_efetuado(data_inicial, dia_hoje)
    if not dt_valida:
        QMessageBox.about(estat_futuro, 'ERRO', 'Data inválida, a data inicial precisa ser maior ou igual a data atual')
    elif not ok:
        QMessageBox.about(estat_futuro, 'ERRO', 'Data inválida, a data inicial precisa ser menor ou igual a data final')
    else:
        limpa_rodape_tabela_estatisticas_futuro()
        carrega_total_dia_intervalo_futuro(data_inicial, data_final)
        carrega_servicos_previstos_intervalo_futuro(data_inicial, data_final)
        carrega_clientes_previstos_intervalo_futuro(data_inicial, data_final)
        carrega_funcionarios_previstos_intervalo_futuro(data_inicial, data_final)
        carrega_lista_negra()
        
        


def limpa_rodape_tabela_estatisticas_futuro():
    estat_futuro.lbl_total.setText('')
    estat_futuro.lbl_total_servicos.setText('')
    estat_futuro.lbl_total_clientes.setText('')
    estat_futuro.lbl_total_profi.setText('')
    

if __name__ == '__main__':
    usuario1 = Usuarios
    usuario_banco = banco.buscar_usuario('ADMIN')
    #print(usuario_banco)
    usuario1.banco_para_modelo(usuario1, usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS ESTATISTICAS FUTURO AGENDA
    estat_futuro = uic.loadUi('estatisticas_ag_futuro.ui')
    
    
    #BOTÕES ESTATÍSTICAS FUTURO AGENDA
    estat_futuro.DataInicial.setDate(data_atual)
    estat_futuro.DataFinal.setDate(data_atual)
    estat_futuro.BtnCarregar.clicked.connect(verificar_intervalo_futuro)
    ##############
    
    estat_futuro.show()
    banco.cria_tabelas()
    qt.exec_()