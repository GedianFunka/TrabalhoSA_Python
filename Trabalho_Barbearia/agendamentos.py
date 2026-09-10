from config import DB_CONFIG
from models import Agendamento
import mysql.connector

def listar_agendamentos():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM agendamentos ORDER BY data_hora")
        return [Agendamento.reverte_tupla(linha) for linha in cursor.fetchall()]

    except mysql.connector.Error as erro:
        print(f"Erro ao listar agendamentos: {erro}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar_agendamento_por_id(id):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM agendamentos WHERE id = %s", (id,))

        buscar = cursor.fetchone()

        if buscar:
            return Agendamento.reverte_tupla(buscar)

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar agendamento: {erro}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar_por_status(status):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM agendamentos WHERE status = %s", (status,))
        return [Agendamento.reverte_tupla(linha) for linha in cursor.fetchall()]

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar agendamentos por status: {erro}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()