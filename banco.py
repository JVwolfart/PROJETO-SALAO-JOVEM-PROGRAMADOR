from os import truncate
import sqlite3
from sqlite3.dbapi2 import Cursor
from datetime import date



#data_atual = datetime.datetime.now()
data_atual = date.today()

#########USUÁRIOS

def criar_usuario():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS usuarios(nome TEXT, senha TEXT, faturamento BOOLEAN, estatistica BOOLEAN, agenda BOOLEAN, root BOOLEAN)'
    cur.execute(sql)
    banco.commit()
    banco.close()

def buscar_usuario(nome):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql= "SELECT rowid, * FROM usuarios WHERE nome=?"
    cur.execute(sql, (nome,))
    return cur.fetchall()
    #banco.commit()

def novo_usuario(nome, senha, faturamento, estatistica, agenda, root=False):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "INSERT INTO usuarios VALUES(?,?,?,?,?,?)"
    cur.execute(sql, (nome,senha,faturamento,estatistica,agenda,root))
    #cur.execute(f"INSERT INTO usuarios VALUES('{nome}','{senha}', {criar}, {editar}, {excluir}, {root})")
    banco.commit()
    banco.close()

def alterar_permissoes(nome, faturamento, estatistica, agenda, root):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "UPDATE usuarios SET faturamento=?, estatistica=?, agenda=?, root=? WHERE nome=?"
    cur.execute(sql, (faturamento,estatistica,agenda,root,nome))
    #cur.execute(f"UPDATE usuarios SET criar={criar}, editar={editar}, excluir={excluir}, root={root} WHERE nome='{nome}'")
    banco.commit()
    banco.close()

def buscar_todos_usuarios():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "SELECT rowid, * FROM usuarios"
    cur.execute(sql)
    return cur.fetchall()
    #banco.commit()

def buscar_todos_usuarios_asc():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "SELECT rowid, * FROM usuarios ORDER BY nome ASC"
    cur.execute(sql)
    return cur.fetchall()
    #banco.commit()

def busca_permissoes(nome):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "SELECT faturamento, estatistica, agenda, root FROM usuarios WHERE nome=?"
    cur.execute(sql, (nome,))
    #cur.execute(f"SELECT criar, editar, excluir, root FROM usuarios WHERE nome='{nome}'")
    permissoes = cur.fetchone()
    autorizacoes = []
    for k, c in enumerate(permissoes):
        if k == 0 and c == 1:
            autorizacoes.append('Faturamento')
        if k == 1 and c == 1:
            autorizacoes.append('Estatistica')
        if k == 2 and c == 1:
            autorizacoes.append('Agenda')
        if k == 3 and c == 1:
            autorizacoes.append('Root')
    if len(autorizacoes) == 0:
        autorizacoes.append('Você não possui permissões liberadas, conseguirá apenas acessar algumas funcionalidades do menu de cadastros. Caso queira outras permissões solicite ao administrador')
    return autorizacoes
    #banco.commit()

#####

#FORMAS DE PAGAMENTO
def cria_tb_fpag():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS fpag (Id_fpag	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Fpag_name TEXT, Status_fpag TEXT)'
    cur.execute(sql)
    banco.commit()
    banco.close()

def busca_todos_fpags():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM fpag'
    cur.execute(sql)
    return cur.fetchall()


def busca_todos_fpags_ativas(status='Ativo'):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM fpag WHERE Status_fpag=? ORDER BY Fpag_name'
    cur.execute(sql, (status,))
    return cur.fetchall()


def inserir_fpag(fpag, status='Ativo'):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'INSERT INTO fpag VALUES (?, ?, ?)'
    cur.execute(sql, (None, fpag, status))
    banco.commit()
    banco.close()

def alterar_fpag(id, fpag):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "UPDATE fpag SET Fpag_name=? WHERE Id_fpag=?"
    cur.execute(sql,(fpag, id))
    banco.commit()
    banco.close()

def desligar_fpag(id, status='Desligado'):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "UPDATE fpag SET Status_fpag=? WHERE Id_fpag=?"
    cur.execute(sql,(status, id))
    banco.commit()
    banco.close()

def reativar_fpag(id, status='Ativo'):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "UPDATE fpag SET Status_fpag=? WHERE Id_fpag=?"
    cur.execute(sql,(status, id))
    banco.commit()
    banco.close()

#########

#FUNCIONÁRIOS

def criar_tb_funcionario():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS funcionarios (Id_func	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Nome TEXT, Cargo TEXT, Matricula TEXT, Status_func TEXT)'
    cur.execute(sql)
    banco.commit()
    banco.close()


