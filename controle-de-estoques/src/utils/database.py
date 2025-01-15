import sqlite3
import os

def conectar():
    db_path = os.path.join(os.path.dirname(__file__), '../db/estoque')
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