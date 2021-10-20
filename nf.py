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

def busca_fiel():
    id = nf.comboClientes.currentData()
    if id != None:
        fidelidade = banco.busca_fidelidade_cliente(id)
        #print(fidelidade)
        nf.vip.setVisible(fidelidade[0])
        nf.frame_vip.setVisible(fidelidade[0])
        nf.VipSlider.setValue(0)
        calcular_desconto()
    else:
        nf.vip.setVisible(0)
        nf.frame_vip.setVisible(0)
        
    
    #print('buscar fieis', id)
    
def busca_preco():
    id = nf.comboServicos.currentData()
    preco_servico = banco.buscar_preco_id(id)
    preco = float(preco_servico[0][0])
    nf.InputPtab.setValue(preco)
    nf.InputPfat.setValue(preco)
    calcular_desconto()    

def busca_preco_manut():
    id = manut_nf.comboServicos.currentData()
    preco_servico = banco.buscar_preco_id(id)
    preco = float(preco_servico[0][0])
    manut_nf.InputPtab.setValue(preco)
    manut_nf.InputPfat.setValue(preco)
    calcular_desconto_manut()    

def cliente_nf_combo():
    nf.comboClientes.clear()
    clientes = banco.busca_todos_clientes_combo_ativos()
    for c in clientes:
        nf.comboClientes.addItem(f"{c[1]}", QVariant(c[0]))
    nf.show()

def servico_nf_combo():
    nf.comboServicos.clear()
    servicos = banco.busca_todos_servicos_ativos()
    for c in servicos:
        nf.comboServicos.addItem(f"{c[1]}", QVariant(c[0]))
    nf.show()


def profi_nf_combo():
    nf.comboProfi.clear()
    profi = banco.busca_todos_funcionarios_combo_ativos()
    for c in profi:
        nf.comboProfi.addItem(f"{c[1]} -> {c[2]}", QVariant(c[0]))
    nf.show()

def fpag_nf_combo():
    nf.comboFpag.clear()
    fpags = banco.busca_todos_fpags_ativas()
    for c in fpags:
        nf.comboFpag.addItem(f"{c[1]}", QVariant(c[0]))
    nf.show()


def servico_nf_combo_manut():
    manut_nf.comboServicos.clear()
    servicos = banco.busca_todos_servicos_ativos()
    for c in servicos:
        manut_nf.comboServicos.addItem(f"{c[1]}", QVariant(c[0]))


def profi_nf_combo_manut():
    manut_nf.comboProfi.clear()
    profi = banco.busca_todos_funcionarios_combo_ativos()
    for c in profi:
        manut_nf.comboProfi.addItem(f"{c[1]} -> {c[2]}", QVariant(c[0]))

def fpag_nf_combo_manut():
    manut_nf.comboFpag.clear()
    fpags = banco.busca_todos_fpags_ativas()
    for c in fpags:
        manut_nf.comboFpag.addItem(f"{c[1]}", QVariant(c[0]))

def calcular_desconto():
    desconto = nf.VipSlider.value()
    nf.lbhs.setText(f'Desconto fidelidade ' + f'{desconto}%')
    preco_fat = nf.InputPtab.value()
    preco_fat = preco_fat-(preco_fat*desconto)/100
    nf.InputPfat.setValue(preco_fat)

def calcular_desconto_manut():
    desconto = manut_nf.VipSlider.value()
    manut_nf.lbhs.setText(f'Desconto fidelidade ' + f'{desconto}%')
    preco_fat = manut_nf.InputPtab.value()
    preco_fat = preco_fat-(preco_fat*desconto)/100
    manut_nf.InputPfat.setValue(preco_fat)

def emitir_nf():
    id_cliente = nf.comboClientes.currentData()
    nome_cli= nf.comboClientes.currentText()
    desconto_fidelidade = nf.vip.isVisible()
    banco.gravar_nf(id_cliente, desconto=desconto_fidelidade)
    numero_nf = banco.proxima_nf()
    numero_nf = numero_nf[0]
    nf.NumeroNf.setValue(numero_nf)
    nf.Id_Cliente.setValue(id_cliente)
    nf.Inome.setText(nome_cli)
    nf.tabWidget.setCurrentIndex(1)
    carrega_itens_nf()