def inserir_funcionario(nome, cargo, matricula, status='Ativo'):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'INSERT INTO funcionarios VALUES ( ?, ?, ?, ?, ?)'
    cur.execute(sql, (None, nome, cargo, matricula, status))
    banco.commit()
    banco.close()

def busca_func_matricula(matricula):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM funcionarios WHERE matricula = ?'
    cur.execute(sql, (matricula,))
    return cur.fetchall()

def busca_func_id(id):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM funcionarios WHERE Id_func = ?'
    cur.execute(sql, (id,))
    return cur.fetchall()


def busca_func_nome(nome):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM funcionarios WHERE Nome = ?'
    cur.execute(sql, (nome,))
    return cur.fetchall()
    
def busca_todos_funcionarios():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM funcionarios'
    cur.execute(sql)
    return cur.fetchall()

def busca_todos_funcionarios_ordem():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM funcionarios ORDER BY Nome'
    cur.execute(sql)
    return cur.fetchall()

def busca_todos_funcionarios_combo():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM funcionarios ORDER BY funcionarios.Nome'
    cur.execute(sql)
    return cur.fetchall()

def busca_todos_funcionarios_combo_ativos():
    status = 'Ativo'
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM funcionarios WHERE Status_func=? ORDER BY funcionarios.Nome'
    cur.execute(sql, (status, ))
    return cur.fetchall()
    
def alterar_funcionario(id, nome, cargo):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE funcionarios SET Nome=?, Cargo=? WHERE Id_func=?'
    cur.execute(sql, (nome, cargo, id))
    banco.commit()
    banco.close()

def desligar_funcionario(id, status='Desligado'):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE funcionarios SET Status_func=? WHERE Id_func=?'
    cur.execute(sql, (status, id))
    banco.commit()
    banco.close()

def reativar_funcionario(id, status='Ativo'):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE funcionarios SET Status_func=? WHERE Id_func=?'
    cur.execute(sql, (status, id))
    banco.commit()
    banco.close()

############

#CLIENTES

def criar_tb_clientes():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS clientes (Id_cliente	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Nome TEXT, Telefone TEXT, Sexo TEXT, Status_cliente TEXT, Fidelizado BOOLEAN)'
    cur.execute(sql)
    banco.commit()
    banco.close()


def inserir_cliente(nome, fone, sexo, status='Ativo', fidelizado=False):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?)'
    cur.execute(sql, (None, nome, fone, sexo, status, fidelizado))
    banco.commit()
    banco.close()

def busca_cliente_nome(nome):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM clientes WHERE Nome = ?'
    cur.execute(sql, (nome,))
    return cur.fetchall()

def busca_cliente_id(id):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM clientes WHERE Id_cliente = ?'
    cur.execute(sql, (id,))
    return cur.fetchall()

def busca_todos_clientes():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM clientes'
    cur.execute(sql)
    return cur.fetchall()

def busca_todos_clientes_ordem():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM clientes ORDER BY nome'
    cur.execute(sql)
    return cur.fetchall()

def busca_todos_clientes_combo():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM clientes ORDER BY clientes.Nome'
    cur.execute(sql)
    return cur.fetchall()

def busca_todos_clientes_combo_ativos():
    status = 'Ativo'
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM clientes WHERE Status_cliente=? ORDER BY clientes.Nome'
    cur.execute(sql, (status, ))
    return cur.fetchall()

def busca_fidelidade_cliente(id):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Fidelizado FROM clientes WHERE id_cliente=? '
    cur.execute(sql, (id, ))
    return cur.fetchone()

def alterar_cliente(id, nome, fone, sexo):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE clientes SET Nome=?, Telefone=?, Sexo=? WHERE Id_cliente=?'
    cur.execute(sql, (nome, fone, sexo, id))
    banco.commit()
    banco.close()
######CONFERIDO ATÉ AQUI


def desligar_cliente(id, status='Desligado'):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE clientes SET Status_cliente=? WHERE Id_cliente=?'
    cur.execute(sql, (status, id))
    banco.commit()
    banco.close()


def fidelizar_cliente(id, fidelizado=True):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE clientes SET Fidelizado=? WHERE Id_cliente=?'
    cur.execute(sql, (fidelizado, id))
    banco.commit()
    banco.close()

def desfidelizar_cliente(id, fidelizado=False):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE clientes SET Fidelizado=? WHERE Id_cliente=?'
    cur.execute(sql, (fidelizado, id))
    banco.commit()
    banco.close()


