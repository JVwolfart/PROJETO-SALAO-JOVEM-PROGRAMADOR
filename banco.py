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
    sql = 'CREATE TABLE IF NOT EXISTS usuarios(nome TEXT, senha TEXT, criar BOOLEAN, editar BOOLEAN, excluir BOOLEAN, root BOOLEAN)'
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

def novo_usuario(nome, senha, criar, editar, excluir, root=False):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "INSERT INTO usuarios VALUES(?,?,?,?,?,?)"
    cur.execute(sql, (nome,senha,criar,editar,excluir,root))
    #cur.execute(f"INSERT INTO usuarios VALUES('{nome}','{senha}', {criar}, {editar}, {excluir}, {root})")
    banco.commit()
    banco.close()

def alterar_permissoes(nome, criar, editar, excluir, root):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = "UPDATE usuarios SET criar=?, editar=?, excluir=?, root=? WHERE nome=?"
    cur.execute(sql, (criar,editar,excluir,root,nome))
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
    sql = "SELECT criar, editar, excluir, root FROM usuarios WHERE nome=?"
    cur.execute(sql, (nome,))
    #cur.execute(f"SELECT criar, editar, excluir, root FROM usuarios WHERE nome='{nome}'")
    permissoes = cur.fetchone()
    autorizacoes = []
    for k, c in enumerate(permissoes):
        if k == 0 and c == 1:
            autorizacoes.append('Criar')
        if k == 1 and c == 1:
            autorizacoes.append('Editar')
        if k == 2 and c == 1:
            autorizacoes.append('Excluir')
        if k == 3 and c == 1:
            autorizacoes.append('Root')
    if len(autorizacoes) == 0:
        autorizacoes.append('Apenas consulta, caso queira outras permissões solicite ao administrador')
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
    sql = 'SELECT Nf_num, Data, Nfiscais.Id_cliente, Nome, Valor, Desconto_fidelidade, Status  FROM Nfiscais LEFT JOIN clientes ON Nfiscais.Id_cliente = clientes.Id_cliente ORDER BY Nf_num DESC'
    cur.execute(sql)
    return cur.fetchall()

def busca_todas_notas_status(status):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Nf_num, Data, Nfiscais.Id_cliente, Nome, Valor, Desconto_fidelidade, Status  FROM Nfiscais LEFT JOIN clientes ON Nfiscais.Id_cliente = clientes.Id_cliente WHERE Status=? ORDER BY Nf_num DESC'
    cur.execute(sql, (status,))
    return cur.fetchall()

def busca_nf_data_status(data, status):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT NFnum, Nfiscais.data as dia , clientes.Nome as cliente, valor, status FROM Nfiscais LEFT JOIN clientes on Nfiscais.id_cliente = clientes.Id_cliente WHERE status=? AND data=? ORDER BY NFnum DESC'
    cur.execute(sql, (status, data))
    return cur.fetchall()

def buscar_nf_data(data):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT NFnum, Nfiscais.data as dia , clientes.Nome as cliente,  valor, status FROM Nfiscais LEFT JOIN clientes on Nfiscais.id_cliente = clientes.Id_cliente WHERE data=? ORDER BY NFnum DESC'
    cur.execute(sql, (data,))
    return cur.fetchall()

def buscar_nf_cliente(id_cliente):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Nf_num, Data, Nfiscais.Id_cliente, Nome, Valor, Desconto_fidelidade, Status  FROM Nfiscais LEFT JOIN clientes ON Nfiscais.Id_cliente = clientes.Id_cliente WHERE clientes.Id_cliente=? ORDER BY Nf_num DESC'
    cur.execute(sql, (id_cliente,))
    return cur.fetchall()

def buscar_nf_cliente_status(id_cliente, status):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Nf_num, Data, Nfiscais.Id_cliente, Nome, Valor, Desconto_fidelidade, Status  FROM Nfiscais LEFT JOIN clientes ON Nfiscais.Id_cliente = clientes.Id_cliente WHERE clientes.Id_cliente=? AND Nfiscais.Status=? ORDER BY Nf_num DESC'
    cur.execute(sql, (id_cliente, status))
    return cur.fetchall()

##############################

