import sqlite3
import sys
from PyQt5 import uic, QtWidgets
import banco
from PyQt5.QtWidgets import QMessageBox
from datetime import date, datetime, time, timedelta
from PyQt5.QtCore import QVariant
from classes import Usuarios
import funcoes

def teste():
    QMessageBox.about(menu, 'Tudo OK', 'Tudo Ok até aqui, mas falta implementar')

data_atual = date.today()
hora = datetime.now().time()


#FUNÇÕES PARA TELA LOGIN
def fazer_login():
    usuario = login.InputUsuario.text().upper()
    senha = login.InputSenha.text()
    usuario_banco = banco.buscar_usuario(usuario)
    if usuario != "ROOT":
        usuario1.banco_para_modelo(usuario_banco)
    if usuario == 'ROOT' and senha == 'manager':
        login.close()
        cad_usuario.show()
        manut_usuarios.BtnOrdenar.setVisible(False)
        manut_usuarios.BtnOrdenarID.setVisible(False)
    else:
        if len(usuario_banco) == 0:
            QMessageBox.about(login, 'ERRO', 'Usuário inexistente no banco')
        if senha != usuario1.senha:
            QMessageBox.about(login, 'ERRO', 'Senha não confere')
        else:
            #usuario1.banco_para_modelo(usuario_banco)
            permi = banco.busca_permissoes(usuario)
            manut_usuarios.BtnOrdenar.setVisible(False)
            manut_usuarios.BtnOrdenarID.setVisible(False)
            #menu_cadastros.Btn_cadastro_usuario.setEnabled(usuario_banco[0][6])
            '''#VENDAS

            vendas.BtnCadFuncionario.setVisible(usuario_banco[0][6])
            vendas.BtnCadClientes.setVisible(usuario_banco[0][3])
            vendas.BtnCadProdutos.setVisible(usuario_banco[0][3])
            vendas.BtnNVenda.setVisible(usuario_banco[0][3])
            vendas.BtnRoot.setVisible(usuario_banco[0][6])
            if usuario_banco[0][6]:
                vendas.lbl_root.setVisible(False)
            

            #FUNCIONÁRIOS
            cad_func.BtnInserir.setVisible(usuario_banco[0][6])
            manut_func.BtnAlterar.setVisible(usuario_banco[0][4])
            manut_func.BtnDesligar.setVisible(usuario_banco[0][6])
            manut_func.BtnReativar.setVisible(usuario_banco[0][6])
            ##############

            #CLIENTES
            cad_cliente.BtnInserir.setVisible(usuario_banco[0][3])
            manut_cliente.BtnAlterar.setVisible(usuario_banco[0][4])
            manut_cliente.BtnDesligar.setVisible(usuario_banco[0][5])
            manut_cliente.BtnReativar.setVisible(usuario_banco[0][6])
            #####################

            #PRODUTOS
            cad_produtos.BtnInserir.setVisible(usuario_banco[0][3])
            manut_produtos.BtnAlterar.setVisible(usuario_banco[0][4])
            manut_produtos.BtnDesligar.setVisible(usuario_banco[0][5])
            manut_produtos.BtnReativar.setVisible(usuario_banco[0][6])
            ###############

            #NOTA FISCAL
            manut_nf.BtnInserir.setVisible(usuario_banco[0][3])
            manut_nf.BtnCalcularNf.setVisible(usuario_banco[0][3])
            manut_nf.BtnCancelarNf.setVisible(usuario_banco[0][5])
            manut_item.BtnAlterar.setVisible(usuario_banco[0][4])
            manut_item.BtnExcluir.setVisible(usuario_banco[0][5])
            '''
            ###############
            login.close()
            menu.lbl_ola.setText(f'Seja bem vindo usuário {usuario1.nome.title()}')
            #menu.lbl_id_user.setText(f'{usuario1.id}')
            menu.showMaximized()
            QMessageBox.about(menu, 'BOAS VINDAS', f'Bem vindo usuário {usuario1.nome}, você possui as seguintes permissões: {permi}')
            banco.cria_tabelas()
            carrega_tabelas()

def abrir_cria_usuario():
    if usuario1.root:
        login.close()
        cad_usuario.show()    
    else:
        erro_sem_permissao()

##############################

#FUNÇÕES PARA CRIAÇÃO DE USUÁRIOS

def abrir_tela_login():
    cad_usuario.close()
    menu.close()
    menu_cadastros.close()
    login.InputUsuario.setText('')
    login.InputSenha.setText('')
    login.show()

def criar_novo_usuario():
    usuario = cad_usuario.InputUsuario.text().upper().strip()
    senha = cad_usuario.InputSenha.text()
    confirma = cad_usuario.InputConfirmar.text()
    criar = False
    editar = False
    excluir = False
    usuario_banco = banco.buscar_usuario(usuario)
    if len(usuario) < 5 or len(senha) < 5:
        QMessageBox.about(cad_usuario, 'ERRO', 'usuário e senha devem ter pelo menos 5 caractéres')
    elif senha != confirma:
        QMessageBox.about(cad_usuario, 'ERRO', 'Senha e confirmação são diferentes')
    elif len(usuario_banco) != 0:
        QMessageBox.about(cad_usuario, 'ERRO', 'Usuário já existe no sistema')
    else:
        banco.novo_usuario(usuario, senha, criar, editar, excluir)
        QMessageBox.about(cad_usuario, 'USUÁRIO CRIADO', f'Usuário {usuario} criado com sucesso!')
        cad_usuario.InputUsuario.setText('')
        cad_usuario.InputSenha.setText('')
        cad_usuario.InputConfirmar.setText('')
        
        
################################

#MANUTENÇÃO DE USUÁRIOS