def reativar_cliente(id, status='Ativo'):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE clientes SET Status_cliente=? WHERE Id_cliente=?'
    cur.execute(sql, (status, id))
    banco.commit()
    banco.close()

def fidelizar_cliente(id, fidelizado=True):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE clientes SET Fidelizado=? WHERE Id_cliente=?'
    cur.execute(sql, (fidelizado, id))
    banco.commit()
    banco.close()

def desfidelizar_cliente(id, fidelizado=False):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE clientes SET Fidelizado=? WHERE Id_cliente=?'
    cur.execute(sql, (fidelizado, id))
    banco.commit()
    banco.close()   

#############

#SERVIÇOS E PRODUTOS 

def criar_tb_servicos():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS servicos (Codigo	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Nome TEXT, Valor REAL, Tempo_medio INTERGER, Status_servico TEXT)'
    cur.execute(sql)
    banco.commit()
    banco.close()


def inserir_servico(nome, valor, tempo, status='Ativo'):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'INSERT INTO servicos VALUES (?, ?, ?, ?, ?)'
    cur.execute(sql, (None, nome, valor, tempo, status))
    banco.commit()
    banco.close()

def busca_servico_nome(nome):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM servicos WHERE Nome = ? ORDER BY Nome'
    cur.execute(sql, (nome,))
    return cur.fetchall()

def buscar_preco_id(id):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Valor FROM servicos WHERE Codigo = ?'
    cur.execute(sql, (id,))
    return cur.fetchall()


def busca_todos_servicos():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM servicos ORDER BY servicos.Nome'
    cur.execute(sql)
    return cur.fetchall()

def busca_todos_servicos_ativos():
    status = 'Ativo'
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM servicos WHERE Status_servico=? ORDER BY servicos.Nome'
    cur.execute(sql, (status, ))
    return cur.fetchall()

def alterar_servico(codigo, nome, valor, tempo):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE servicos SET Nome=?, Valor=?, Tempo_medio=? WHERE Codigo=?'
    cur.execute(sql, (nome, valor, tempo, codigo))
    banco.commit()
    banco.close()

def desligar_servico(codigo, status='Desligado'):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE servicos SET Status_servico=? WHERE Codigo=?'
    cur.execute(sql, (status, codigo))
    banco.commit()
    banco.close()

def reativar_servico(codigo, status='Ativo'):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE servicos SET Status_servico=? WHERE Codigo=?'
    cur.execute(sql, (status, codigo))
    banco.commit()
    banco.close()


def busca_tempo_servico_codigo(codigo):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Tempo_medio FROM servicos WHERE Codigo = ?'
    cur.execute(sql, (codigo,))
    return cur.fetchall()

############

#NOTAS FISCAIS

def criar_tb_notas():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS Nfiscais (Nf_num	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Data	DATE, Id_cliente	INTEGER, Valor	REAL, Status	TEXT, Desconto_fidelidade	BOOLEAN, FOREIGN KEY(Id_cliente) REFERENCES clientes(Id_cliente))'
    cur.execute(sql)
    banco.commit()
    banco.close()


def proxima_nf():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT MAX(Nf_num) FROM Nfiscais'
    cur.execute(sql)
    return cur.fetchone()

def busca_nf(nf):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Nf_num, Data, Nfiscais.Id_cliente, Nome, Valor, Desconto_fidelidade, Status  FROM Nfiscais LEFT JOIN clientes ON Nfiscais.Id_cliente = clientes.Id_cliente WHERE Nf_num=?'
    cur.execute(sql, (nf,))
    return cur.fetchone()

def gravar_nf(id_cliente, valor=0, status='Pendente', desconto=False):
    cria_tabelas()
    global data_atual
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'INSERT INTO Nfiscais VALUES (?, ?, ?, ?, ?, ?)'
    cur.execute(sql, (None, data_atual, id_cliente, valor, status, desconto))
    banco.commit()
    banco.close()

def busca_todas_notas():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Nf_num, Data, Nfiscais.Id_cliente, Nome, Valor, Desconto_fidelidade, Status  FROM Nfiscais LEFT JOIN clientes ON Nfiscais.Id_cliente = clientes.Id_cliente ORDER BY Nf_num DESC LIMIT 50'
    cur.execute(sql)
    return cur.fetchall()

def busca_todas_notas_status(status):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Nf_num, Data, Nfiscais.Id_cliente, Nome, Valor, Desconto_fidelidade, Status  FROM Nfiscais LEFT JOIN clientes ON Nfiscais.Id_cliente = clientes.Id_cliente WHERE Status=? ORDER BY Nf_num DESC LIMIT 50'
    cur.execute(sql, (status,))
    return cur.fetchall()

