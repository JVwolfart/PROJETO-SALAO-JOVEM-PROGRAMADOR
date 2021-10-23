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
    print('Tudo OK')

data_atual = date.today()
hora = datetime.now().time()


def escreve_data():    
    if agenda.InputData.date() == data_atual:
        agenda.lbl_dia.setText("Hoje é dia: " + agenda.InputData.text())
    else:
        dia = agenda.InputData.text()
        agenda.lbl_dia.setText(f"Data selecionada: {dia}")
        
def setar_hoje():
    agenda.InputData.setDate(data_atual)

def consulta_agenda():

    print ("cheguei")
    data_sel = funcoes.data_banco(ag.InputData.text())
    print(data_sel)
    print(data_atual)
    data_valida = (funcoes.inicial_maior_final(str(data_atual),str(data_sel)))
    if not data_valida:
        QMessageBox.about(ag, 'DATA INVÁLIDA', f'ATENÇÃO !! A data do agendamento precisa ser igual ou maior que a data atual')
        
    else:

        cliente_id = ag.comboClientes.currentData()
        profi_id = ag.comboProfi.currentData()
        cliente = banco.busca_cliente_id(cliente_id)
        profi = banco.busca_func_id(profi_id)
        data = ag.InputData.text()

        ag.data_agendamento.setText(data)
        ag.id_profi.setText(str(profi[0][0]))
        ag.profissional.setText(profi[0][1])
        ag.especialidade.setText(profi[0][2])
        ag.id_cliente.setText(str(cliente[0][0]))
        ag.cliente.setText(cliente[0][1])
        ag.telefone.setText(cliente[0][2])

        ag.tabWidget.setCurrentIndex(1)
        
        print(cliente)
        print(profi)


def cliente_ag_combo():
    ag.comboClientes.clear()
    clientes = banco.busca_todos_clientes_combo_ativos()
    for c in clientes:
        ag.comboClientes.addItem(f"{c[1]}", QVariant(c[0]))

def servico_ag_combo():
    ag.comboServicos.clear()
    servicos = banco.busca_todos_servicos_ativos()
    for c in servicos:
        ag.comboServicos.addItem(f"{c[1]}", QVariant(c[0]))


def profi_ag_combo():
    ag.comboProfi.clear()
    profi = banco.busca_todos_funcionarios_combo_ativos()
    for c in profi:
        ag.comboProfi.addItem(f"{c[1]} -> {c[2]}", QVariant(c[0]))
    


def inicia_agendamento():
    profi_ag_combo()
    cliente_ag_combo()
    servico_ag_combo()
    ag.show()

def grava_agendamento():
    data = ag.data_agendamento.text()
    hora = ag.hora.text()
    id_cliente= int(ag.id_cliente.text())
    id_profi = int(ag.id_profi.text())
    id_servico = ag.comboServicos.currentData()
    data = funcoes.data_banco(data)
    print(data, hora, id_cliente, id_profi, id_servico)
    banco.inserir_agendamento(data,hora,id_cliente,id_profi,id_servico)
    QMessageBox.about(ag, 'AGENDAMENTO INSERIDO', f'ATENÇÃO !! AGENDAMENTO INSERIDO COM SUCESSO')
    



def agendamento():
    dia = ag.InputData.text()
    dia = datetime(int(dia[6:]), int(dia[3:5]), int(dia[0:2]))
    if dia.date() == data_atual:
        hora = datetime.now().time()    
        if ag.hora.time()<= hora:
            print('hora menor')
            QMessageBox.about(ag, 'HORA INVÁLIDA', f'ATENÇÃO !! A HORA do agendamento precisa ser maior que a HORA atual')
        else:
            print('ok')
            grava_agendamento()
         
    else:
        print('dia diferente')
        grava_agendamento()
        
        
        

if __name__ == '__main__':
    usuario1 = Usuarios
    usuario_banco = banco.buscar_usuario('ADMIN')
    #print(usuario_banco)
    usuario1.banco_para_modelo(usuario1, usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS ESTATISTICAS
    agenda = uic.loadUi('agenda.ui')
    ag = uic.loadUi('agendamento.ui')
    
    
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
    agenda.InputData.setDate(data_atual)
    ag.InputData.setDate(data_atual)
    agenda.lbl_dia.setText("Hoje é dia: " + agenda.InputData.text())
    agenda.InputData.dateChanged.connect(escreve_data)
    agenda.BtnAgendamento.clicked.connect(inicia_agendamento)
    agenda.BtnHoje.clicked.connect(setar_hoje)
    ag.BtnConsultaAgenda.clicked.connect(consulta_agenda)
    ag.BtnSair.clicked.connect(ag.close)
    ag.BtnAgendar.clicked.connect(agendamento)
    
    '''hora = datetime.now().time()
    
    ag.hora.setTime(hora)
    hora_fim = datetime.time.fromisoformat('08:00:00')
    ag.hora.setTime(hora_fim)  
'''
    agenda.show()
    banco.cria_tabelas()
    qt.exec_()