def inserir_item_nf():
    num_nf = nf.NumeroNf.value()
    codigo = nf.comboServicos.currentData()
    item = nf.comboServicos.currentText()
    id_profi = nf.comboProfi.currentData()
    id_fpag = nf.comboFpag.currentData()
    preco_tab = nf.InputPtab.value()
    preco_fat = nf.InputPfat.value()
    desc = nf.VipSlider.value()
    id_cliente = nf.Id_Cliente.value()
    fidelidade = nf.frame_vip.isVisible()
    banco.inserir_itens_nf(num_nf, codigo, id_profi, id_fpag, preco_tab, preco_fat, desc, fidelidade, id_cliente)
    carrega_itens_nf()
    QMessageBox.about(nf, 'ITEM INCLUÍDO', f'Item {item} incluído com sucesso')
    


def inserir_item_nf_manut():
    num_nf = manut_nf.NumeroNf.value()
    codigo = manut_nf.comboServicos.currentData()
    item = manut_nf.comboServicos.currentText()
    id_profi = manut_nf.comboProfi.currentData()
    id_fpag = manut_nf.comboFpag.currentData()
    preco_tab = manut_nf.InputPtab.value()
    preco_fat = manut_nf.InputPfat.value()
    desc = manut_nf.VipSlider.value()
    id_cliente = manut_nf.Id_Cliente.value()
    fidelidade = manut_nf.frame_vip.isVisible()
    banco.inserir_itens_nf(num_nf, codigo, id_profi, id_fpag, preco_tab, preco_fat, desc, fidelidade, id_cliente)
    carrega_itens_nf_manut()
    QMessageBox.about(manut_nf, 'ITEM INCLUÍDO', f'Item {item} incluído com sucesso')
    

def carrega_itens_nf():
    num_nf = nf.NumeroNf.value()
    tabela = nf.TabelaItensNf
    row = 0
    itens_nf = banco.buscar_itens_nf(num_nf)
    tabela.setRowCount(len(itens_nf))
    tabela.setColumnWidth(0, 50)
    tabela.setColumnWidth(1, 250)
    tabela.setColumnWidth(2, 180)
    tabela.setColumnWidth(3, 120)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setColumnWidth(6, 150)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in itens_nf:
        total += c[5]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[4]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'R$ {c[5]:.2f}'))
        if c[6] == 0:
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'NÃO'))
        else:
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'SIM'))
        if c[7] == 0:    
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'Zero'))
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'{c[7]} %'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{c[8]}'))
        row += 1
        nf.lbl_total.setText(f'Total dos itens da nota: R$ {total:.2f}')


def carrega_itens_nf_manut():
    num_nf = manut_nf.NumeroNf.value()
    tabela = manut_nf.TabelaItensNf
    row = 0
    itens_nf = banco.buscar_itens_nf(num_nf)
    tabela.setRowCount(len(itens_nf))
    tabela.setColumnWidth(0, 50)
    tabela.setColumnWidth(1, 250)
    tabela.setColumnWidth(2, 180)
    tabela.setColumnWidth(3, 120)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setColumnWidth(6, 150)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in itens_nf:
        total += c[5]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[4]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'R$ {c[5]:.2f}'))
        if c[6] == 0:
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'NÃO'))
        else:
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'SIM'))
        if c[7] == 0:    
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'Zero'))
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'{c[7]} %'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{c[8]}'))
        row += 1
        manut_nf.lbl_total.setText(f'Total dos itens da nota: R$ {total:.2f}')