def busca_nf_data_status(data, status):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT NF_num, Nfiscais.data as dia ,Nfiscais.Id_cliente, clientes.Nome as cliente, valor,Desconto_fidelidade, status FROM Nfiscais LEFT JOIN clientes on Nfiscais.id_cliente = clientes.Id_cliente WHERE status=? AND data=?'
    cur.execute(sql, (status, data))
    return cur.fetchall()

def buscar_nf_data(data):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT NF_num, Nfiscais.data as dia ,Nfiscais.Id_cliente,  clientes.Nome as cliente,  valor,Desconto_fidelidade, status FROM Nfiscais LEFT JOIN clientes on Nfiscais.id_cliente = clientes.Id_cliente WHERE data=?'
    cur.execute(sql, (data,))
    return cur.fetchall()

def buscar_nf_cliente(id_cliente):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Nf_num, Data, Nfiscais.Id_cliente, Nome, Valor, Desconto_fidelidade, Status  FROM Nfiscais LEFT JOIN clientes ON Nfiscais.Id_cliente = clientes.Id_cliente WHERE clientes.Id_cliente=?'
    cur.execute(sql, (id_cliente,))
    return cur.fetchall()

def buscar_nf_cliente_status(id_cliente, status):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Nf_num, Data, Nfiscais.Id_cliente, Nome, Valor, Desconto_fidelidade, Status  FROM Nfiscais LEFT JOIN clientes ON Nfiscais.Id_cliente = clientes.Id_cliente WHERE clientes.Id_cliente=? AND Nfiscais.Status=?'
    cur.execute(sql, (id_cliente, status))
    return cur.fetchall()

##############################


def busca_nf_intervalo_datas(data_inicio, data_fim):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Nf_num, Data, Nfiscais.Id_cliente, Nome, Valor, Desconto_fidelidade, Status  FROM Nfiscais LEFT JOIN clientes ON Nfiscais.Id_cliente = clientes.Id_cliente WHERE Nfiscais.Data BETWEEN ? AND ?'
    cur.execute(sql, (data_inicio, data_fim))
    return cur.fetchall()


def busca_nf_intervalo_datas_status(data_inicio, data_fim, status):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Nf_num, Data, Nfiscais.Id_cliente, Nome, Valor, Desconto_fidelidade, Status  FROM Nfiscais LEFT JOIN clientes ON Nfiscais.Id_cliente = clientes.Id_cliente WHERE Nfiscais.Data BETWEEN ? AND ? AND Status=?'
    cur.execute(sql, (data_inicio, data_fim, status))
    return cur.fetchall()


def busca_nf_intervalo_notas(nota_inicio, nota_fim):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Nf_num, Data, Nfiscais.Id_cliente, Nome, Valor, Desconto_fidelidade, Status  FROM Nfiscais LEFT JOIN clientes ON Nfiscais.Id_cliente = clientes.Id_cliente WHERE Nfiscais.Nf_num BETWEEN ? AND ?'
    cur.execute(sql, (nota_inicio, nota_fim))
    return cur.fetchall()


def busca_nf_intervalo_notas_status(nota_inicio, nota_fim, status):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Nf_num, Data, Nfiscais.Id_cliente, Nome, Valor, Desconto_fidelidade, Status  FROM Nfiscais LEFT JOIN clientes ON Nfiscais.Id_cliente = clientes.Id_cliente WHERE Nfiscais.Nf_num BETWEEN ? AND ? AND Status=?'
    cur.execute(sql, (nota_inicio, nota_fim, status))
    return cur.fetchall()

#############################

#ITENS NF


def criar_tb_itens_nf():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = """CREATE TABLE IF NOT EXISTS "Itens_nf" (
	"Id_item"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Nf"	INTEGER,
	"data_emissao"	DATE,
	"Codigo_serv"	INTEGER,
	"Id_profi"	INTEGER,
	"Id_fpag"	INTEGER,
	"Preco_tab"	REAL,
	"Preco_fat"	REAL,
	"percentual"	INTEGER,
	"fidelidade"	BOOLEAN,
	"id_cliente"	INTEGER,
	FOREIGN KEY("id_cliente") REFERENCES "clientes"("Id_cliente"),
	FOREIGN KEY("Nf") REFERENCES "Nfiscais"("Nf_num"),
	FOREIGN KEY("Codigo_serv") REFERENCES "servicos"("Codigo"),
	FOREIGN KEY("Id_profi") REFERENCES "funcionarios"("Id_func"),
	FOREIGN KEY("Id_fpag") REFERENCES "fpag"("Id_fpag")
)"""
    cur.execute(sql)
    banco.commit()
    banco.close()

