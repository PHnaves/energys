# Função para criar um novo usuário
from Connection.connection import connect_database

def criar_usuario(user_name, user_email, user_password, user_cpf, user_phone, user_date_birth):
    connection = connect_database()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO users (user_name, user_email, user_password, user_cpf, user_phone, user_date_birth) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (user_name, user_email, user_password, user_cpf, user_phone, user_date_birth)
        cursor.execute(query, values)
        connection.commit()
        print("Usuário criado com sucesso!")
        connection.close()
