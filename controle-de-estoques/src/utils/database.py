import sqlite3
import os

def conectar():
    db_path = os.path.join(os.path.dirname(__file__), '../db/estoque')
    
    # Verifica se o diretório existe, se não, cria o diretório
    if not os.path.exists(os.path.dirname(db_path)):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Verifica se o arquivo de banco de dados existe, se não, cria o arquivo
    if not os.path.exists(db_path):
        open(db_path, 'w').close()
    
    return sqlite3.connect(db_path)

def desconectar(conexao):
    conexao.close()

def executar_consulta(conexao, consulta, parametros=None):
    cursor = conexao.cursor()
    if parametros:
        cursor.execute(consulta, parametros)
    else:
        cursor.execute(consulta)
    conexao.commit()
    return cursor.fetchall()

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL,
            nome_produto TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conexao.commit()
    desconectar(conexao)