def inserir_itens_nf(nf, codigo, id_profi, id_fpag, preco_tab, preco_fat, desc, fidelidade, id_cliente):
    global data_atual
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'INSERT INTO Itens_nf VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cur.execute(sql, (None, nf, data_atual, codigo, id_profi, id_fpag, preco_tab, preco_fat, desc, fidelidade,id_cliente))
    banco.commit()
    banco.close()

def buscar_itens_nf(nf):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Id_item as ID, NF, servicos.Codigo, servicos.Nome as serviço , funcionarios.Nome as profissional, Preco_fat, fidelidade, Itens_nf.percentual, fpag.Fpag_name FROM Itens_nf LEFT JOIN servicos ON servicos.Codigo = Itens_nf.Codigo_serv LEFT JOIN funcionarios on funcionarios.Id_func = Itens_nf.Id_profi LEFT JOIN fpag on Itens_nf.Id_fpag = fpag.Id_fpag  WHERE Itens_nf.Nf=?'
    cur.execute(sql, (nf,))
    return cur.fetchall()

def calcula_total_nf(nf):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT sum(Preco_fat) FROM Itens_nf WHERE Nf =?'
    cur.execute(sql, (nf,))
    return cur.fetchall()

def atualizar_nf(nf, total):
    status = 'Emitida'
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "UPDATE Nfiscais SET valor=?, status=? WHERE Nf_num=?"
    cur.execute(sql,(total, status, nf))
    banco.commit()
    banco.close()

def atualizar_nf_cancelamento(nf, total):
    status = 'Cancelada'
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "UPDATE Nfiscais SET valor=?, status=? WHERE Nf_num=?"
    cur.execute(sql,(total, status, nf))
    banco.commit()
    banco.close()

def alterar_itens_nf(qtde, preco, id):
    cria_tabelas()
    valor = qtde*preco
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "UPDATE Itens_nf SET Quant=?, Preco=?, Valor=? WHERE Id=?"
    cur.execute(sql,(qtde, preco, valor, id))
    banco.commit()
    banco.close()

def excluir_item_nf(id):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "DELETE FROM Itens_nf  WHERE Id_item=?"
    cur.execute(sql,(id,))
    banco.commit()
    banco.close()

def excluir_itens_nf(nf):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "DELETE FROM Itens_nf  WHERE Nf=?"
    cur.execute(sql,(nf,))
    banco.commit()
    banco.close()

#######################################

### AGENDA

def criar_tb_agenda():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = """CREATE TABLE IF NOT EXISTS "agenda" (
	"Id_agenda"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"data_agenda"	DATA,
	"hora"	TEXT,
	"id_cliente"	INTEGER,
	"id_profi"	INTEGER,
	"id_servico"	INTEGER,
	"status_agenda"	TEXT,
	FOREIGN KEY("id_servico") REFERENCES "servicos"("Codigo"),
	FOREIGN KEY("id_profi") REFERENCES "funcionarios"("Id_func"),
	FOREIGN KEY("id_cliente") REFERENCES "clientes"("Id_cliente"))"""

    cur.execute(sql)
    banco.commit()
    banco.close()

def inserir_agendamento(data, hora, id_cliente, id_profi, id_servico, status = "Agendado"):
    global data_atual
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'INSERT INTO agenda VALUES (?, ?, ?, ?, ?, ?, ?)'
    cur.execute(sql, (None, data, hora, id_cliente, id_profi, id_servico, status))
    banco.commit()
    banco.close()

def busca_toda_agenda_dia(dia):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT data_agenda, hora, servicos.Tempo_medio, funcionarios.Nome as profissional, clientes.Nome as cliente, clientes.Telefone, servicos.Nome as servico, status_agenda, Id_agenda FROM agenda LEFT JOIN servicos on agenda.id_servico = servicos.Codigo LEFT JOIN clientes on agenda.id_cliente = clientes.Id_cliente LEFT JOIN funcionarios on agenda.id_profi= funcionarios.Id_func WHERE  data_agenda >= ? AND status_agenda <> "Eliminado" order by data_agenda,hora'
    cur.execute(sql, (dia,))
    return cur.fetchall()


def busca_toda_agenda_dia_pendentes(status='Pendente'):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT data_agenda, hora, servicos.Tempo_medio, funcionarios.Nome as profissional, clientes.Nome as cliente, clientes.Telefone, servicos.Nome as servico, status_agenda, Id_agenda FROM agenda LEFT JOIN servicos on agenda.id_servico = servicos.Codigo LEFT JOIN clientes on agenda.id_cliente = clientes.Id_cliente LEFT JOIN funcionarios on agenda.id_profi= funcionarios.Id_func WHERE status_agenda=? order by data_agenda,hora'
    cur.execute(sql, (status,))
    return cur.fetchall()

