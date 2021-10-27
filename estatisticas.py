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

#FUNÇÕES ESTATÍSTICAS

def carrega_total_dia():
    tabela = estatisitcas.TabelaVendasDia
    row = 0
    nfs = banco.vendas_por_dia()
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 250)
    tabela.setColumnWidth(1, 200)
    tabela.setColumnWidth(2, 200)
    tabela.setColumnWidth(3, 200)
    tabela.setColumnWidth(4, 200)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    total_desc = 0
    for c in nfs:
        total += c[2]
        data = funcoes.banco_data(c[0])
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'Total do dia {data}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'R$ {c[1]:.2f}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'R$ {c[2]:.2f}'))
        percentual = 100-(float(c[2])/float(c[1]))*100
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{percentual:.2f} %'))
        desconto = c[1]-c[2]
        total_desc+=desconto
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {desconto:.2f}'))
        row += 1
        estatisitcas.lbl_total.setText(f'Total do valor faturado líquido: R$ {total:.2f} e total de descontos R$ {total_desc:.2f}')


def carrega_ranking_servicos_total():
    tabela = estatisitcas.TabelaServicos
    row = 0
    nfs = banco.vendas_por_servico_ranking_desc()
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 130)
    tabela.setColumnWidth(1, 70)
    tabela.setColumnWidth(2, 250)
    tabela.setColumnWidth(3, 120)
    tabela.setColumnWidth(4, 140)
    tabela.setColumnWidth(5, 100)
    tabela.setColumnWidth(6, 250)
    tabela.setColumnWidth(7, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[3]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{row+1}° no ranking'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        percentual = 100-(float(c[3])/float(c[2]))*100
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'R$ {c[2]:.2f}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[3]:.2f}'))
        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'{percentual:.2f} %'))
        total_minutos = c[0]*c[4]
        horas = total_minutos // 60
        resto_minutos = total_minutos % 60
        media = float(c[3])/int(c[0])
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{total_minutos}m = {horas} horas e {resto_minutos} minutos'))
        tabela.setItem(row, 7, QtWidgets.QTableWidgetItem(f'R$ {media:.2f}'))
        row += 1
        estatisitcas.lbl_total_servicos.setText(f'Total do valor faturado líquido: R$ {total:.2f}')

def carrega_ranking_clientes_total():
    tabela = estatisitcas.TabelaClientes
    row = 0
    nfs = banco.vendas_por_cliente_ranking_desc()
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 130)
    tabela.setColumnWidth(1, 250)
    tabela.setColumnWidth(2, 150)
    tabela.setColumnWidth(3, 120)
    tabela.setColumnWidth(4, 140)
    tabela.setColumnWidth(5, 150)
    tabela.setColumnWidth(6, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[3]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{row+1}° no ranking'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        percentual = 100-(float(c[3])/float(c[2]))*100
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'R$ {c[2]:.2f}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[3]:.2f}'))
        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'{percentual:.2f} %'))
        if c[4] == 1:
            tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'NÃO'))
        row += 1
        estatisitcas.lbl_total_clientes.setText(f'Total do valor faturado líquido: R$ {total:.2f}')

def carrega_ranking_funcionarios_total():
    tabela = estatisitcas.TabelaProfi
    row = 0
    nfs = banco.vendas_por_funcionario_ranking_desc()
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 130)
    tabela.setColumnWidth(1, 150)
    tabela.setColumnWidth(2, 250)
    tabela.setColumnWidth(3, 180)
    tabela.setColumnWidth(4, 140)
    tabela.setColumnWidth(5, 150)
    tabela.setColumnWidth(6, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[4]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{row+1}° no ranking'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        percentual = 100-(float(c[4])/float(c[3]))*100
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[3]:.2f}'))
        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'R$ {c[4]:.2f}'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{percentual:.2f} %'))
        row += 1
        estatisitcas.lbl_total_profi.setText(f'Total do valor faturado líquido: R$ {total:.2f}')

