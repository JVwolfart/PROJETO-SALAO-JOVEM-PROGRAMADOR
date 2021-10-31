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

#FUNÇÕES DA AGENDA
def inicializar_agenda():
    escreve_data()
    atualizar_pendentes()

def escreve_data():    
    if agenda.InputData.date() == data_atual:
        agenda.lbl_dia.setText("Hoje é dia: " + agenda.InputData.text())
    else:
        dia = agenda.InputData.text()
        agenda.lbl_dia.setText(f"Data selecionada: {dia}")
    carrega_agenda_dia_geral()
    carrega_agenda_dia_profi()
    profi_agenda_combo()
    carrega_agenda_dia_pendentes()

    agenda.show()
        
def setar_hoje():
    agenda.InputData.setDate(data_atual)

def consulta_agenda():

    data_sel = funcoes.data_banco(ag.InputData.text())

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
        carrega_ag_dia_profi()



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


def servico_ag_combo_manut():
    manut_ag.comboServicos.clear()
    servicos = banco.busca_todos_servicos_ativos()
    for c in servicos:
        manut_ag.comboServicos.addItem(f"{c[1]}", QVariant(c[0]))


def profi_ag_combo():
    ag.comboProfi.clear()
    profi = banco.busca_todos_funcionarios_combo_ativos()
    for c in profi:
        ag.comboProfi.addItem(f"{c[1]} -> {c[2]}", QVariant(c[0]))

def profi_agenda_combo():
    agenda.comboProfi.clear()
    profi = banco.busca_todos_funcionarios_combo()
    for c in profi:
        agenda.comboProfi.addItem(f"{c[1]} -> {c[2]}  -> {c[4]}", QVariant(c[0]))
    

def busca_tempo_servico():
    servico = ag.comboServicos.currentData()
    tempo = banco.busca_tempo_servico_codigo(servico)
    if len(tempo) != 0:
        ag.InputTempo.setText(f'{tempo[0][0]}')


def busca_tempo_servico_manut():
    servico = manut_ag.comboServicos.currentData()
    tempo = banco.busca_tempo_servico_codigo(servico)
    if len(tempo) != 0:
        manut_ag.InputTempo.setText(f'{tempo[0][0]}')


def inicia_agendamento():
    ag.tabWidget.setCurrentIndex(0)
    limpa_campos_ag()
    profi_ag_combo()
    cliente_ag_combo()
    servico_ag_combo()
    ag.show()


def limpa_campos_ag():
    ag.data_agendamento.setText('')
    ag.id_profi.setText('')
    ag.profissional.setText('')
    ag.especialidade.setText('')
    ag.id_cliente.setText('')
    ag.cliente.setText('')
    ag.telefone.setText('')

def grava_agendamento():
    data = ag.data_agendamento.text()
    hora = ag.hora.text()
    id_cliente= int(ag.id_cliente.text())
    id_profi = int(ag.id_profi.text())
    id_servico = ag.comboServicos.currentData()
    data = funcoes.data_banco(data)
    banco.inserir_agendamento(data,hora,id_cliente,id_profi,id_servico)
    QMessageBox.about(ag, 'AGENDAMENTO INSERIDO', f'ATENÇÃO !! AGENDAMENTO INSERIDO COM SUCESSO')
    carrega_agenda_dia_geral()
    carrega_agenda_dia_profi()
    carrega_ag_dia_profi()
    
    
def carrega_agenda_dia_geral():
    dia_escolhido = agenda.InputData.text()
    dia_escolhido = funcoes.data_banco(dia_escolhido)
    agen = banco.busca_toda_agenda_dia(dia_escolhido)
    tabela = agenda.TabelaAgenda
    row = 0
    tabela.setRowCount(len(agen))
    tabela.setColumnWidth(0, 100)
    tabela.setColumnWidth(1, 70)
    tabela.setColumnWidth(2, 100)
    tabela.setColumnWidth(3, 200)
    tabela.setColumnWidth(4, 200)
    tabela.setColumnWidth(5, 150)
    tabela.setColumnWidth(6, 250)
    tabela.setColumnWidth(7, 250)
    tabela.setColumnWidth(8, 30)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in agen:
        data = funcoes.banco_data(c[0])
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{data}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{c[4]}'))
        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'{c[5]}'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{c[6]}'))
        tabela.setItem(row, 7, QtWidgets.QTableWidgetItem(f'{c[7]}'))
        tabela.setItem(row, 8, QtWidgets.QTableWidgetItem(f'{c[8]}'))
        row += 1


