import sqlite3
from sqlite3.dbapi2 import connect
        
    

class Usuarios():
    def __init__(self):
       self.id = None
       self.nome = None
       self.senha = None
       self.faturamento = None
       self.estatistica = None
       self.agenda = None
       self.root = None
    
    def banco_para_modelo(self, usuario_banco):
        self.id = usuario_banco[0][0]
        self.nome = usuario_banco[0][1]
        self.senha = usuario_banco[0][2]
        self.faturamento = usuario_banco[0][3]
        self.estatistica = usuario_banco[0][4]
        self.agenda = usuario_banco[0][5]
        self.root = usuario_banco[0][6] 

class Funcionario():
    def __init__(self):
        self.id = None
        self.nome = None
        self.funcao = None
        self.matricula = None

class Cliente():
    def __init__(self):
        self.id = None
        self.nome = None


class Produto():
    def __init__(self):
        self.codigo = None
        self.nome = None
        self.valor = 0

class NFiscal():
    def __init__(self):
        self.num = None
        self.data = None
        self.id_cliente = None
        self.cliente = None
        self.valor = 0
        self.status = 'Pendente'
        self.desconto_fidelidade = None