def carrega_usuarios():
    usuarios = banco.buscar_todos_usuarios()
    row = 0
    tabela = manut_usuarios.TabelaUsuarios
    tabela.setRowCount(len(usuarios))
    tabela.setColumnWidth(0, 50)
    tabela.setColumnWidth(1, 350)
    tabela.setColumnWidth(2, 100)
    tabela.setColumnWidth(3, 100)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in usuarios:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        if c[3] == 1:
            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'NÃO'))
        if c[4] == 1:
            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'NÃO'))
        if c[5] == 1:
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'NÃO'))
        if c[6] == 1:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'NÃO'))            
        row += 1
    
    

def pega_usuario():
    linha = manut_usuarios.TabelaUsuarios.currentRow()
    nome = manut_usuarios.TabelaUsuarios.item(linha, 1).text()
    criar = manut_usuarios.TabelaUsuarios.item(linha, 2).text()
    editar = manut_usuarios.TabelaUsuarios.item(linha, 3).text()
    excluir = manut_usuarios.TabelaUsuarios.item(linha, 4).text()
    root = manut_usuarios.TabelaUsuarios.item(linha, 5).text()
    permissoes.InputUsuario.setText(nome)
    if criar == 'SIM':
        permissoes.CbCriar.setChecked(True)
    else:
        permissoes.CbCriar.setChecked(False)
    
    if editar == 'SIM':
        permissoes.CbEditar.setChecked(True)
    else:
        permissoes.CbEditar.setChecked(False)

    if excluir == 'SIM':
        permissoes.CbExcluir.setChecked(True)
    else:
        permissoes.CbExcluir.setChecked(False)
    
    if root == 'SIM':
        permissoes.CbRoot.setChecked(True)
    else:
        permissoes.CbRoot.setChecked(False)
    
    permissoes.show()

def carrega_usuario_asc():
    usuarios = banco.buscar_todos_usuarios_asc()
    row = 0
    tabela = manut_usuarios.TabelaUsuarios
    tabela.setRowCount(len(usuarios))
    tabela.setColumnWidth(0, 50)
    tabela.setColumnWidth(1, 350)
    tabela.setColumnWidth(2, 100)
    tabela.setColumnWidth(3, 100)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in usuarios:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        if c[3] == 1:
            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'NÃO'))
        if c[4] == 1:
            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'NÃO'))
        if c[5] == 1:
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'NÃO'))
        if c[6] == 1:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'NÃO'))            
        row += 1
    manut_usuarios.show()


def permissao():
    carrega_usuarios()
    manut_usuarios.show()

def setar_permissoes():
    nome = permissoes.InputUsuario.text()
    criar = permissoes.CbCriar.isChecked()
    editar = permissoes.CbEditar.isChecked()
    excluir = permissoes.CbExcluir.isChecked()
    root = permissoes.CbRoot.isChecked()
    banco.alterar_permissoes(nome, criar, editar, excluir, root)
    QMessageBox.about(permissoes, 'PERMISSÕES ALTERADAS', f'Permissões do usuário {nome} alteradas com sucesso')
    carrega_usuarios()
    permissoes.close()



def erro_sem_permissao():
    QMessageBox.about(menu_cadastros, 'ERRO', f'Usuário {usuario1.nome} não tem poder para cadastrar novos usuários, essa permissão é exclusiva para ROOT')
    




#FUNÇÕES DE SERVIÇOS

def inserir_servico():
    descricao = servico.InputNome.text().strip().title()
    valor = servico.InputValor.value()
    tempo = servico.InputTempo.value()
    if descricao == '' or valor == 0 or tempo == 0:
        QMessageBox.about(servico, 'ERRO', 'Nenhum campo pode ficar vazio')
    else:
        banco.inserir_servico(descricao, valor, tempo)
        QMessageBox.about(servico, 'SERVIÇO CADASTRADO', f'Serviço {descricao} cadastrado com sucesso')
        servico.InputNome.setText('')
        servico.InputValor.setValue(0)
        servico.InputTempo.setValue(0)
        carrega_servicos()
        servico.show()

def carrega_servicos():
    tabela = servico.TabelaServicos
    servicos = banco.busca_todos_servicos()
    row = 0
    tabela.setRowCount(len(servicos))
    tabela.setColumnWidth(0, 30)
    tabela.setColumnWidth(1, 400)
    tabela.setColumnWidth(2, 150)
    tabela.setColumnWidth(3, 150)
    tabela.setColumnWidth(4, 200)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in servicos:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'R$ {c[2]:.2f}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{c[4]}'))
        row += 1
      
    


def pega_servico():
    linha = servico.TabelaServicos.currentRow()
    codigo = int(servico.TabelaServicos.item(linha, 0).text())
    descricao = servico.TabelaServicos.item(linha, 1).text()
    valor = servico.TabelaServicos.item(linha, 2).text()
    valor = valor.replace('R$ ', '')
    valor = float(valor)
    tempo = int(servico.TabelaServicos.item(linha, 3).text())
    status = servico.TabelaServicos.item(linha, 4).text()
    if status == 'Desligado' and usuario1.root == False:
        QMessageBox.about(servico, 'ERRO', f'Serviço já está desligado, solicite ao root para reativa-lo')
    else:
        manut_servico.InputId.setValue(codigo)
        manut_servico.Nome.setText(descricao)
        manut_servico.Valor.setValue(valor)
        manut_servico.Tempo.setValue(tempo)
        manut_servico.show()