def busca_agenda_dia_profi(dia, id_profi):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT data_agenda, hora, servicos.Tempo_medio, clientes.Nome as cliente, clientes.Telefone, servicos.Nome as servico, clientes.Fidelizado, status_agenda, Id_agenda FROM agenda LEFT JOIN servicos on agenda.id_servico = servicos.Codigo LEFT JOIN clientes on agenda.id_cliente = clientes.Id_cliente LEFT JOIN funcionarios on agenda.id_profi= funcionarios.Id_func WHERE id_profi = ? and data_agenda >= ? AND status_agenda <> "Eliminado" ORDER by  data_agenda,hora'
    cur.execute(sql, (id_profi, dia))
    return cur.fetchall()


def alterar_agendamento(hora, id_servico, status, id_ag):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE agenda SET hora=?, id_servico=?, status_agenda=? WHERE id_agenda=?'
    cur.execute(sql, (hora, id_servico, status, id_ag))
    banco.commit()
    banco.close()


def efetuar_agendamento(id_ag):
    status='Serviço efetuado'
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE agenda SET status_agenda=? WHERE id_agenda=?'
    cur.execute(sql, (status, id_ag))
    banco.commit()
    banco.close()


def alterar_status_pendentes(id_ag, status):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE agenda SET status_agenda=? WHERE id_agenda=?'
    cur.execute(sql, (status, id_ag))
    banco.commit()
    banco.close()

def setar_pendentes():
    status='Pendente'
    global data_atual
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE agenda SET status_agenda=? WHERE data_agenda<? AND status_agenda = "Agendado"'
    cur.execute(sql, (status, data_atual))
    banco.commit()
    banco.close()

def cria_tabelas():
    criar_usuario()
    criar_tb_funcionario()
    criar_tb_clientes()
    criar_tb_servicos()
    criar_tb_notas()
    cria_tb_fpag()
    criar_tb_itens_nf()
    criar_tb_agenda()


#### ESATISTICAS

def vendas_por_dia():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT data_emissao, sum(Preco_tab), sum(Preco_fat) FROM Itens_nf GROUP BY data_emissao ORDER BY data_emissao DESC'
    cur.execute(sql)
    return cur.fetchall()


def vendas_por_dia_intervalo(data_inicial, data_final):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT data_emissao, sum(Preco_tab), sum(Preco_fat) FROM Itens_nf WHERE data_emissao BETWEEN ? AND ? GROUP BY data_emissao ORDER BY data_emissao DESC'
    cur.execute(sql, (data_inicial, data_final))
    return cur.fetchall()

def vendas_por_servico_ranking_desc():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT  count(Codigo_serv), servicos.Nome, sum(Preco_tab), sum(Preco_fat), servicos.Tempo_medio FROM Itens_nf LEFT JOIN servicos on Codigo_serv = Codigo GROUP BY Codigo_serv ORDER BY sum(Preco_fat) DESC'
    cur.execute(sql)
    return cur.fetchall()


def vendas_por_servico_ranking_desc_intervalo(data_inicial, data_final):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT  count(Codigo_serv), servicos.Nome, sum(Preco_tab), sum(Preco_fat), servicos.Tempo_medio FROM Itens_nf  LEFT JOIN servicos on Codigo_serv = Codigo WHERE data_emissao BETWEEN ? AND ? GROUP BY Codigo_serv ORDER BY sum(Preco_fat) DESC'
    cur.execute(sql, (data_inicial, data_final))
    return cur.fetchall()

def vendas_por_funcionario_ranking_desc():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT  count(Itens_nf.Id_profi), funcionarios.nome, funcionarios.Cargo, sum(Preco_tab), sum(Preco_fat) FROM Itens_nf LEFT JOIN funcionarios on Itens_nf.Id_profi = funcionarios.Id_func GROUP BY Itens_nf.Id_profi ORDER BY sum(Preco_fat) DESC'
    cur.execute(sql)
    return cur.fetchall()


def vendas_por_funcionario_ranking_desc_intervalo(data_inicial, data_final):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT  count(Itens_nf.Id_profi), funcionarios.nome, funcionarios.Cargo, sum(Preco_tab), sum(Preco_fat) FROM Itens_nf LEFT JOIN funcionarios on Itens_nf.Id_profi = funcionarios.Id_func WHERE data_emissao BETWEEN ? AND ? GROUP BY Itens_nf.Id_profi ORDER BY sum(Preco_fat) DESC'
    cur.execute(sql, (data_inicial, data_final))
    return cur.fetchall()