def carrega_ranking_fpags_total():
    tabela = estatisitcas.TabelaFpag
    row = 0
    nfs = banco.vendas_por_fpag_ranking_desc()
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 130)
    tabela.setColumnWidth(1, 150)
    tabela.setColumnWidth(2, 250)
    tabela.setColumnWidth(3, 180)
    tabela.setColumnWidth(4, 140)
    tabela.setColumnWidth(5, 150)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[3]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{row+1}° no ranking'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        percentual = 100-(float(c[3])/float(c[2]))*100
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'R$ {c[2]:.2f}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[3]:.2f}'))
        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'{percentual:.2f} %'))
        row += 1
        estatisitcas.lbl_total_fpag.setText(f'Total do valor faturado líquido: R$ {total:.2f}')



def carrega_total_dia_intervalo(data_inicial, data_final):
    tabela = estatisitcas.TabelaVendasDia
    row = 0
    nfs = banco.vendas_por_dia_intervalo(data_inicial, data_final)
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 250)
    tabela.setColumnWidth(1, 200)
    tabela.setColumnWidth(2, 200)
    tabela.setColumnWidth(3, 200)
    tabela.setColumnWidth(4, 200)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    total_desc = 0
    for c in nfs:
        total += c[2]
        data = funcoes.banco_data(c[0])
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'Total do dia {data}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'R$ {c[1]:.2f}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'R$ {c[2]:.2f}'))
        percentual = 100-(float(c[2])/float(c[1]))*100
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{percentual:.2f} %'))
        desconto = c[1]-c[2]
        total_desc+=desconto
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {desconto:.2f}'))
        row += 1
        estatisitcas.lbl_total.setText(f'Total do valor faturado líquido: R$ {total:.2f} e total de descontos R$ {total_desc:.2f}')


def carrega_ranking_servicos_total_intervalo(data_inicial, data_final):
    tabela = estatisitcas.TabelaServicos
    row = 0
    nfs = banco.vendas_por_servico_ranking_desc_intervalo(data_inicial, data_final)
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 130)
    tabela.setColumnWidth(1, 70)
    tabela.setColumnWidth(2, 250)
    tabela.setColumnWidth(3, 120)
    tabela.setColumnWidth(4, 140)
    tabela.setColumnWidth(5, 100)
    tabela.setColumnWidth(6, 250)
    tabela.setColumnWidth(7, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[3]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{row+1}° no ranking'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        percentual = 100-(float(c[3])/float(c[2]))*100
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'R$ {c[2]:.2f}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[3]:.2f}'))
        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'{percentual:.2f} %'))
        total_minutos = c[0]*c[4]
        horas = total_minutos // 60
        resto_minutos = total_minutos % 60
        media = float(c[3])/int(c[0])
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{total_minutos}m = {horas} horas e {resto_minutos} minutos'))
        tabela.setItem(row, 7, QtWidgets.QTableWidgetItem(f'R$ {media:.2f}'))
        row += 1
        estatisitcas.lbl_total_servicos.setText(f'Total do valor faturado líquido: R$ {total:.2f}')

def carrega_ranking_clientes_total_intervalo(data_inicial, data_final):
    tabela = estatisitcas.TabelaClientes
    row = 0
    nfs = banco.vendas_por_cliente_ranking_desc_intervalo(data_inicial, data_final)
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 130)
    tabela.setColumnWidth(1, 250)
    tabela.setColumnWidth(2, 150)
    tabela.setColumnWidth(3, 120)
    tabela.setColumnWidth(4, 140)
    tabela.setColumnWidth(5, 150)
    tabela.setColumnWidth(6, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[3]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{row+1}° no ranking'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        percentual = 100-(float(c[3])/float(c[2]))*100
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'R$ {c[2]:.2f}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[3]:.2f}'))
        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'{percentual:.2f} %'))
        if c[4] == 1:
            tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'NÃO'))
        row += 1
        estatisitcas.lbl_total_clientes.setText(f'Total do valor faturado líquido: R$ {total:.2f}')