def excluir_item_nf():
    linha = nf.TabelaItensNf.currentRow()
    id_item = int(nf.TabelaItensNf.item(linha, 0).text())
    item = nf.TabelaItensNf.item(linha, 1).text()
    men = QMessageBox.question(nf, 'EXCLUIR ITEM DA NOTA', f'ATENÇÃO, deseja realmente excluir da nota o item {item}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.excluir_item_nf(id_item)
        QMessageBox.about(nf, 'ITEM EXCLUÍDO', f'Item {item} excluído com sucesso')
        carrega_itens_nf()
    else:
        return

def excluir_item_nf_manut():
    status = manut_nf.Istatus.text()
    if status == 'Pendente':
        linha = manut_nf.TabelaItensNf.currentRow()
        id_item = int(manut_nf.TabelaItensNf.item(linha, 0).text())
        item = manut_nf.TabelaItensNf.item(linha, 1).text()
        men = QMessageBox.question(manut_nf, 'EXCLUIR ITEM DA NOTA', f'ATENÇÃO, deseja realmente excluir da nota o item {item}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            banco.excluir_item_nf(id_item)
            QMessageBox.about(manut_nf, 'ITEM EXCLUÍDO', f'Item {item} excluído com sucesso')
            carrega_itens_nf_manut()
        else:
            return
    else:
        QMessageBox.about(manut_nf, 'ERRO', f'Nota fiscal já foi emitida, caso necessário vocẽ precisa cancelar a nota')


def finalizar_nf():
    num_nf = nf.NumeroNf.value()
    total = banco.calcula_total_nf(num_nf)
    if total[0][0] == None:
        QMessageBox.about(nf, 'ERRO', f'Nota fiscal não pode ser gerada pois não foi incluido nenhum item')
    else:
        valor_total = float(total[0][0])
        banco.atualizar_nf(num_nf, valor_total)
        QMessageBox.about(nf, 'NOTA EMITIDA', f'Nota fiscal emitida com sucesso')
        nf.tabWidget.setCurrentIndex(0)
        nf.close()
        carrega_tabelas_nf()
        vendas.tabWidget.setCurrentIndex(1)
        vendas.lbl_escolha.setText('')

def finalizar_nf_manut():
    num_nf = manut_nf.NumeroNf.value()
    total = banco.calcula_total_nf(num_nf)
    if total[0][0] == None:
        QMessageBox.about(manut_nf, 'ERRO', f'Nota fiscal não pode ser gerada pois não foi incluido nenhum item')
    else:
        valor_total = float(total[0][0])
        banco.atualizar_nf(num_nf, valor_total)
        QMessageBox.about(manut_nf, 'NOTA EMITIDA', f'Nota fiscal emitida com sucesso')
        manut_nf.close()
        carrega_tabelas_nf()
        vendas.tabWidget.setCurrentIndex(1)
        vendas.lbl_escolha.setText('')


def carrega_combos_nf():
    nf.tabWidget.setCurrentIndex(0)
    cliente_nf_combo()
    servico_nf_combo()
    profi_nf_combo()
    fpag_nf_combo()

def carrega_combos_nf_manut():
    servico_nf_combo_manut()
    profi_nf_combo_manut()
    fpag_nf_combo_manut()

def carrega_todas_nfs():
    tabela = vendas.TabelaNfs
    row = 0
    nfs = banco.busca_todas_notas()
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 50)
    tabela.setColumnWidth(1, 130)
    tabela.setColumnWidth(2, 80)
    tabela.setColumnWidth(3, 300)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setColumnWidth(6, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[4]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        data = funcoes.banco_data(c[1])
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{data}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[4]:.2f}'))
        if c[5] == 0:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'NÃO'))
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'SIM'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{c[6]}'))
        row += 1
        vendas.lbl_total.setText(f'Total das notas listadas: R$ {total:.2f}')

def carrega_nfs_emitidas():
    tabela = vendas.TabelaEmitidas
    row = 0
    nfs = banco.busca_todas_notas_status('Emitida')
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 50)
    tabela.setColumnWidth(1, 130)
    tabela.setColumnWidth(2, 80)
    tabela.setColumnWidth(3, 300)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setColumnWidth(6, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[4]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        data = funcoes.banco_data(c[1])
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{data}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[4]:.2f}'))
        if c[5] == 0:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'NÃO'))
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'SIM'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{c[6]}'))
        row += 1
        vendas.lbl_total_emitidas.setText(f'Total das notas listadas: R$ {total:.2f}')


def carrega_nfs_pendentes():
    tabela = vendas.TabelaPendentes
    row = 0
    nfs = banco.busca_todas_notas_status('Pendente')
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 50)
    tabela.setColumnWidth(1, 130)
    tabela.setColumnWidth(2, 80)
    tabela.setColumnWidth(3, 300)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setColumnWidth(6, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[4]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        data = funcoes.banco_data(c[1])
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{data}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[4]:.2f}'))
        if c[5] == 0:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'NÃO'))
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'SIM'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{c[6]}'))
        row += 1
        vendas.lbl_total_pendentes.setText(f'Total das notas listadas: R$ {total:.2f}')

def carrega_nfs_canceladas():
    tabela = vendas.TabelaCanceladas
    row = 0
    nfs = banco.busca_todas_notas_status('Cancelada')
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 50)
    tabela.setColumnWidth(1, 130)
    tabela.setColumnWidth(2, 80)
    tabela.setColumnWidth(3, 300)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setColumnWidth(6, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[4]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        data = funcoes.banco_data(c[1])
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{data}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[4]:.2f}'))
        if c[5] == 0:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'NÃO'))
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'SIM'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{c[6]}'))
        row += 1
        vendas.lbl_total_canceladas.setText(f'Total das notas listadas: R$ {total:.2f}')