## busca todas as vendas em totais dos clientes em um ranking do maior para o menor em valor total
def vendas_por_cliente_ranking_desc():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT clientes.Nome,  count(Itens_nf.id_cliente), sum(Preco_tab), sum(Preco_fat), clientes.Fidelizado FROM Itens_nf LEFT JOIN clientes on Itens_nf.id_cliente = clientes.Id_cliente GROUP BY Itens_nf.id_cliente ORDER BY sum(Preco_fat) DESC'
    cur.execute(sql)
    return cur.fetchall()
    
def vendas_por_cliente_ranking_desc_intervalo(data_inicial, data_final):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT clientes.Nome,  count(Itens_nf.id_cliente), sum(Preco_tab), sum(Preco_fat), clientes.Fidelizado FROM Itens_nf LEFT JOIN clientes on Itens_nf.id_cliente = clientes.Id_cliente WHERE data_emissao BETWEEN ? AND ? GROUP BY Itens_nf.id_cliente ORDER BY sum(Preco_fat) DESC'
    cur.execute(sql, (data_inicial, data_final))
    return cur.fetchall()

def vendas_por_fpag_ranking_desc():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT  count(Itens_nf.Id_fpag), fpag.Fpag_name, sum(Preco_tab), sum(Preco_fat) FROM Itens_nf LEFT JOIN fpag on Itens_nf.Id_fpag = fpag.Id_fpag GROUP BY Itens_nf.Id_fpag ORDER BY sum(Preco_fat) DESC'
    cur.execute(sql)
    return cur.fetchall()


def vendas_por_fpag_ranking_desc_intervalo(data_inicial, data_final):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT  count(Itens_nf.Id_fpag), fpag.Fpag_name, sum(Preco_tab), sum(Preco_fat) FROM Itens_nf LEFT JOIN fpag on Itens_nf.Id_fpag = fpag.Id_fpag WHERE data_emissao BETWEEN ? AND ? GROUP BY Itens_nf.Id_fpag ORDER BY sum(Preco_fat) DESC'
    cur.execute(sql, (data_inicial, data_final))
    return cur.fetchall()


#FUNÇÕES ESTATÍSTICAS FUTURO BASEADO NA AGENDA

def previsao_fat_dia(data_inicial, data_final):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT data_agenda, sum(servicos.Valor) FROM agenda LEFT JOIN servicos on servicos.Codigo = agenda.id_servico WHERE status_agenda="Agendado" AND data_agenda BETWEEN ? AND ? GROUP BY data_agenda'
    cur.execute(sql, (data_inicial, data_final))
    return cur.fetchall()

def previsao_fat_servico_futuro(data_inicial, data_final):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT servicos.Nome, count(id_servico), sum(servicos.Valor) as Total_servico FROM agenda LEFT JOIN servicos on servicos.Codigo = agenda.id_servico WHERE status_agenda="Agendado" AND data_agenda BETWEEN ? AND ? GROUP BY id_servico ORDER BY TotaL_servico DESC'
    cur.execute(sql, (data_inicial, data_final))
    return cur.fetchall()


def previsao_fat_cliente_futuro(data_inicial, data_final):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT clientes.Nome, count(agenda.id_cliente), sum(servicos.Valor) as Total_servico, clientes.Fidelizado FROM agenda LEFT JOIN servicos on servicos.Codigo = agenda.id_servico LEFT JOIN clientes on clientes.Id_cliente = agenda.id_cliente WHERE status_agenda="Agendado" AND data_agenda BETWEEN ? AND ? GROUP BY agenda.id_cliente ORDER BY TotaL_servico DESC'
    cur.execute(sql, (data_inicial, data_final))
    return cur.fetchall()


def previsao_fat_profi_futuro(data_inicial, data_final):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT funcionarios.Nome, count(agenda.id_profi), sum(servicos.Valor) as Total_servico, funcionarios.Cargo FROM agenda LEFT JOIN servicos on servicos.Codigo = agenda.id_servico LEFT JOIN funcionarios on funcionarios.Id_func = agenda.id_profi WHERE status_agenda="Agendado" AND data_agenda BETWEEN ? AND ? GROUP BY agenda.id_profi ORDER BY TotaL_servico DESC'
    cur.execute(sql, (data_inicial, data_final))
    return cur.fetchall()