def carrega_ranking_funcionarios_total_intervalo(data_inicial, data_final):
    tabela = estatisitcas.TabelaProfi
    row = 0
    nfs = banco.vendas_por_funcionario_ranking_desc_intervalo(data_inicial, data_final)
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 130)
    tabela.setColumnWidth(1, 150)
    tabela.setColumnWidth(2, 250)
    tabela.setColumnWidth(3, 180)
    tabela.setColumnWidth(4, 140)
    tabela.setColumnWidth(5, 150)
    tabela.setColumnWidth(6, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[4]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{row+1}° no ranking'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        percentual = 100-(float(c[4])/float(c[3]))*100
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[3]:.2f}'))
        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'R$ {c[4]:.2f}'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{percentual:.2f} %'))
        row += 1
        estatisitcas.lbl_total_profi.setText(f'Total do valor faturado líquido: R$ {total:.2f}')

def carrega_ranking_fpags_total_intervalo(data_inicial, data_final):
    tabela = estatisitcas.TabelaFpag
    row = 0
    nfs = banco.vendas_por_fpag_ranking_desc_intervalo(data_inicial, data_final)
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 130)
    tabela.setColumnWidth(1, 150)
    tabela.setColumnWidth(2, 250)
    tabela.setColumnWidth(3, 180)
    tabela.setColumnWidth(4, 140)
    tabela.setColumnWidth(5, 150)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[3]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{row+1}° no ranking'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        percentual = 100-(float(c[3])/float(c[2]))*100
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'R$ {c[2]:.2f}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[3]:.2f}'))
        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'{percentual:.2f} %'))
        row += 1
        estatisitcas.lbl_total_fpag.setText(f'Total do valor faturado líquido: R$ {total:.2f}')

def carrega_tabelas_estatisticas():
    estatisitcas.lbl_escolha.setText('Todo o período')
    carrega_total_dia()
    carrega_ranking_servicos_total()
    carrega_ranking_clientes_total()
    carrega_ranking_funcionarios_total()
    carrega_ranking_fpags_total()
    estatisitcas.show()


def carrega_tabelas_estatisticas_intervalo(data_inicial, data_final):
    carrega_total_dia_intervalo(data_inicial, data_final)
    carrega_ranking_servicos_total_intervalo(data_inicial, data_final)
    carrega_ranking_clientes_total_intervalo(data_inicial, data_final)
    carrega_ranking_funcionarios_total_intervalo(data_inicial, data_final)
    carrega_ranking_fpags_total_intervalo(data_inicial, data_final)
    estatisitcas.show()


def verificar_intervalo():
    data_inicial = data_estat.DataInicial.text()
    data_final = data_estat.DataFinal.text()
    data_inicial = funcoes.data_banco(data_inicial)
    data_final = funcoes.data_banco(data_final)
    ok = funcoes.inicial_maior_final(data_inicial, data_final)
    if not ok:
        QMessageBox.about(data_estat, 'ERRO', 'Data inválida, a data inicial precisa ser menor ou igual a data final')
    else:
        limpa_rodape_tabela_estatisticas()
        carrega_tabelas_estatisticas_intervalo(data_inicial, data_final)
        estatisitcas.lbl_escolha.setText(f'Data inicial = {data_estat.DataInicial.text()}, data final = {data_estat.DataFinal.text()}')
        data_estat.close()


def limpa_rodape_tabela_estatisticas():
    estatisitcas.lbl_total.setText('')
    estatisitcas.lbl_total_servicos.setText('')
    estatisitcas.lbl_total_clientes.setText('')
    estatisitcas.lbl_total_profi.setText('')
    estatisitcas.lbl_total_fpag.setText('')

if __name__ == '__main__':
    usuario1 = Usuarios
    usuario_banco = banco.buscar_usuario('ADMIN')
    #print(usuario_banco)
    usuario1.banco_para_modelo(usuario1, usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS ESTATISTICAS
    estatisitcas = uic.loadUi('telas_duda/estatisticas.ui')
    data_estat = uic.loadUi('estatisticas_por_intervalo_de_data.ui')
    
    #BOTÕES ESTATÍSTICAS
    estatisitcas.RbIntervaloDatas.clicked.connect(data_estat.show)
    estatisitcas.RbTodas.clicked.connect(carrega_tabelas_estatisticas)
    data_estat.DataInicial.setDate(data_atual)
    data_estat.DataFinal.setDate(data_atual)
    data_estat.BtnConfirmar.clicked.connect(verificar_intervalo)
    ##############
    
    carrega_tabelas_estatisticas()
    banco.cria_tabelas()
    qt.exec_()