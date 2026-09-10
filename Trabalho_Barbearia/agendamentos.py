from Trabalho_Barbearia.config import DB_CONFIG
from Trabalho_Barbearia.models import Agendamento
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