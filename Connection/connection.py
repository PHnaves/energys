import mysql.connector
from mysql.connector import Error

def connect_database():

    try:
        # Definindo as credenciais de conexão
        connection = mysql.connector.connect(
            host='localhost',  # ou o IP do seu servidor MySQL
            user='root',  # substitua pelo seu usuário
            password='root',  # substitua pela sua senha
            database='energys'  # substitua pelo nome do seu banco de dados
        )

        if connection.is_connected():
            print("Conexão bem-sucedida ao banco de dados")
            return connection  # Retorna o objeto de conexão

    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Testando a conexão
connection = connect_database()
if connection:
    connection.close()  