def carrega_agenda_dia_pendentes():
    dia_escolhido = agenda.InputData.text()
    dia_escolhido = funcoes.data_banco(dia_escolhido)
    agen = banco.busca_toda_agenda_dia_pendentes()
    tabela = agenda.TabelaPendentes
    row = 0
    tabela.setRowCount(len(agen))
    tabela.setColumnWidth(0, 100)
    tabela.setColumnWidth(1, 70)
    tabela.setColumnWidth(2, 100)
    tabela.setColumnWidth(3, 200)
    tabela.setColumnWidth(4, 200)
    tabela.setColumnWidth(5, 150)
    tabela.setColumnWidth(6, 250)
    tabela.setColumnWidth(7, 250)
    tabela.setColumnWidth(8, 30)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in agen:
        data = funcoes.banco_data(c[0])
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{data}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{c[4]}'))
        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'{c[5]}'))
        tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'{c[6]}'))
        tabela.setItem(row, 7, QtWidgets.QTableWidgetItem(f'{c[7]}'))
        tabela.setItem(row, 8, QtWidgets.QTableWidgetItem(f'{c[8]}'))
        row += 1

def carrega_agenda_dia_profi():
    dia_escolhido = agenda.InputData.text()
    profi = agenda.comboProfi.currentData()
    dia_escolhido = funcoes.data_banco(dia_escolhido)
    agen = banco.busca_agenda_dia_profi(dia_escolhido,profi)
    tabela = agenda.TabelaAgendaProfi
    row = 0
    tabela.setRowCount(len(agen))
    tabela.setColumnWidth(0, 100)
    tabela.setColumnWidth(1, 70)
    tabela.setColumnWidth(2, 100)
    tabela.setColumnWidth(3, 250)
    tabela.setColumnWidth(4, 150)
    tabela.setColumnWidth(5, 250)
    tabela.setColumnWidth(6, 70)
    tabela.setColumnWidth(7, 250)
    tabela.setColumnWidth(8, 30)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in agen:
        data = funcoes.banco_data(c[0])
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{data}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{c[4]}'))
        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'{c[5]}'))
        if c[6]==1:
            tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'NÃO'))
        tabela.setItem(row, 7, QtWidgets.QTableWidgetItem(f'{c[7]}'))
        tabela.setItem(row, 8, QtWidgets.QTableWidgetItem(f'{c[8]}'))
        row += 1        


def carrega_ag_dia_profi():
    dia_escolhido = ag.InputData.text()
    profi = ag.comboProfi.currentData()
    dia_escolhido = funcoes.data_banco(dia_escolhido)
    agen = banco.busca_agenda_dia_profi(dia_escolhido,profi)
    tabela = ag.TabelaAgendaProfi
    row = 0
    tabela.setRowCount(len(agen))
    tabela.setColumnWidth(0, 100)
    tabela.setColumnWidth(1, 70)
    tabela.setColumnWidth(2, 100)
    tabela.setColumnWidth(3, 250)
    tabela.setColumnWidth(4, 150)
    tabela.setColumnWidth(5, 250)
    tabela.setColumnWidth(6, 70)
    tabela.setColumnWidth(7, 100)
    tabela.setColumnWidth(8, 30)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in agen:
        data = funcoes.banco_data(c[0])
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{data}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{c[4]}'))
        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'{c[5]}'))
        if c[6]==1:
            tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 6, QtWidgets.QTableWidgetItem(f'NÃO'))
        tabela.setItem(row, 7, QtWidgets.QTableWidgetItem(f'{c[7]}'))
        tabela.setItem(row, 8, QtWidgets.QTableWidgetItem(f'{c[8]}'))
        row += 1


def agendamento():
    dia = ag.InputData.text()
    dia = datetime(int(dia[6:]), int(dia[3:5]), int(dia[0:2]))
    if dia.date() == data_atual:
        hora = datetime.now().time()    
        if ag.hora.time()<= hora:
            print('hora menor')
            QMessageBox.about(ag, 'HORA INVÁLIDA', f'ATENÇÃO !! A HORA do agendamento precisa ser maior que a HORA atual')
        else:
            grava_agendamento()
         
    else:
        grava_agendamento()
        
        
