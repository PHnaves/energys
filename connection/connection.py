import mysql.connector
from mysql.connector import Error

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

    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Testando a conexão
# connection = connect_database()
# if connection:
#     connection.close()  
