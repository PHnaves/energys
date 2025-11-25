import mysql.connector
from mysql.connector import Error

from style.colors import RED, RESET

def connect_database():

    try:
        connection = mysql.connector.connect(
            # credenciais do banco
            host='seu_localhost',  
            user='seu_usuario',  
            password='sua_senha',  
            database='seu_banco_de_dados'  
        )

        if connection.is_connected():
            return connection  

    except Error:
        print(f"{RED}Erro ao conectar ao banco de dados{RESET}")
        return None