def pega_ag():
    linha = ag.TabelaAgendaProfi.currentRow()
    id_agenda = ag.TabelaAgendaProfi.item(linha, 8).text()
    data = ag.TabelaAgendaProfi.item(linha, 0).text()
    hora = ag.TabelaAgendaProfi.item(linha, 1).text()
    cliente = ag.TabelaAgendaProfi.item(linha, 3).text()
    tele = ag.TabelaAgendaProfi.item(linha, 4).text()
    status = ag.TabelaAgendaProfi.item(linha, 7).text()
    serv = ag.TabelaAgendaProfi.item(linha, 5).text()
    if status == 'Serviço efetuado':
        QMessageBox.about(ag, 'ERRO', 'Serviço já foi efetuado, não pode ser alterado')
    elif status == 'Eliminado':
        QMessageBox.about(ag, 'ERRO', 'Serviço já foi eliminado, não pode mais ser alterado')
    else:
        manut_ag.InputIdAgenda.setText(id_agenda)
        manut_ag.data_agendamento.setText(data)
        hora = time.fromisoformat(hora)
        manut_ag.hora.setTime(hora)
        manut_ag.cliente.setText(cliente)
        manut_ag.telefone.setText(tele)
        manut_ag.comboStatus.setCurrentText(status)
        servico_ag_combo_manut()
        manut_ag.comboServicos.setCurrentText(serv)
        manut_ag.show()
    


def pega_agenda():
    linha = agenda.TabelaAgendaProfi.currentRow()
    id_agenda = agenda.TabelaAgendaProfi.item(linha, 8).text()
    data = agenda.TabelaAgendaProfi.item(linha, 0).text()
    hora = agenda.TabelaAgendaProfi.item(linha, 1).text()
    cliente = agenda.TabelaAgendaProfi.item(linha, 3).text()
    tele = agenda.TabelaAgendaProfi.item(linha, 4).text()
    status = agenda.TabelaAgendaProfi.item(linha, 7).text()
    serv = agenda.TabelaAgendaProfi.item(linha, 5).text()
    if status != 'Nota Fiscal Emitida':
        if status == 'Serviço efetuado':
            QMessageBox.about(agenda, 'ERRO', 'Serviço já foi efetuado, não pode ser alterado')
        elif status == 'Eliminado':
            QMessageBox.about(agenda, 'ERRO', 'Serviço já foi eliminado, não pode mais ser alterado')
        else:
            manut_ag.InputIdAgenda.setText(id_agenda)
            manut_ag.data_agendamento.setText(data)
            hora = time.fromisoformat(hora)
            manut_ag.hora.setTime(hora)
            manut_ag.cliente.setText(cliente)
            manut_ag.telefone.setText(tele)
            manut_ag.comboStatus.setCurrentText(status)
            servico_ag_combo_manut()
            manut_ag.comboServicos.setCurrentText(serv)
            manut_ag.show()
    else:
        QMessageBox.about(agenda, 'ERRO', 'Nota fiscal já foi emitida, não pode mais ser alterado')


def alterar_agendamento():
    id_ag = int(manut_ag.InputIdAgenda.text())
    hora = manut_ag.hora.text()
    status = manut_ag.comboStatus.currentText()
    codigo_servico = manut_ag.comboServicos.currentData()
    data_ag = manut_ag.data_agendamento.text()
    if status == 'Serviço efetuado':
        data_ag = funcoes.data_banco(data_ag)
        global data_atual
        dia_hoje = datetime.strftime(data_atual, '%Y-%m-%d')
        ok = funcoes.valida_data_servico_efetuado(dia_hoje, data_ag)
        if not ok:
            QMessageBox.about(manut_ag, 'ERRO', 'Opção de status inválida, serviço não pode ser considerado efetuado pois seu agendamento é pra data futura')
        else:
            banco.alterar_agendamento(hora, codigo_servico, status, id_ag)
            QMessageBox.about(manut_ag, 'AGENDAMENTO ALTERADO', 'Agendamento alterado com sucesso')
            manut_ag.close()
            carrega_ag_dia_profi()
            carrega_agenda_dia_geral()
            carrega_agenda_dia_profi()
    else:   
        banco.alterar_agendamento(hora, codigo_servico, status, id_ag)
        QMessageBox.about(manut_ag, 'AGENDAMENTO ALTERADO', 'Agendamento alterado com sucesso')
        manut_ag.close()
        carrega_ag_dia_profi()
        carrega_agenda_dia_geral()
        carrega_agenda_dia_profi()


