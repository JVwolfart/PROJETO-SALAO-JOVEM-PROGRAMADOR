import sqlite3
import sys
from PyQt5 import uic, QtWidgets
import banco
from PyQt5.QtWidgets import QMessageBox
from datetime import date, datetime
from classes import Usuarios
from PyQt5.QtCore import QVariant

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

def calcular_desconto():
    desconto = nf.VipSlider.value()
    nf.lbhs.setText(f'Desconto fidelidade ' + f'{desconto}%')
    preco_fat = nf.InputPtab.value()
    preco_fat = preco_fat-(preco_fat*desconto)/100
    nf.InputPfat.setValue(preco_fat)

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
    print(fidelidade)
    banco.inserir_itens_nf(num_nf, codigo, id_profi, id_fpag, preco_tab, preco_fat, desc, fidelidade, id_cliente)
    QMessageBox.about(nf, 'ITEM INCLUÍDO', f'Item {item} incluído com sucesso')
    carrega_itens_nf()

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
    

def finalizar_nf():
    num_nf = nf.NumeroNf.value()
    total = banco.calcula_total_nf(num_nf)
    if total[0][0] == None:
        QMessageBox.about(nf, 'ERRO', f'Nota fiscal não pode ser gerada pois não foi incluido nenhum item')
    valor_total = float(total[0][0])
    banco.atualizar_nf(num_nf, valor_total)
    QMessageBox.about(nf, 'NOTA EMITIDA', f'Nota fiscal emitida com sucesso')
    nf.tabWidget.setCurrentIndex(0)


if __name__ == '__main__':
    usuario1 = Usuarios
    usuario_banco = banco.buscar_usuario('ADMIN')
    #print(usuario_banco)
    usuario1.banco_para_modelo(usuario1, usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS NF
    nf = uic.loadUi('emissao_nf.ui')
    
    
    
    #BOTÕES NF
    '''servico.BtnInserir.clicked.connect(inserir_servico)
    servico.TabelaServicos.doubleClicked.connect(pega_servico)
    manut_servico.BtnSair.clicked.connect(manut_servico.close)
    manut_servico.BtnDesligar.clicked.connect(desligar_servico)
    manut_servico.BtnReativar.clicked.connect(reativar_servico)
    manut_servico.BtnAlterar.clicked.connect(alterar_servico)'''
    nf.vip.setVisible(0)
    nf.frame_vip.setVisible(0)
    nf.comboClientes.currentTextChanged.connect(busca_fiel)
    nf.comboServicos.currentTextChanged.connect(busca_preco)
    nf.VipSlider.valueChanged.connect(calcular_desconto)
    nf.BtnGerarNf.clicked.connect(emitir_nf)
    nf.BtnInserir.clicked.connect(inserir_item_nf)
    nf.BtnCalcularNf.clicked.connect(finalizar_nf)
    nf.TabelaItensNf.doubleClicked.connect(excluir_item_nf)

    ##############
    cliente_nf_combo()
    servico_nf_combo()
    profi_nf_combo()
    fpag_nf_combo()
    
    #carrega_servicos()  
    banco.cria_tabelas()
    qt.exec_()