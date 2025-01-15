import sqlite3

def conectar():
    return sqlite3.connect('/home/eduardo/projetos/controle_estoques/controle-de-estoques/db/estoque')

def desconectar(conexao):
    conexao.close()

def executar_consulta(conexao, consulta, parametros=None):
    cursor = conexao.cursor()
    if parametros:
        cursor.execute(consulta, parametros)
    else:
        cursor.execute(consulta)
    conexao.commit()