def desligar_servico():
    codigo = manut_servico.InputId.value()
    nome = manut_servico.Nome.text()
    men = QMessageBox.question(manut_servico, 'DESLIGAR SERVIÇO', f'ATENÇÃO, deseja realmente desligar o serviço {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.desligar_servico(codigo)
        QMessageBox.about(manut_servico, 'SERVIÇO DESLIGADO', f'Serviço {nome} desligado com sucesso')
        carrega_servicos()
        manut_servico.close()
        servico.show()
    else:
        return


def reativar_servico():
    codigo = manut_servico.InputId.value()
    nome = manut_servico.Nome.text()
    men = QMessageBox.question(manut_servico, 'REATIVAR SERVIÇO', f'ATENÇÃO, deseja realmente reativar o serviço {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.reativar_servico(codigo)
        QMessageBox.about(manut_servico, 'SERVIÇO REATIVADO', f'Serviço {nome} reativado com sucesso')
        carrega_servicos()
        manut_servico.close()
        servico.show()
    else:
        return

def alterar_servico():
    codigo = manut_servico.InputId.value()
    nome = manut_servico.Nome.text().strip().title()
    tempo = manut_servico.Tempo.value()
    valor = manut_servico.Valor.value()
    if nome == '' or valor == 0 or tempo == 0:
        QMessageBox.about(manut_servico, 'ERRO', 'Nenhum campo pode ficar vazio')
    else:
        banco.alterar_servico(codigo, nome, valor, tempo)
        QMessageBox.about(servico, 'SERVIÇO ALTERADO', f'Serviço {nome} alterado com sucesso')
        manut_servico.Nome.setText('')
        manut_servico.Valor.setValue(0)
        manut_servico.Tempo.setValue(0)
        manut_servico.close()
        carrega_servicos()
        servico.show()


#FUNÇÕES DE clienteS

def inserir_cliente():
    nome = cliente.Inome.text().strip().title()
    telefone = cliente.Itelefone.text()
    sexo = cliente.CbSexo.currentText()
    if sexo == 'Selecione um Gênero':
        QMessageBox.about(cliente, 'ERRO', 'Selecione um Gênero')
    else:
        if nome == '' or len(nome)< 5:
            QMessageBox.about(cliente, 'ERRO', 'Campo Nome Não pode ser vazio e precisa pelo menos 5 caracteres')
        elif len(telefone)< 14:
            QMessageBox.about(cliente, 'ERRO', 'Telefone Inválido, pecisa pelo menos 10 digitos')
        else:
            banco.inserir_cliente(nome,telefone,sexo)
            QMessageBox.about(cliente, 'CLIENTE CADASTRADO', f'Cliente {nome} cadastrado com sucesso')
            cliente.Inome.setText('')
            cliente.Itelefone.setText('')
            cliente.CbSexo.setCurrentIndex(0)
            carrega_clientes()

def carrega_clientes():
    tabela = cliente.TabelaClientes
    clientes = banco.busca_todos_clientes_ordem()
    row = 0
    tabela.setRowCount(len(clientes))
    tabela.setColumnWidth(0, 60)
    tabela.setColumnWidth(1, 350)
    tabela.setColumnWidth(2, 190)
    tabela.setColumnWidth(3, 130)
    tabela.setColumnWidth(4, 100)
    tabela.setColumnWidth(5, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in clientes:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{c[4]}'))
        if c[5] == 0:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'Não'))
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f'Sim'))
        row += 1
      
    


def pega_cliente():
    linha = cliente.TabelaClientes.currentRow()
    id = int(cliente.TabelaClientes.item(linha, 0).text())
    nome = cliente.TabelaClientes.item(linha, 1).text()
    telefone = cliente.TabelaClientes.item(linha, 2).text()
    sexo = cliente.TabelaClientes.item(linha, 3).text()
    status = cliente.TabelaClientes.item(linha, 4).text()
    fidelizado = cliente.TabelaClientes.item(linha, 5).text()
    if status == 'Desligado' and usuario1.root == False:
        QMessageBox.about(cliente, 'ERRO', f'Cliente já está desligado, solicite ao root para reativa-lo')
    else:
        manut_cliente.InputId.setValue(id)
        manut_cliente.Nome.setText(nome)
        manut_cliente.Itelefone.setText(telefone)
        if sexo == "Feminino":
            manut_cliente.CbSexo.setCurrentIndex(0)
        elif sexo == "Masculino":
            manut_cliente.CbSexo.setCurrentIndex(1)
        else:
            manut_cliente.CbSexo.setCurrentIndex(2)
        
        if status == 'Desligado':
            manut_cliente.CkAtivo.setChecked(False)
        else:
            manut_cliente.CkAtivo.setChecked(True)
        if fidelizado == 'Não':
            manut_cliente.CkFidelizado.setChecked(False)
        else:
            manut_cliente.CkFidelizado.setChecked(True)
        manut_cliente.show()

