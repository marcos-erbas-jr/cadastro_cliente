import sqlite3
from sqlite3 import Error
import os

pastaApp = os.path.dirname(__file__)
nomeBanco = pastaApp + "\\clientdatabase.db"

def ConexaoBanco():
    con = None
    try:
        con = sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return con

def dql(query):
    """Para função de select"""
    try:
        vcon = ConexaoBanco()
        c = vcon.cursor()
        c.execute(query)
        res = c.fetchall()
        vcon.close()
    except Error as ex:
        print(ex)
    else:
        return res

def dml(query):
    """Para funções de insert, update, delete"""
    try:
        vcon = ConexaoBanco()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
        print("sucesso")
    except Error as ex:
        print(ex)

vsql = """CREATE TABLE colaboradores(
            ID_COLAB INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME_COLAB VARCHAR(30),
            CARGO_COLAB VARCHAR(30),
            SETOR_COLAB VARCHAR(30),
            USER_COLAB VARCHAR(15),
            SENHA_COLAB VARCHAR(20)
            );"""

vsql2 = """CREATE TABLE admins(
            ID_ADMIN INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME_ADMIN VARCHAR(30),
            CARGO_ADMIN VARCHAR(30),
            SETOR_ADMIN VARCHAR(30),
            USER_ADMIN VARCHAR(15),
            SENHA_ADMIN VARCHAR(20)
            );"""

vsql3 = """CREATE TABLE clientes(
            ID_ADMIN INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME_CLIENTE VARCHAR(30),
            ENDEREÇO_CLIENTE VARCHAR(50),
            EMAIL_CLIENTE VARCHAR(40),
            TELEFONE_CLIENTE VARCHAR(20)
            );"""

def criarTabela(conexao, sql):
    """Criar tabelas no banco de dados"""
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Tabela criada!")
    except Error as ex:
        print(ex)

vcon = ConexaoBanco()
criarTabela(vcon, vsql)