def buscar_nf_func(id_func):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT NFnum, Nfiscais.data as dia , clientes.Nome as cliente, funcionarios.Nome as vendedor, matricula, valor, status FROM Nfiscais LEFT JOIN clientes on Nfiscais.id_cliente = clientes.Id_cliente, funcionarios on Nfiscais.id_func = funcionarios.Id_func WHERE Nfiscais.id_func=? ORDER BY NFnum DESC'
    cur.execute(sql, (id_func,))
    return cur.fetchall()

def buscar_nf_func_status(id_func, status):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT NFnum, Nfiscais.data as dia , clientes.Nome as cliente, funcionarios.Nome as vendedor, matricula, valor, status FROM Nfiscais LEFT JOIN clientes on Nfiscais.id_cliente = clientes.Id_cliente, funcionarios on Nfiscais.id_func = funcionarios.Id_func WHERE Nfiscais.id_func=? AND status=? ORDER BY NFnum DESC'
    cur.execute(sql, (id_func, status))
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


def cria_tabelas():
    criar_usuario()
    criar_tb_funcionario()
    criar_tb_clientes()
    criar_tb_servicos()
    criar_tb_notas()
    cria_tb_fpag()
    criar_tb_itens_nf()


#### ESATISTICAS

def vendas_por_item_ranking_desc():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT produtos.Codigo, nome, SUM (Itens_nf.Quant), SUM (Itens_nf.Valor) FROM produtos LEFT JOIN Itens_nf ON Itens_nf.Codigo = produtos.Codigo GROUP BY produtos.Codigo ORDER BY SUM (Itens_nf.Valor) DESC'
    cur.execute(sql)
    return cur.fetchall()

def vendas_por_item_ranking_desc_datas(data_inicio, data_fim):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT produtos.Codigo, nome, SUM (Itens_nf.Quant), SUM (Itens_nf.Valor) FROM produtos LEFT JOIN Itens_nf ON Itens_nf.Codigo = produtos.Codigo WHERE Itens_nf.data_venda BETWEEN ? AND ?  GROUP BY produtos.Codigo ORDER BY SUM (Itens_nf.Valor) DESC'
    cur.execute(sql, (data_inicio, data_fim))
    return cur.fetchall()

def vendas_por_funcionario_ranking_desc():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT funcionarios.Id_func, funcionarios.Matricula, funcionarios.Nome, SUM (Nfiscais.valor) FROM funcionarios LEFT JOIN Nfiscais ON funcionarios.Id_func = Nfiscais.id_func GROUP BY Nfiscais.id_func ORDER BY SUM (Nfiscais.valor) DESC'
    cur.execute(sql)
    return cur.fetchall()

def vendas_por_funcionario_ranking_desc_data(data_inicio, data_fim):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT funcionarios.Id_func, funcionarios.Matricula, funcionarios.Nome, SUM (Nfiscais.valor), funcionarios.Status_func FROM funcionarios LEFT JOIN Nfiscais ON funcionarios.Id_func = Nfiscais.id_func WHERE Nfiscais.data BETWEEN ? AND ? GROUP BY Nfiscais.id_func ORDER BY SUM (Nfiscais.valor) DESC'
    cur.execute(sql, (data_inicio, data_fim))
    return cur.fetchall()

## busca todas as vendas em totais dos clientes em um ranking do maior para o menor em valor total
def vendas_por_cliente_ranking_desc():
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT clientes.Id_cliente, clientes.Nome, SUM (Nfiscais.valor) FROM clientes LEFT JOIN Nfiscais ON clientes.Id_cliente = Nfiscais.id_cliente GROUP BY Nfiscais.id_cliente ORDER BY SUM (Nfiscais.valor) DESC'
    cur.execute(sql)
    return cur.fetchall()
    
## busca todas as vendas em totais dos clientes em um ranking do maior para o menor em valor total em um intervalo de datas
def vendas_por_cliente_ranking_desc_datas(data_Inicio, data_Fim):
    cria_tabelas()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT clientes.Id_cliente, clientes.Nome, SUM (Nfiscais.valor) FROM clientes LEFT JOIN Nfiscais ON clientes.Id_cliente = Nfiscais.id_cliente WHERE Nfiscais.data BETWEEN ? AND ?  GROUP BY Nfiscais.id_cliente ORDER BY SUM (Nfiscais.valor) DESC '
    cur.execute(sql, (data_Inicio, data_Fim))
    return cur.fetchall()