def efetuar_agendamento():
    linha = agenda.TabelaAgenda.currentRow()
    id_ag = int(agenda.TabelaAgenda.item(linha, 8).text())
    status_ag = agenda.TabelaAgenda.item(linha, 7).text()
    data_ag = agenda.TabelaAgenda.item(linha, 0).text()
    if status_ag != 'Nota Fiscal Emitida':
        men = QMessageBox.question(agenda, 'MARCAR SERVIÇO COMO EFETUADO', f'ATENÇÃO, deseja realmente marcar esse agendamento como Serviço efetuado? Após confirmado não poderá mais ser alterado', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            data_ag = funcoes.data_banco(data_ag)
            global data_atual
            dia_hoje = datetime.strftime(data_atual, '%Y-%m-%d')
            ok = funcoes.valida_data_servico_efetuado(dia_hoje, data_ag)
            if not ok:
                QMessageBox.about(agenda, 'ERRO', 'Serviço não pode ser considerado efetuado pois seu agendamento é pra data futura')
            else:
                banco.efetuar_agendamento(id_ag)
                QMessageBox.about(manut_ag, 'SERVIÇO EFETUADO', 'Alteração de status de serviço efetuada com sucesso')
                manut_ag.close()
                carrega_ag_dia_profi()
                carrega_agenda_dia_geral()
                carrega_agenda_dia_profi()
                carrega_agenda_dia_pendentes()
        else:
            return
    else:
        QMessageBox.about(agenda, 'ERRO', 'Nota fiscal já foi emitida, não pode mais ser alterado')


def alterar_status_pendente():
    linha = agenda.TabelaPendentes.currentRow()
    id_ag = int(agenda.TabelaPendentes.item(linha, 8).text())
    efetuado = manut_pendente.RbEfetuado.isChecked()
    cancelado = manut_pendente.RbCancelado.isChecked()
    faltou = manut_pendente.RbFaltou.isChecked()
    eliminado = manut_pendente.RbEliminado.isChecked()
    if efetuado:
        status = 'Serviço efetuado'
        banco.alterar_status_pendentes(id_ag, status)
    elif cancelado:
        status = 'Cancelado pelo cliente'
        banco.alterar_status_pendentes(id_ag, status)
    elif faltou:
        status = 'Cliente não compareceu'
        banco.alterar_status_pendentes(id_ag, status)
    else:
        status = 'Eliminado'
        banco.alterar_status_pendentes(id_ag, status)
    QMessageBox.about(manut_pendente, 'STATUS ALTERADO', 'Status do agendamento alterado com sucesso')
    carrega_agenda_dia_geral()
    carrega_agenda_dia_profi()
    carrega_ag_dia_profi()
    carrega_agenda_dia_pendentes()
    manut_pendente.close()

def atualizar_pendentes():
    banco.setar_pendentes()
    carrega_agenda_dia_pendentes()

if __name__ == '__main__':
    usuario1 = Usuarios
    usuario_banco = banco.buscar_usuario('ADMIN')
    #print(usuario_banco)
    usuario1.banco_para_modelo(usuario1, usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS AGENDA
    agenda = uic.loadUi('agenda.ui')
    ag = uic.loadUi('agendamento.ui')
    manut_ag = uic.loadUi('manut_agendamento.ui')
    manut_pendente = uic.loadUi('manut_agenda.ui')
    
    
    #BOTÕES AGENDA
    
    ##############
    agenda.InputData.setDate(data_atual)
    ag.InputData.setDate(data_atual)
    agenda.lbl_dia.setText("Hoje é dia: " + agenda.InputData.text())
    agenda.InputData.dateChanged.connect(escreve_data)
    agenda.BtnAgendamento.clicked.connect(inicia_agendamento)
    agenda.BtnHoje.clicked.connect(setar_hoje)
    agenda.comboProfi.currentTextChanged.connect(carrega_agenda_dia_profi)
    agenda.TabelaAgendaProfi.doubleClicked.connect(pega_agenda)
    agenda.TabelaAgenda.doubleClicked.connect(efetuar_agendamento)
    agenda.TabelaPendentes.doubleClicked.connect(manut_pendente.show)
    ag.BtnConsultaAgenda.clicked.connect(consulta_agenda)
    ag.BtnSair.clicked.connect(ag.close)
    ag.BtnAgendar.clicked.connect(agendamento)
    ag.comboServicos.currentTextChanged.connect(busca_tempo_servico)
    ag.TabelaAgendaProfi.doubleClicked.connect(pega_ag)
    manut_ag.comboServicos.currentTextChanged.connect(busca_tempo_servico_manut)
    manut_ag.BtnAlterar.clicked.connect(alterar_agendamento)
    manut_ag.BtnSair.clicked.connect(manut_ag.close)
    manut_pendente.BtnAlterar.clicked.connect(alterar_status_pendente)
    manut_pendente.BtnSair.clicked.connect(manut_pendente.close)

    inicializar_agenda()
    banco.cria_tabelas()
    qt.exec_()