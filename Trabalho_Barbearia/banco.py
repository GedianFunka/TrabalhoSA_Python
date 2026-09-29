import mysql.connector
from mysql.connector import Error
from Trabalho_Barbearia.config import DB_CONFIG

def conectar():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {Error}")
        return None