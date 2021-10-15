import sqlite3
import sys
from PyQt5 import uic, QtWidgets
import banco
from PyQt5.QtWidgets import QMessageBox
from datetime import date, datetime
from classes import Usuarios

def teste():
    print('Tudo OK')

data_atual = date.today()


#FUNÇÕES PARA TELA LOGIN
def fazer_login():
    usuario = login.InputUsuario.text().upper()
    senha = login.InputSenha.text()
    usuario_banco = banco.buscar_usuario(usuario)
    if usuario != "ROOT":
        usuario1.banco_para_modelo(usuario_banco)
    if usuario == 'ROOT' and senha == 'manager':
        login.close()
        abrir_cria_usuario()
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
            menu.lbl_ola.setText(f'Seja bem vindo usuário {usuario1.nome}')
            #menu.lbl_id_user.setText(f'{usuario1.id}')
            menu.showMaximized()
            QMessageBox.about(menu, 'BOAS VINDAS', f'Bem vindo usuário {usuario1.nome}, você possui as seguintes permissões: {permi}')
            banco.cria_tabelas()
            #carrega_tabelas()

def abrir_cria_usuario():
    if usuario1.root:
        login.close()
        cad_usuario.CbCriar.setVisible(False)
        cad_usuario.CbEditar.setVisible(False)
        cad_usuario.CbExcluir.setVisible(False)
        cad_usuario.CbRoot.setVisible(False)
        cad_usuario.show()    
    else:
        erro_sem_permissao()

##############################

#FUNÇÕES PARA CRIAÇÃO DE USUÁRIOS

def abrir_tela_login():
    cad_usuario.close()
    menu.close()
    login.InputUsuario.setText('')
    login.InputSenha.setText('')
    login.show()

def criar_novo_usuario():
    usuario = cad_usuario.InputUsuario.text().upper().strip()
    senha = cad_usuario.InputSenha.text()
    confirma = cad_usuario.InputConfirmar.text()
    criar = cad_usuario.CbCriar.isChecked()
    editar = cad_usuario.CbEditar.isChecked()
    excluir = cad_usuario.CbExcluir.isChecked()
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
        cad_usuario.CbCriar.setChecked(False)
        cad_usuario.CbEditar.setChecked(False)
        cad_usuario.CbExcluir.setChecked(False)
        novo_usuario = banco.buscar_usuario(usuario)
        id_usuario = str(novo_usuario[0][0])
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
    manut_usuarios.show()
    

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
    print(usuario1.root)








if __name__ == '__main__':

    qt = QtWidgets.QApplication(sys.argv)
    
    usuario1 = Usuarios()
    menu = uic.loadUi('menu2.ui')
    menu_cadastros = uic.loadUi('menu_cadastros.ui')
    login = uic.loadUi('tela_login.ui')
    cad_usuario = uic.loadUi('tela_cadastro.ui')
    manut_usuarios = uic.loadUi('manutencao_usuarios.ui')
    permissoes = uic.loadUi('permissoes_usuarios.ui')
    
    ##menu2
    menu.Btn_Sair.clicked.connect(menu.close)
    menu.Btn_Mudar_usuario.clicked.connect(abrir_tela_login)
    menu.Btn_cadastro.clicked.connect(menu_cadastros.show)
    menu_cadastros.Btn_cadastro_usuario.clicked.connect(abrir_cria_usuario)
    menu_cadastros.Btn_cadastro_servico.clicked.connect(teste)
    menu_cadastros.Btn_cadastro_cliente.clicked.connect(teste)
    menu_cadastros.Btn_cadastro_funcionario.clicked.connect(teste)
    ##


    #USUÁRIOS



    login.BtnEntrar.clicked.connect(fazer_login)
    cad_usuario.BtnCadastrar.clicked.connect(criar_novo_usuario)
    cad_usuario.BtnLogin.clicked.connect(abrir_tela_login)
    cad_usuario.BtnPermissao.clicked.connect(carrega_usuarios)
    manut_usuarios.BtnVoltar.clicked.connect(manut_usuarios.close)
    manut_usuarios.BtnOrdenar.clicked.connect(carrega_usuario_asc)
    manut_usuarios.BtnOrdenarID.clicked.connect(carrega_usuarios)
    manut_usuarios.TabelaUsuarios.doubleClicked.connect(pega_usuario)
    manut_usuarios.TabelaUsuarios.setSortingEnabled(True)
    tabela = manut_usuarios.TabelaUsuarios
    permissoes.BtnCancelar.clicked.connect(permissoes.close)
    permissoes.BtnSetar.clicked.connect(setar_permissoes)

    ##############

    #menu.showMaximized()
    login.show()
    banco.cria_tabelas()
    qt.exec_()