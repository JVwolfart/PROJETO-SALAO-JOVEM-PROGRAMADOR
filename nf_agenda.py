import sqlite3
import sys
from PyQt5 import uic, QtWidgets
import banco
from PyQt5.QtWidgets import QMessageBox
from datetime import date, datetime, time, timedelta
from classes import Usuarios
from PyQt5.QtCore import QVariant
import funcoes


def teste():
    QMessageBox.about(nf_agenda, 'Tudo OK', 'Tudo Ok até aqui, mas falta implementar')


data_atual = date.today()
hora = datetime.now().time()

#FUNÇÕES DA AGENDA
def inicializar_nf_agenda():
    carrega_tabela_serv_efetuado()    
    nf_agenda.show()
    

def carrega_tabela_serv_efetuado():
    serv = banco.busca_serv_efetuado_agenda()
    tabela = nf_agenda.TabelaAgenda_NF
    row = 0
    tabela.setRowCount(len(serv))
    tabela.setColumnWidth(0, 100)
    tabela.setColumnWidth(1, 250)
    tabela.setColumnWidth(2, 250)
    tabela.setColumnWidth(3, 250)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setColumnWidth(6, 150)
    tabela.setColumnWidth(7, 30)
    
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in serv:
        data = funcoes.banco_data(c[0])
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{data}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        if c[4] == 1:
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'NÃO'))

        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'R$ {c[5]:.2f}'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{c[6]}'))
        tabela.setItem(row, 7, QtWidgets.QTableWidgetItem(f'{c[7]}'))
        
        row += 1
        
def fpag_nf_combo_agenda():
    nf_ag.comboFpag.clear()
    fpags = banco.busca_todos_fpags_ativas()
    for c in fpags:
        nf_ag.comboFpag.addItem(f"{c[1]}", QVariant(c[0]))
        
        
def pega_serv_efetuado():
    fpag_nf_combo_agenda()
    
    linha = nf_agenda.TabelaAgenda_NF.currentRow()
    id_agenda = int(nf_agenda.TabelaAgenda_NF.item(linha, 7).text())
    nf_ag.Id_agenda.setValue(id_agenda)
    serv = banco.busca_serv_agenda_id(id_agenda)
    fidelizado = serv[0][7]
    nf_ag.frame_vip.setVisible(fidelizado)
    preco_tab = serv[0][8] 
    nf_ag.InputPtab.setValue(preco_tab)
    nf_ag.InputPfat.setValue(preco_tab)
    id_cliente = serv[0][3]
    nf_ag.Id_Cliente.setValue(id_cliente)
    id_profi = serv[0][1]
    nf_ag.Id_Profi.setValue(id_profi)
    id_serv = serv[0][5]
    nf_ag.codigo_servico.setValue(id_serv)
    nf_ag.Inome.setText(serv[0][4])
    nf_ag.IProfi.setText(serv[0][2])
    nf_ag.IServ.setText(serv[0][6])
    #fpag = nf_ag.comboFpag.currentData()
    #print(fpag)
    nf_ag.show()


    print(serv)

    

def emitir_nf():
    cliente_nome = nf_ag.Inome.text()
    id_agenda = nf_ag.Id_agenda.value()
    id_cliente= nf_ag.Id_Cliente.value()
    id_profi = nf_ag.Id_Profi.value()
    id_serv = nf_ag.codigo_servico.value()
    fpag = nf_ag.comboFpag.currentData()
    fidelidade = nf_ag.frame_vip.isVisible()
    valorFat = nf_ag.InputPfat.value()
    valorTab = nf_ag.InputPtab.value()
    desc = nf_ag.VipSlider.value()
    banco.gravar_nf(id_cliente, valorFat,'Emitida',fidelidade)
    numero_nf = banco.proxima_nf()
    numero_nf = numero_nf[0]
    banco.inserir_itens_nf(numero_nf,id_serv,id_profi,fpag,valorTab,valorFat,desc,fidelidade,id_cliente)
    banco.alterar_status_ag_nf_emitida(id_agenda,"Nota Fiscal Emitida")
    QMessageBox.about(nf_ag, 'Nota fiscal emitida', f'Nota Fiscal numero {numero_nf} emitida com sucesso para o cliente {cliente_nome} ')
    nf_ag.VipSlider.setValue(0)
    nf_ag.close()
    carrega_tabela_serv_efetuado()
    


def calcular_desconto_nf_agenda():
    desconto = nf_ag.VipSlider.value()
    nf_ag.lbhs.setText(f'Desconto fidelidade ' + f'{desconto}%')
    preco_fat = nf_ag.InputPtab.value()
    preco_fat = preco_fat-(preco_fat*desconto)/100
    nf_ag.InputPfat.setValue(preco_fat)


if __name__ == '__main__':
    usuario1 = Usuarios
    usuario_banco = banco.buscar_usuario('ADMIN')
    
    usuario1.banco_para_modelo(usuario1, usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS EMISSÃO DE NF PELA AGENDA
    nf_agenda = uic.loadUi('nf_agenda.ui')
    nf_ag = uic.loadUi('emissao_nf_agenda.ui')
    nf_ag.VipSlider.valueChanged.connect(calcular_desconto_nf_agenda)





    #BOTÕES AGENDA
    nf_agenda.TabelaAgenda_NF.doubleClicked.connect(pega_serv_efetuado)
    nf_ag.BtnEmitir.clicked.connect(emitir_nf)    
    ##############
    inicializar_nf_agenda()
    banco.cria_tabelas()
    qt.exec_()