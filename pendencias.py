import sqlite3
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import flush
import banco
from PyQt5.QtWidgets import QMessageBox
from datetime import date, datetime
from classes import Usuarios
from time import sleep

def teste():
    print('Tudo OK')

data_atual = date.today()

#FUNÇÕES DE VERIFICAÇÃO DE PENDÊNCIAS

def verificar_pendencias():
    nf_pendentes = banco.busca_todas_notas_status('Pendente')
    ag_pendentes = banco.busca_toda_agenda_dia_pendentes('Pendente')
    ag_efetuados = banco.busca_toda_agenda_dia_pendentes('Serviço efetuado')
    notas_pendentes = len(nf_pendentes)
    agendamentos_pendentes = len(ag_pendentes)
    agendamentos_efetuados = len(ag_efetuados)
    if usuario1.faturamento:
        if notas_pendentes != 0 or agendamentos_efetuados != 0:
            return True
        else:
            return False
        
    elif usuario1.agenda:
        if agendamentos_pendentes != 0:
            return True
        else:
            return False
    else:
        return False


def buscar_pendencias():
    pendencias.Mensagem.addItem('Verificação de pendências...')
    nf_pendentes = banco.busca_todas_notas_status('Pendente')
    ag_pendentes = banco.busca_toda_agenda_dia_pendentes('Pendente')
    ag_efetuados = banco.busca_toda_agenda_dia_pendentes('Serviço efetuado')
    notas_pendentes = len(nf_pendentes)
    agendamentos_pendentes = len(ag_pendentes)
    agendamentos_efetuados = len(ag_efetuados)
    if usuario1.faturamento:
        if notas_pendentes != 0:
            if notas_pendentes == 1:
                pendencias.Mensagem.addItem(f'Existe {notas_pendentes} nota pendente, verifique')
            else:
                pendencias.Mensagem.addItem(f'Existem {notas_pendentes} notas pendentes, verifique')
        
        if agendamentos_efetuados != 0:
            if agendamentos_efetuados == 1:
                pendencias.Mensagem.addItem(f'Existe {agendamentos_efetuados} agendamento com serviço efetuado aguardando emissão de nota fiscal, verifique')
            else:
                pendencias.Mensagem.addItem(f'Existem {agendamentos_efetuados} agendamentos com serviço efetuado aguardando emissão de nota fiscal, verifique')
    else:
        pendencias.Mensagem.addItem('Não encontrado pendências de notas fiscais ou de agendamentos no faturamento')


    if usuario1.agenda:
        if agendamentos_pendentes != 0:
            if agendamentos_pendentes == 1:
                pendencias.Mensagem.addItem(f'Existe {agendamentos_pendentes} agendamento pendente aguardando verificação, por favor verifique')
            else:
                pendencias.Mensagem.addItem(f'Existem {agendamentos_pendentes} agendamentos pendentes aguardando verificação, por favor verifique')
    else:
        pendencias.Mensagem.addItem('Não encontrado pendências nos agendamentos')



if __name__ == '__main__':
    usuario1 = Usuarios()
    usuario_banco = banco.buscar_usuario('ADMIN')
    #print(usuario_banco)
    usuario1.banco_para_modelo(usuario_banco)
    qt = QtWidgets.QApplication(sys.argv)
    
    #TELAS VERIFICAÇÃO DE PENDÊNCIAS
    pendencias = uic.loadUi('telas_duda/pendencias.ui')
    
    
    
    #BOTÕES SERVIÇOS
    '''servico.BtnInserir.clicked.connect(inserir_servico)
    servico.TabelaServicos.doubleClicked.connect(pega_servico)
    manut_servico.BtnSair.clicked.connect(manut_servico.close)
    manut_servico.BtnDesligar.clicked.connect(desligar_servico)
    manut_servico.BtnReativar.clicked.connect(reativar_servico)
    manut_servico.BtnAlterar.clicked.connect(alterar_servico)'''

    ##############

    #menu.showMaximized()
    #carrega_servicos()
    buscar_pendencias()
    pendencias.show()
    banco.cria_tabelas()
    qt.exec_()