def lista_negra_cancelamentos():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT clientes.Nome, count(agenda.id_cliente), clientes.Fidelizado, agenda.status_agenda FROM agenda LEFT JOIN servicos on servicos.Codigo = agenda.id_servico LEFT JOIN clientes on clientes.Id_cliente = agenda.id_cliente WHERE status_agenda="Cancelado pelo cliente" OR status_agenda="Cliente não compareceu" GROUP BY clientes.Nome, agenda.status_agenda  ORDER BY clientes.Nome'
    cur.execute(sql)
    return cur.fetchall()


#ESTATÍSTICAS POR GÊNERO DE CLIENTE

def vendas_realizadas_genero():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT clientes.Sexo, sum(Preco_fat), count(clientes.Sexo), sum(servicos.Tempo_medio) FROM Itens_nf LEFT JOIN clientes on Itens_nf.id_cliente = clientes.Id_cliente LEFT JOIN servicos on Itens_nf.Codigo_serv = servicos.Codigo WHERE Itens_nf.data_emissao GROUP BY clientes.Sexo ORDER BY sum(Preco_fat) DESC'
    cur.execute(sql)
    return cur.fetchall()

def vendas_realizadas_genero_intervalo(data_inicial, data_final):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = """SELECT clientes.Sexo, sum(Preco_fat), count(clientes.Sexo), sum(servicos.Tempo_medio) FROM Itens_nf LEFT JOIN clientes on Itens_nf.id_cliente = clientes.Id_cliente LEFT JOIN servicos on Itens_nf.Codigo_serv = servicos.Codigo WHERE Itens_nf.data_emissao BETWEEN ? AND ? GROUP BY clientes.Sexo ORDER BY sum(Preco_fat) DESC"""
    cur.execute(sql, (data_inicial, data_final))
    return cur.fetchall()


#ESTATÍSTICAS FUTURAS POR GÊNERO DE CLIENTE

def vendas_previstas_genero():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT clientes.Sexo, sum(servicos.Valor), count(clientes.Sexo), sum(servicos.Tempo_medio) FROM agenda LEFT JOIN clientes on agenda.id_cliente = clientes.Id_cliente LEFT JOIN servicos on agenda.id_servico = servicos.Codigo WHERE status_agenda="Agendado" GROUP BY clientes.Sexo ORDER BY sum(Valor) DESC'
    cur.execute(sql)
    return cur.fetchall()

def vendas_previstas_genero_intervalo(data_inicial, data_final):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = """SELECT clientes.Sexo, sum(servicos.Valor), count(clientes.Sexo), sum(servicos.Tempo_medio) FROM agenda LEFT JOIN clientes on agenda.id_cliente = clientes.Id_cliente LEFT JOIN servicos on agenda.id_servico = servicos.Codigo WHERE status_agenda='Agendado' AND data_agenda BETWEEN ? AND ? GROUP BY clientes.Sexo ORDER BY sum(Valor) DESC"""
    cur.execute(sql, (data_inicial, data_final))
    return cur.fetchall()


    #### funções para emissão de NF pela agenda

def busca_serv_efetuado_agenda():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "SELECT data_agenda, funcionarios.Nome as funcionario, clientes.nome as cliente, servicos.Nome as servico, clientes.Fidelizado, servicos.Valor, status_agenda, Id_agenda  FROM agenda  LEFT JOIN clientes on agenda.id_cliente = clientes.Id_cliente LEFT join funcionarios on agenda.id_profi = funcionarios.Id_func LEFT JOIN servicos on agenda.id_servico = servicos.Codigo WHERE status_agenda = 'Serviço efetuado' ORDER by data_agenda"
    cur.execute(sql)
    return cur.fetchall()

def busca_serv_agenda_id(id):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "SELECT data_agenda, funcionarios.Id_func, funcionarios.Nome as funcionario, clientes.Id_cliente, clientes.nome as cliente, servicos.Codigo ,servicos.Nome as servico, clientes.Fidelizado, servicos.Valor, status_agenda, Id_agenda  FROM agenda  LEFT JOIN clientes on agenda.id_cliente = clientes.Id_cliente LEFT join funcionarios on agenda.id_profi = funcionarios.Id_func LEFT JOIN servicos on agenda.id_servico = servicos.Codigo WHERE agenda.Id_agenda = ?"
    cur.execute(sql, (id, ))
    return cur.fetchall()

def alterar_status_ag_nf_emitida(id_ag, status):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'UPDATE agenda SET status_agenda=? WHERE id_agenda=?'
    cur.execute(sql, (status, id_ag))
    banco.commit()
    banco.close()


#FUNÇÕES DE VERIFICAÇÃO DE PENDÊNCIAS