def carrega_todas_nfs_cliente():
    id_cliente = nf_cliente.comboClientes.currentData()
    tabela = vendas.TabelaNfs
    row = 0
    nfs = banco.buscar_nf_cliente(id_cliente)
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 50)
    tabela.setColumnWidth(1, 130)
    tabela.setColumnWidth(2, 80)
    tabela.setColumnWidth(3, 300)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setColumnWidth(6, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[4]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        data = funcoes.banco_data(c[1])
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{data}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[4]:.2f}'))
        if c[5] == 0:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'NÃO'))
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'SIM'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{c[6]}'))
        row += 1
        vendas.lbl_total.setText(f'Total das notas listadas: R$ {total:.2f}')
    carrega_nfs_emitidas_clientes()
    carrega_nfs_pendentes_clientes()
    carrega_nfs_canceladas_clientes()
    nf_cliente.close()

def carrega_nfs_emitidas_clientes():
    id_cliente = nf_cliente.comboClientes.currentData()
    tabela = vendas.TabelaEmitidas
    row = 0
    nfs = banco.buscar_nf_cliente_status(id_cliente, 'Emitida')
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 50)
    tabela.setColumnWidth(1, 130)
    tabela.setColumnWidth(2, 80)
    tabela.setColumnWidth(3, 300)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setColumnWidth(6, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[4]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        data = funcoes.banco_data(c[1])
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{data}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[4]:.2f}'))
        if c[5] == 0:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'NÃO'))
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'SIM'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{c[6]}'))
        row += 1
        vendas.lbl_total_emitidas.setText(f'Total das notas listadas: R$ {total:.2f}')


def carrega_nfs_pendentes_clientes():
    id_cliente = nf_cliente.comboClientes.currentData()
    tabela = vendas.TabelaPendentes
    row = 0
    nfs = banco.buscar_nf_cliente_status(id_cliente, 'Pendente')
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 50)
    tabela.setColumnWidth(1, 130)
    tabela.setColumnWidth(2, 80)
    tabela.setColumnWidth(3, 300)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setColumnWidth(6, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[4]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        data = funcoes.banco_data(c[1])
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{data}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[4]:.2f}'))
        if c[5] == 0:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'NÃO'))
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'SIM'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{c[6]}'))
        row += 1
        vendas.lbl_total_pendentes.setText(f'Total das notas listadas: R$ {total:.2f}')


def carrega_nfs_canceladas_clientes():
    id_cliente = nf_cliente.comboClientes.currentData()
    tabela = vendas.TabelaCanceladas
    row = 0
    nfs = banco.buscar_nf_cliente_status(id_cliente, 'Cancelada')
    tabela.setRowCount(len(nfs))
    tabela.setColumnWidth(0, 50)
    tabela.setColumnWidth(1, 130)
    tabela.setColumnWidth(2, 80)
    tabela.setColumnWidth(3, 300)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setColumnWidth(6, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    total = 0
    for c in nfs:
        total += c[4]
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        data = funcoes.banco_data(c[1])
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{data}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'R$ {c[4]:.2f}'))
        if c[5] == 0:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'NÃO'))
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'SIM'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{c[6]}'))
        row += 1
        vendas.lbl_total_canceladas.setText(f'Total das notas listadas: R$ {total:.2f}')

def pega_nf():
    carrega_combos_nf_manut()
    linha = vendas.TabelaNfs.currentRow()
    nota_fiscal = int(vendas.TabelaNfs.item(linha, 0).text())
    nota = banco.busca_nf(nota_fiscal)
    manut_nf.NumeroNf.setValue(nota[0])
    manut_nf.Istatus.setText(nota[6])
    manut_nf.Inome.setText(nota[3])
    manut_nf.Id_Cliente.setValue(nota[2])
    manut_nf.frame_vip.setVisible(nota[5])
    manut_nf.lbl_total.setText('')
    carrega_itens_nf_manut()
    if nota[6] != 'Pendente':
        manut_nf.BtnInserir.setVisible(False)
        manut_nf.BtnCalcularNf.setVisible(False)
    else:
        manut_nf.BtnInserir.setVisible(True)
        manut_nf.BtnCalcularNf.setVisible(True)
    manut_nf.show()


def pega_nf_emitida():
    carrega_combos_nf_manut()
    linha = vendas.TabelaEmitidas.currentRow()
    nota_fiscal = int(vendas.TabelaEmitidas.item(linha, 0).text())
    nota = banco.busca_nf(nota_fiscal)
    manut_nf.NumeroNf.setValue(nota[0])
    manut_nf.Istatus.setText(nota[6])
    manut_nf.Inome.setText(nota[3])
    manut_nf.Id_Cliente.setValue(nota[2])
    manut_nf.frame_vip.setVisible(nota[5])
    manut_nf.lbl_total.setText('')
    carrega_itens_nf_manut()
    if nota[6] != 'Pendente':
        manut_nf.BtnInserir.setVisible(False)
        manut_nf.BtnCalcularNf.setVisible(False)
    else:
        manut_nf.BtnInserir.setVisible(True)
        manut_nf.BtnCalcularNf.setVisible(True)
    manut_nf.show()

