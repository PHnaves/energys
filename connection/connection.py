import mysql.connector
from mysql.connector import Error

from style.colors import RED, RESET

def connect_database():

    try:
        connection = mysql.connector.connect(
            # credenciais do banco
            host='localhost',  
            user='root',  
            password='154287639',  
            database='energys'  
        )

        if connection.is_connected():
            return connection  

    except Error:
        print(f"{RED}Erro ao conectar ao banco de dados{RESET}")
        return None

