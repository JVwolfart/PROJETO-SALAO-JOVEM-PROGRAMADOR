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


def carrega_total_dia():
    tabela = estatisitcas.TabelaVendasDia
    row = 0
    nfs = banco.vendas_por_dia()
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 250)
    tabela.setColumnWidth(1, 200)
    tabela.setColumnWidth(2, 200)
    tabela.setColumnWidth(3, 200)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[2]
        data = funcoes.banco_data(c[0])
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'Total do dia {data}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'R$ {c[1]:.2f}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'R$ {c[2]:.2f}'))
        percentual = 100-(float(c[2])/float(c[1]))*100
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{percentual:.2f} %'))
        row += 1
        estatisitcas.lbl_total.setText(f'Total do valor faturado líquido: R$ {total:.2f}')


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
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{total_minutos} = {horas} horas e {resto_minutos} minutos'))
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

def carrega_tabelas_estatisticas():
    carrega_total_dia()
    carrega_ranking_servicos_total()
    carrega_ranking_clientes_total()
    carrega_ranking_funcionarios_total()
    carrega_ranking_fpags_total()
    estatisitcas.show()

if __name__ == '__main__':
    usuario1 = Usuarios
    usuario_banco = banco.buscar_usuario('ADMIN')
    #print(usuario_banco)
    usuario1.banco_para_modelo(usuario1, usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS ESTATISTICAS
    estatisitcas = uic.loadUi('estatisticas.ui')
    
    
    #BOTÕES NF
    '''vendas.BtnNVenda.clicked.connect(carrega_combos_nf)
    vendas.TabelaNfs.doubleClicked.connect(pega_nf)
    vendas.TabelaEmitidas.doubleClicked.connect(pega_nf_emitida)
    vendas.TabelaPendentes.doubleClicked.connect(pega_nf_pendente)
    vendas.RbTodas.clicked.connect(rb_todas_nfs)
    vendas.RbCliente.clicked.connect(abrir_consulta_cliente)
    vendas.RbData.clicked.connect(nf_data.show)
    vendas.RbIntervaloDatas.clicked.connect(intervalo_datas.show)
    vendas.RbIntervaloNotas.clicked.connect(intervalo_nf.show)
    nf_cliente.BtnConfirmar.clicked.connect(carrega_todas_nfs_cliente)
    nf_cliente.comboClientes.currentTextChanged.connect(escrever_cliente)
    nf_data.InputData.setDate(data_atual)
    nf_data.BtnConfirmar.clicked.connect(escrever_data)
    intervalo_datas.DataInicial.setDate(data_atual)
    intervalo_datas.DataFinal.setDate(data_atual)
    intervalo_datas.BtnConfirmar.clicked.connect(consulta_intervalo_datas)
    intervalo_nf.BtnConfirmar.clicked.connect(consulta_intervalo_notas)
    nf.vip.setVisible(0)
    nf.frame_vip.setVisible(0)
    nf.comboClientes.currentTextChanged.connect(busca_fiel)
    nf.comboServicos.currentTextChanged.connect(busca_preco)
    nf.VipSlider.valueChanged.connect(calcular_desconto)
    nf.BtnGerarNf.clicked.connect(emitir_nf)
    nf.BtnInserir.clicked.connect(inserir_item_nf)
    nf.BtnCalcularNf.clicked.connect(finalizar_nf)
    nf.TabelaItensNf.doubleClicked.connect(excluir_item_nf)
    manut_nf.BtnInserir.clicked.connect(inserir_item_nf_manut)
    manut_nf.comboServicos.currentTextChanged.connect(busca_preco_manut)
    manut_nf.VipSlider.valueChanged.connect(calcular_desconto_manut)
    manut_nf.TabelaItensNf.doubleClicked.connect(excluir_item_nf_manut)
    manut_nf.BtnSair.clicked.connect(manut_nf.close)
    manut_nf.BtnCancelarNf.clicked.connect(cancelar_nf)
    manut_nf.BtnCalcularNf.clicked.connect(finalizar_nf_manut)'''
    ##############
    
    carrega_tabelas_estatisticas()
    banco.cria_tabelas()
    qt.exec_()