def pega_nf_pendente():
    carrega_combos_nf_manut()
    linha = vendas.TabelaPendentes.currentRow()
    nota_fiscal = int(vendas.TabelaPendentes.item(linha, 0).text())
    nota = banco.busca_nf(nota_fiscal)
    manut_nf.NumeroNf.setValue(nota[0])
    manut_nf.Istatus.setText(nota[6])
    manut_nf.Inome.setText(nota[3])
    manut_nf.Id_Cliente.setValue(nota[2])
    manut_nf.frame_vip.setVisible(nota[5])
    manut_nf.lbl_total.setText('')
    carrega_itens_nf_manut()
    if nota[6] != 'Pendente':
        manut_nf.BtnInserir.setVisible(False)
        manut_nf.BtnCalcularNf.setVisible(False)
    else:
        manut_nf.BtnInserir.setVisible(True)
        manut_nf.BtnCalcularNf.setVisible(True)
    manut_nf.show()    


def cancelar_nf():
    num_nf = manut_nf.NumeroNf.value()
    men = QMessageBox.question(manut_nf, 'CANCELAR NOTA', f'ATENÇÃO, deseja realmente cancelar essa nota?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.atualizar_nf_cancelamento(num_nf, 0)
        banco.excluir_itens_nf(num_nf)
        QMessageBox.about(manut_nf, 'NOTA CANCELADA', f'Nota cancelada com sucesso')
        carrega_itens_nf_manut()
        manut_nf.close()
        carrega_tabelas_nf()
        vendas.tabWidget.setCurrentIndex(3)
    else:
        return


def escrever_cliente():
    vendas.lbl_escolha.setText('')
    cliente = nf_cliente.comboClientes.currentText()
    vendas.lbl_escolha.setText(f'Cliente: {cliente}')

def escrever_data():
    vendas.lbl_escolha.setText('')
    data = nf_data.InputData.text()
    vendas.lbl_escolha.setText(f'Data de emissão: {data}')

def carrega_tabelas_nf():
    carrega_todas_nfs()
    carrega_nfs_emitidas()
    carrega_nfs_pendentes()
    carrega_nfs_canceladas()
    vendas.show()

def rb_todas_nfs():
    vendas.lbl_escolha.setText('')
    carrega_tabelas_nf()



def abrir_consulta_cliente():
    nf_cliente.comboClientes.clear()
    clientes = banco.busca_todos_clientes_combo()
    for c in clientes:
        nf_cliente.comboClientes.addItem(f'{c[1]}', QVariant(c[0]))
    nf_cliente.show()




if __name__ == '__main__':
    usuario1 = Usuarios
    usuario_banco = banco.buscar_usuario('ADMIN')
    #print(usuario_banco)
    usuario1.banco_para_modelo(usuario1, usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS NF
    nf = uic.loadUi('emissao_nf.ui')
    vendas = uic.loadUi('vendas.ui')
    manut_nf = uic.loadUi('manut_nf.ui')
    nf_cliente = uic.loadUi('nf_por_cliente.ui')
    nf_data = uic.loadUi('nf_por_data.ui')
    
    #BOTÕES NF
    vendas.BtnNVenda.clicked.connect(carrega_combos_nf)
    vendas.TabelaNfs.doubleClicked.connect(pega_nf)
    vendas.TabelaEmitidas.doubleClicked.connect(pega_nf_emitida)
    vendas.TabelaPendentes.doubleClicked.connect(pega_nf_pendente)
    vendas.RbTodas.clicked.connect(rb_todas_nfs)
    vendas.RbCliente.clicked.connect(abrir_consulta_cliente)
    vendas.RbData.clicked.connect(nf_data.show)
    nf_cliente.BtnConfirmar.clicked.connect(carrega_todas_nfs_cliente)
    nf_cliente.comboClientes.currentTextChanged.connect(escrever_cliente)
    nf_data.InputData.setDate(data_atual)
    nf_data.BtnConfirmar.clicked.connect(escrever_data)
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
    manut_nf.BtnCalcularNf.clicked.connect(finalizar_nf_manut)
    ##############
    
    carrega_tabelas_nf()
    #carrega_servicos()  
    banco.cria_tabelas()
    qt.exec_()