def desligar_cliente():
    id = manut_cliente.InputId.value()
    nome = manut_cliente.Nome.text()
    ativo = manut_cliente.CkAtivo.isChecked()
    if not ativo:
        QMessageBox.about(manut_cliente, 'ERRO', f'O Cliente {nome} já está desligado')
    else:
        men = QMessageBox.question(manut_cliente, 'DESLIGAR CLIENTE', f'ATENÇÃO, deseja realmente desligar o cliente {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            banco.desligar_cliente(id)
            QMessageBox.about(manut_cliente, 'CLIENTE DESLIGADO', f'Cliente {nome} desligado com sucesso')
            carrega_clientes()
            manut_cliente.close()
        else:
            return

def reativar_cliente():
    id = manut_cliente.InputId.value()
    nome = manut_cliente.Nome.text()
    ativo = manut_cliente.CkAtivo.isChecked()
    if ativo:
        QMessageBox.about(manut_cliente, 'ERRO', f'O Cliente {nome} já está ativo')
    else:
        men = QMessageBox.question(manut_cliente, 'REATIVAR CLIENTE', f'ATENÇÃO, deseja realmente reativar o cliente {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            banco.reativar_cliente(id)
            QMessageBox.about(manut_cliente, 'CLIENTE REATIVADO', f'Cliente {nome} reativado com sucesso')
            carrega_clientes()
            manut_cliente.close()
        else:
            return


def fidelizar_cliente():
    id = manut_cliente.InputId.value()
    nome = manut_cliente.Nome.text()
    fidelizado = manut_cliente.CkFidelizado.isChecked()
    if fidelizado:
        QMessageBox.about(manut_cliente, 'ERRO', f'O Cliente {nome} já é fidelizado')
    else:
        men = QMessageBox.question(manut_cliente, 'FIDELIZAR CLIENTE', f'ATENÇÃO, deseja realmente FIDELIZAR o cliente {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            banco.fidelizar_cliente(id)
            QMessageBox.about(manut_cliente, 'CLIENTE FIDELIZADO', f'O Cliente {nome} foi fidelizado com sucesso e a partir de agora pode receber os descontos de fidelidade')
            carrega_clientes()
            manut_cliente.close()
        else:
            return

def desfidelizar_cliente():
    id = manut_cliente.InputId.value()
    nome = manut_cliente.Nome.text()
    fidelizado = manut_cliente.CkFidelizado.isChecked()
    if not fidelizado:
        QMessageBox.about(manut_cliente, 'ERRO', f'O Cliente {nome} não é fidelizado')
    else:
        men = QMessageBox.question(manut_cliente, 'DESFIDELIZAR CLIENTE', f'ATENÇÃO, deseja realmente DESFIDELIZAR o cliente {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            banco.desfidelizar_cliente(id)
            QMessageBox.about(manut_cliente, 'CLIENTE DESFIDELIZADO', f'O Cliente {nome} foi desfidelizado e não contará mais com os descontos de fidelidade')
            carrega_clientes()
            manut_cliente.close()
        else:
            return


def alterar_cliente():
    id = manut_cliente.InputId.value()
    nome = manut_cliente.Nome.text().strip().title()
    telefone = manut_cliente.Itelefone.text()
    sexo = manut_cliente.CbSexo.currentText()
    if sexo == 'Selecione um Gênero':
        QMessageBox.about(manut_cliente, 'ERRO', 'Selecione um Gênero')
    else:
        if nome == '' or len(nome)< 5:
            QMessageBox.about(manut_cliente, 'ERRO', 'Campo Nome Não pode ser vazio e precisa pelo menos 5 caracteres')
        elif len(telefone)< 14:
            QMessageBox.about(manut_cliente, 'ERRO', 'Telefone Inválido, pecisa pelo menos 10 digitos')
        else:
            
            banco.alterar_cliente(id,nome,telefone,sexo)
            QMessageBox.about(manut_cliente, 'CLIENTE EDITADO', f'Cliente {nome} foi alterado com sucesso')
            manut_cliente.Nome.setText('')
            manut_cliente.Itelefone.setText('')
            manut_cliente.CbSexo.setCurrentIndex(0)
            carrega_clientes()
            manut_cliente.close()



#FUNÇÕES DE profissionais

def inserir_profissional():
    nome = profissional.Inome.text().strip().title()
    matricula = profissional.Imatricula.text().strip()
    cargo = profissional.Ifuncao.text().strip().title()
    func_banco = banco.busca_func_matricula(matricula)
    if nome == '' or len(nome)< 5:
        QMessageBox.about(profissional, 'ERRO', 'Campo Nome Não pode ser vazio e precisa pelo menos 5 caracteres')
    elif matricula == '' or cargo == '':
        QMessageBox.about(profissional, 'ERRO', 'Nenhum campo deve ficar vazio')
    elif len(func_banco) != 0:
        QMessageBox.about(profissional, 'ERRO', 'Já existe profissional com essa Matricula cadastrada')
    else:
        banco.inserir_funcionario(nome,cargo,matricula)
        QMessageBox.about(profissional, 'PROFISSIONAL CADASTRADO', f'Profissional {nome} cadastrado com sucesso')
        profissional.Inome.setText('')
        profissional.Ifuncao.setText('')
        profissional.Imatricula.setText('')
        carrega_profissionais()

def carrega_profissionais():
    tabela = profissional.TabelaProfissionais
    profissionais = banco.busca_todos_funcionarios_ordem()
    row = 0
    tabela.setRowCount(len(profissionais))
    tabela.setColumnWidth(0, 60)
    tabela.setColumnWidth(1, 350)
    tabela.setColumnWidth(2, 250)
    tabela.setColumnWidth(3, 130)
    tabela.setColumnWidth(4, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in profissionais:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{c[4]}'))
        row += 1
      


def pega_profissional():
    linha = profissional.TabelaProfissionais.currentRow()
    id = int(profissional.TabelaProfissionais.item(linha, 0).text())
    nome = profissional.TabelaProfissionais.item(linha, 1).text()
    cargo = profissional.TabelaProfissionais.item(linha, 2).text()
    matricula = profissional.TabelaProfissionais.item(linha, 3).text()
    status = profissional.TabelaProfissionais.item(linha, 4).text()
    if status == 'Desligado' and usuario1.root == False:
        QMessageBox.about(profissional, 'ERRO', f'Profissional já está desligado, solicite ao root para reativa-lo')
    else:
        manut_profissional.InputId.setValue(id)
        manut_profissional.Inome.setText(nome)
        manut_profissional.Ifuncao.setText(cargo)
        manut_profissional.Imatricula.setText(matricula)
        manut_profissional.show()

def desligar_profissional():
    id = manut_profissional.InputId.value()
    nome = manut_profissional.Inome.text()
    men = QMessageBox.question(manut_profissional, 'DESLIGAR PROFISSIONAL', f'ATENÇÃO, deseja realmente desligar o profissional {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.desligar_funcionario(id)
        QMessageBox.about(manut_profissional, 'PROFISSIONAL DESLIGADO', f'Profissional {nome} desligado com sucesso')
        carrega_profissionais()
        manut_profissional.close()
    else:
        return

def reativar_profissional():
    id = manut_profissional.InputId.value()
    nome = manut_profissional.Inome.text()
    men = QMessageBox.question(manut_profissional, 'REATIVAR PROFISSIONAL', f'ATENÇÃO, deseja realmente reativar o profissional {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.reativar_funcionario(id)
        QMessageBox.about(manut_profissional, 'PROFISSIONAL REATIVADO', f'Profissional {nome} reativado com sucesso')
        carrega_profissionais()
        manut_profissional.close()
    else:
        return


def alterar_profissional():
    id = manut_profissional.InputId.value()
    nome = manut_profissional.Inome.text().strip().title()
    cargo = manut_profissional.Ifuncao.text().strip().title()
    if nome == '' or len(nome)< 5:
        QMessageBox.about(manut_profissional, 'ERRO', 'Campo Nome Não pode ser vazio e precisa pelo menos 5 caracteres')
    elif cargo == '':
        QMessageBox.about(manut_profissional, 'ERRO', 'Cargo Inválido não pode ser vazio')
    else:    
        banco.alterar_funcionario(id,nome,cargo)
        QMessageBox.about(manut_profissional, 'PROFISSIONAL EDITADO', f'Profissional {nome} foi alterado com sucesso')
        manut_profissional.Inome.setText('')
        manut_profissional.Ifuncao.setText('')
        carrega_profissionais()
        manut_profissional.close()


#FUNÇÕES DE SERVIÇOS

def inserir_fpag():
    descricao = fpag.InputNome.text().strip().title()
    if descricao == '':
        QMessageBox.about(fpag, 'ERRO', 'Campo não pode ficar vazio')
    else:
        banco.inserir_fpag(descricao)
        QMessageBox.about(fpag, 'FORMA DE PAGAMENTO CADASTRADA', f'Forma de pagamento {descricao} cadastrada com sucesso')
        fpag.InputNome.setText('')
        carrega_fpags()

def carrega_fpags():
    tabela = fpag.TabelaFpag
    f_pag = banco.busca_todos_fpags()
    row = 0
    tabela.setRowCount(len(f_pag))
    tabela.setColumnWidth(0, 100)
    tabela.setColumnWidth(1, 400)
    tabela.setColumnWidth(2, 150)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in f_pag:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        row += 1
      
    


def pega_fpag():
    linha = fpag.TabelaFpag.currentRow()
    id = int(fpag.TabelaFpag.item(linha, 0).text())
    descricao = fpag.TabelaFpag.item(linha, 1).text()
    status = fpag.TabelaFpag.item(linha, 2).text()
    if status == 'Desligado' and usuario1.root == False:
        QMessageBox.about(fpag, 'ERRO', f'Forma de pagamento já está desligada, solicite ao root para reativa-la')
    else:
        manut_fpag.InputId.setValue(id)
        manut_fpag.Nome.setText(descricao)
        manut_fpag.show()

def desligar_fpag():
    codigo = manut_fpag.InputId.value()
    nome = manut_fpag.Nome.text()
    men = QMessageBox.question(manut_fpag, 'DESLIGAR FORMA DE PAGAMENTO', f'ATENÇÃO, deseja realmente desligar a forma de pagamento {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.desligar_fpag(codigo)
        QMessageBox.about(manut_fpag, 'FORMA DE PAGAMENTO DESLIGADO', f'Forma de pagamento {nome} desligada com sucesso')
        carrega_fpags()
        manut_fpag.close()
    else:
        return


def reativar_fpag():
    codigo = manut_fpag.InputId.value()
    nome = manut_fpag.Nome.text()
    men = QMessageBox.question(manut_fpag, 'REATIVAR FORMA DE PAGAMENTO', f'ATENÇÃO, deseja realmente reativar a forma de pagamento {nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.reativar_fpag(codigo)
        QMessageBox.about(manut_fpag, 'FORMA DE PAGAMENTO REATIVADO', f'Forma de pagamento {nome} reativada com sucesso')
        carrega_fpags()
        manut_fpag.close()
    else:
        return

def alterar_fpag():
    codigo = manut_fpag.InputId.value()
    nome = manut_fpag.Nome.text().strip().title()
    if nome == '':
        QMessageBox.about(manut_fpag, 'ERRO', 'Campo não pode ficar vazio')
    else:
        banco.alterar_fpag(codigo, nome)
        QMessageBox.about(fpag, 'FORMA DE PAGAMENTO ALTERADO', f'Forma de pagamento {nome} alterada com sucesso')
        manut_fpag.Nome.setText('')
        manut_fpag.close()
        carrega_fpags()



def carrega_tabelas():
    carrega_usuarios()
    carrega_servicos()
    carrega_clientes()
    carrega_profissionais()
    carrega_fpags()



#FUNÇÕES DE NOTAS FISCAIS
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
    if len(preco_servico) != 0:
        preco = float(preco_servico[0][0])
        nf.InputPtab.setValue(preco)
        nf.InputPfat.setValue(preco)
        calcular_desconto()    

def busca_preco_manut():
    id = manut_nf.comboServicos.currentData()
    preco_servico = banco.buscar_preco_id(id)
    if len(preco_servico) != 0:
        preco = float(preco_servico[0][0])
        manut_nf.InputPtab.setValue(preco)
        manut_nf.InputPfat.setValue(preco)
        calcular_desconto_manut()    

def cliente_nf_combo():
    nf.comboClientes.clear()
    clientes = banco.busca_todos_clientes_combo_ativos()
    for c in clientes:
        nf.comboClientes.addItem(f"{c[1]}", QVariant(c[0]))
    #nf.show()

def servico_nf_combo():
    nf.comboServicos.clear()
    servicos = banco.busca_todos_servicos_ativos()
    for c in servicos:
        nf.comboServicos.addItem(f"{c[1]}", QVariant(c[0]))
    #nf.show()


def profi_nf_combo():
    nf.comboProfi.clear()
    profi = banco.busca_todos_funcionarios_combo_ativos()
    for c in profi:
        nf.comboProfi.addItem(f"{c[1]} -> {c[2]}", QVariant(c[0]))
    #nf.show()

def fpag_nf_combo():
    nf.comboFpag.clear()
    fpags = banco.busca_todos_fpags_ativas()
    for c in fpags:
        nf.comboFpag.addItem(f"{c[1]}", QVariant(c[0]))
    #nf.show()


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
    nf.lbl_total.setText('')
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
        #vendas.lbl_escolha.setText('')

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
    nf.show()

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
    cliente = nf_cliente.comboClientes.currentText()
    vendas.lbl_escolha.setText(f'Cliente selecionado : {cliente}')
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


#### notas por data de emissão
def carrega_todas_nfs_dtemissao():
    data = nf_data.InputData.text()
    vendas.lbl_escolha.setText(f'Data de emissão selecionada: {data}')
    vendas.lbl_total.setText(f'')
    dtemissão = funcoes.data_banco2(data)
    tabela = vendas.TabelaNfs
    row = 0
    nfs=banco.buscar_nf_data(dtemissão)
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
    carrega_nfs_emitidas_dtemissao()
    carrega_nfs_pendentes_dtemissao()
    carrega_nfs_canceladas_dtemissao()
    nf_data.close()

def carrega_nfs_emitidas_dtemissao():
    data = nf_data.InputData.text()
    vendas.lbl_escolha.setText(f'Data de emissão selecionada: {data}')
    vendas.lbl_total_emitidas.setText(f'')
    dtemissão = funcoes.data_banco2(data)
    row = 0
    nfs = banco.busca_nf_data_status(dtemissão, 'Emitida')
    tabela = vendas.TabelaEmitidas
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

def carrega_nfs_pendentes_dtemissao():
    data = nf_data.InputData.text()
    vendas.lbl_escolha.setText(f'Data de emissão selecionada: {data}')
    vendas.lbl_total_pendentes.setText(f'')
    dtemissão = funcoes.data_banco2(data)
    tabela = vendas.TabelaPendentes
    row = 0
    nfs = banco.busca_nf_data_status(dtemissão, 'Pendente')
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


def carrega_nfs_canceladas_dtemissao():
    data = nf_data.InputData.text()
    vendas.lbl_escolha.setText(f'Data de emissão selecionada: {data}')
    vendas.lbl_total_canceladas.setText(f'')
    dtemissão = funcoes.data_banco2(data)
    tabela = vendas.TabelaCanceladas
    row = 0
    nfs = banco.busca_nf_data_status(dtemissão, 'Cancelada')
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
    #vendas.lbl_escolha.setText('')
    #cliente = nf_cliente.comboClientes.currentText()
    #vendas.lbl_escolha.setText(f'Cliente selecionado : {cliente}')
    pass

def escrever_data():
    vendas.lbl_escolha.setText('')
    carrega_todas_nfs_dtemissao()

def carrega_tabelas_nf():
    vendas.lbl_escolha.setText('Busca Todas as Notas fiscais (últimas 50 nfs ordem decrescente)')
    carrega_todas_nfs()
    carrega_nfs_emitidas()
    carrega_nfs_pendentes()
    carrega_nfs_canceladas()
    vendas.show()

def rb_todas_nfs():
    vendas.lbl_escolha.setText('Busca Todas as Notas fiscais (últimas 50 nfs ordem decrescente)')
    carrega_tabelas_nf()



def abrir_consulta_cliente():
    nf_cliente.comboClientes.clear()
    clientes = banco.busca_todos_clientes_combo()
    for c in clientes:
        nf_cliente.comboClientes.addItem(f'{c[1]}', QVariant(c[0]))
    nf_cliente.show()


def consulta_intervalo_datas():
    data_inicial = intervalo_datas.DataInicial.text()
    data_final = intervalo_datas.DataFinal.text()
    data_inicial = funcoes.data_banco(data_inicial)
    data_final = funcoes.data_banco(data_final)
    maior_data = funcoes.inicial_maior_final(data_inicial, data_final)
    if not maior_data:
        QMessageBox.about(intervalo_datas, 'ERRO', 'Data inicial deve ser menor ou igual a final')
    else:
        vendas.lbl_escolha.setText(f'Consulta notas entre os dias {funcoes.banco_data(data_inicial)} e {funcoes.banco_data(data_final)}')
        carrega_nfs_intervalo_datas()
        carrega_nfs_emitidas_intervalo_datas()
        carrega_nfs_pendentes_intervalo_datas()
        carrega_nfs_canceladas_intervalo_datas()
        intervalo_datas.close()




def carrega_nfs_intervalo_datas():
    data_inicial = intervalo_datas.DataInicial.text()
    data_final = intervalo_datas.DataFinal.text()
    data_inicial = funcoes.data_banco(data_inicial)
    data_final = funcoes.data_banco(data_final)
    tabela = vendas.TabelaNfs
    row = 0
    nfs = banco.busca_nf_intervalo_datas(data_inicial, data_final)
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


def carrega_nfs_emitidas_intervalo_datas():
    data_inicial = intervalo_datas.DataInicial.text()
    data_final = intervalo_datas.DataFinal.text()
    data_inicial = funcoes.data_banco(data_inicial)
    data_final = funcoes.data_banco(data_final)
    tabela = vendas.TabelaEmitidas
    row = 0
    status = 'Emitida'
    nfs = banco.busca_nf_intervalo_datas_status(data_inicial, data_final, status)
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


def carrega_nfs_pendentes_intervalo_datas():
    data_inicial = intervalo_datas.DataInicial.text()
    data_final = intervalo_datas.DataFinal.text()
    data_inicial = funcoes.data_banco(data_inicial)
    data_final = funcoes.data_banco(data_final)
    tabela = vendas.TabelaPendentes
    row = 0
    status = 'Pendente'
    nfs = banco.busca_nf_intervalo_datas_status(data_inicial, data_final, status)
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


def carrega_nfs_canceladas_intervalo_datas():
    data_inicial = intervalo_datas.DataInicial.text()
    data_final = intervalo_datas.DataFinal.text()
    data_inicial = funcoes.data_banco(data_inicial)
    data_final = funcoes.data_banco(data_final)
    tabela = vendas.TabelaCanceladas
    row = 0
    status = 'Cancelada'
    nfs = banco.busca_nf_intervalo_datas_status(data_inicial, data_final, status)
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


def consulta_intervalo_notas():
    nota_inicial = intervalo_nf.NotaInicial.value()
    nota_final = intervalo_nf.NotaFinal.value()
    if nota_inicial > nota_final:
        QMessageBox.about(intervalo_nf, 'ERRO', 'Nota inicial deve ser menor ou igual a final')
    else:
        vendas.lbl_escolha.setText(f'Consulta notas entre {nota_inicial} e {nota_final}')
        carrega_nf_intervalo_notas()
        carrega_nf_emitidas_intervalo_notas()
        carrega_nf_pendentes_intervalo_notas()
        carrega_nf_canceladas_intervalo_notas()
        intervalo_nf.close()

def carrega_nf_intervalo_notas():
    nota_inicial = intervalo_nf.NotaInicial.value()
    nota_final = intervalo_nf.NotaFinal.value()
    tabela = vendas.TabelaNfs
    row = 0
    nfs = banco.busca_nf_intervalo_notas(nota_inicial, nota_final)
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


def carrega_nf_emitidas_intervalo_notas():
    nota_inicial = intervalo_nf.NotaInicial.value()
    nota_final = intervalo_nf.NotaFinal.value()
    tabela = vendas.TabelaEmitidas
    row = 0
    status = 'Emitida'
    nfs = banco.busca_nf_intervalo_notas_status(nota_inicial, nota_final, status)
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
    
def carrega_nf_pendentes_intervalo_notas():
    nota_inicial = intervalo_nf.NotaInicial.value()
    nota_final = intervalo_nf.NotaFinal.value()
    tabela = vendas.TabelaPendentes
    row = 0
    status = 'Pendente'
    nfs = banco.busca_nf_intervalo_notas_status(nota_inicial, nota_final, status)
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

def carrega_nf_canceladas_intervalo_notas():
    nota_inicial = intervalo_nf.NotaInicial.value()
    nota_final = intervalo_nf.NotaFinal.value()
    tabela = vendas.TabelaCanceladas
    row = 0
    status = 'Cancelada'
    nfs = banco.busca_nf_intervalo_notas_status(nota_inicial, nota_final, status)
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
            #print('hora menor')
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
        manut_ag.show()


def pega_agenda():
    linha = agenda.TabelaAgendaProfi.currentRow()
    id_agenda = agenda.TabelaAgendaProfi.item(linha, 8).text()
    data = agenda.TabelaAgendaProfi.item(linha, 0).text()
    hora = agenda.TabelaAgendaProfi.item(linha, 1).text()
    cliente = agenda.TabelaAgendaProfi.item(linha, 3).text()
    tele = agenda.TabelaAgendaProfi.item(linha, 4).text()
    status = agenda.TabelaAgendaProfi.item(linha, 7).text()
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
        manut_ag.show()

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
    data_ag = agenda.TabelaAgenda.item(linha, 0).text()
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

    qt = QtWidgets.QApplication(sys.argv)
    
    usuario1 = Usuarios()
    menu = uic.loadUi('telas_duda/menu2.ui')
    menu_cadastros = uic.loadUi('telas_duda/menu_cadastros.ui')
    menu_vendas = uic.loadUi('menu_vendas_faturamento.ui')
    menu_estat = uic.loadUi('menu_estatisticas.ui')
    login = uic.loadUi('telas_duda/tela_login.ui')
    cad_usuario = uic.loadUi('telas_duda/tela_cadastro.ui')
    manut_usuarios = uic.loadUi('telas_duda/manutencao_usuarios.ui')
    permissoes = uic.loadUi('telas_duda/permissoes_usuarios.ui')

    #TELAS SERVIÇOS
    servico = uic.loadUi('telas_duda/servicos.ui')
    manut_servico = uic.loadUi('telas_duda/manut_servico.ui')

    #TELAS clienteS
    cliente = uic.loadUi('telas_duda/clientes.ui')
    manut_cliente = uic.loadUi('telas_duda/manut_cliente.ui')

    #TELAS profissionais
    profissional = uic.loadUi('telas_duda/profissionais.ui')
    manut_profissional = uic.loadUi('telas_duda/manut_profissional.ui')

    #TELAS FPAGS
    fpag = uic.loadUi('telas_duda/fpag.ui')
    manut_fpag = uic.loadUi('telas_duda/manut_fpag.ui')


    #TELAS NF
    nf = uic.loadUi('telas_duda/emissao_nf.ui')
    vendas = uic.loadUi('telas_duda/vendas.ui')
    manut_nf = uic.loadUi('telas_duda/manut_nf.ui')
    nf_cliente = uic.loadUi('telas_duda/nf_por_cliente.ui')
    nf_data = uic.loadUi('nf_por_data.ui')
    intervalo_datas = uic.loadUi('telas_duda/nf_por_intervalo_de_data.ui')
    intervalo_nf = uic.loadUi('telas_duda/nf_por_intervalo_de_notas.ui')
    

    #TELAS ESTATISTICAS
    estatisitcas = uic.loadUi('telas_duda/estatisticas.ui')
    data_estat = uic.loadUi('estatisticas_por_intervalo_de_data.ui')

    #TELAS AGENDA
    agenda = uic.loadUi('agenda.ui')
    ag = uic.loadUi('agendamento.ui')
    manut_ag = uic.loadUi('manut_agendamento.ui')
    manut_pendente = uic.loadUi('manut_agenda.ui')

    ##BOTÕES MENU
    menu.Btn_Sair.clicked.connect(menu.close)
    menu.Btn_Mudar_usuario.clicked.connect(abrir_tela_login)
    menu.Btn_cadastro.clicked.connect(menu_cadastros.show)
    menu.Btn_faturamento.clicked.connect(menu_vendas.show)
    menu.Btn_estatisticas.clicked.connect(menu_estat.show)
    menu.Btn_agenda.clicked.connect(inicializar_agenda)
    menu_cadastros.Btn_cadastro_usuario.clicked.connect(abrir_cria_usuario)
    menu_cadastros.Btn_cadastro_servico.clicked.connect(servico.show)
    menu_cadastros.Btn_cadastro_cliente.clicked.connect(cliente.show)
    menu_cadastros.Btn_cadastro_funcionario.clicked.connect(profissional.show)
    menu_cadastros.Btn_cadastro_fpag.clicked.connect(fpag.show)
    menu_vendas.Btn_Vendas.clicked.connect(carrega_tabelas_nf)
    menu_vendas.Btn_nova_venda.clicked.connect(carrega_combos_nf)
    menu_estat.Btn_Estatisticas_realizado.clicked.connect(carrega_tabelas_estatisticas)
    menu_estat.Btn_Estatisticas_futuro.clicked.connect(teste)
    ##

    #BOTÕES SERVIÇOS
    servico.BtnInserir.clicked.connect(inserir_servico)
    servico.TabelaServicos.doubleClicked.connect(pega_servico)
    manut_servico.BtnSair.clicked.connect(manut_servico.close)
    manut_servico.BtnDesligar.clicked.connect(desligar_servico)
    manut_servico.BtnReativar.clicked.connect(reativar_servico)
    manut_servico.BtnAlterar.clicked.connect(alterar_servico)


    #BOTÕES clienteS
    cliente.BtnInserir.clicked.connect(inserir_cliente)
    cliente.TabelaClientes.doubleClicked.connect(pega_cliente)
    manut_cliente.BtnSair.clicked.connect(manut_cliente.close)
    manut_cliente.BtnDesligar.clicked.connect(desligar_cliente)
    manut_cliente.BtnReativar.clicked.connect(reativar_cliente)
    manut_cliente.BtnFidelizar.clicked.connect(fidelizar_cliente)
    manut_cliente.BtnDesfidelizar.clicked.connect(desfidelizar_cliente)
    manut_cliente.BtnAlterar.clicked.connect(alterar_cliente)

    ##############

    #BOTÕES profissionais
    profissional.BtnInserir.clicked.connect(inserir_profissional)
    profissional.TabelaProfissionais.doubleClicked.connect(pega_profissional)
    manut_profissional.BtnSair.clicked.connect(manut_profissional.close)
    manut_profissional.BtnDesligar.clicked.connect(desligar_profissional)
    manut_profissional.BtnReativar.clicked.connect(reativar_profissional)
    manut_profissional.BtnAlterar.clicked.connect(alterar_profissional)

    #BOTÕES USUÁRIOS



    login.BtnEntrar.clicked.connect(fazer_login)
    cad_usuario.BtnCadastrar.clicked.connect(criar_novo_usuario)
    cad_usuario.BtnLogin.clicked.connect(abrir_tela_login)
    cad_usuario.BtnPermissao.clicked.connect(permissao)
    manut_usuarios.BtnVoltar.clicked.connect(manut_usuarios.close)
    manut_usuarios.BtnOrdenar.clicked.connect(carrega_usuario_asc)
    manut_usuarios.BtnOrdenarID.clicked.connect(carrega_usuarios)
    manut_usuarios.TabelaUsuarios.doubleClicked.connect(pega_usuario)
    manut_usuarios.TabelaUsuarios.setSortingEnabled(True)
    tabela = manut_usuarios.TabelaUsuarios
    permissoes.BtnCancelar.clicked.connect(permissoes.close)
    permissoes.BtnSetar.clicked.connect(setar_permissoes)

    ##############

    #BOTÕES FPAGS
    fpag.BtnInserir.clicked.connect(inserir_fpag)
    fpag.TabelaFpag.doubleClicked.connect(pega_fpag)
    manut_fpag.BtnSair.clicked.connect(manut_fpag.close)
    manut_fpag.BtnDesligar.clicked.connect(desligar_fpag)
    manut_fpag.BtnReativar.clicked.connect(reativar_fpag)
    manut_fpag.BtnAlterar.clicked.connect(alterar_fpag)

    ##############

    #BOTÕES NF
    vendas.BtnNVenda.clicked.connect(carrega_combos_nf)
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
    manut_nf.BtnCalcularNf.clicked.connect(finalizar_nf_manut)
    ##############

    #BOTÕES ESTATÍSTICAS
    estatisitcas.RbIntervaloDatas.clicked.connect(data_estat.show)
    estatisitcas.RbTodas.clicked.connect(carrega_tabelas_estatisticas)
    data_estat.DataInicial.setDate(data_atual)
    data_estat.DataFinal.setDate(data_atual)
    data_estat.BtnConfirmar.clicked.connect(verificar_intervalo)
    ##############

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


    #menu.showMaximized()
    login.show()
    banco.cria_tabelas()
    qt.exec_()