# Função para atualizar um usuário
from Connection.connection import connect_database

def atualizar_usuario(id_usuario, user_name, user_email, user_password, user_cpf, user_phone, user_date_birth):
    connection = connect_database()
    if connection:
        cursor = connection.cursor()
        
        query = """UPDATE = users 
                   SET user_name = %s, user_email = %s, user_password = %s, user_cpf = %s, user_phone = %s, user_date_birth = %s 
                   WHERE id = %s"""
        
        # Passing the correct values in the correct order
        values = (user_name, user_email, user_password, user_cpf, user_phone, user_date_birth, id_usuario)
        
        cursor.execute(query, values)
        
        connection.commit()
        
        print("Usuario atualizado!")
        
        connection.close()
