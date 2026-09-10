import mysql.connector
from Trabalho_Barbearia.config import DB_CONFIG

def conectar():
    return mysql.connector.connect(**DB_CONFIG)