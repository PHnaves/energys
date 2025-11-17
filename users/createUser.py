import bcrypt
from connection.connection import connect_database

def create_user(user_name, user_email, user_password, user_cpf, user_date_birth):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return

    cursor = connection.cursor(dictionary=True, buffered=True) 
    hashed_password = bcrypt.hashpw(user_password, bcrypt.gensalt())

    try:
        query = """
            INSERT INTO users (user_name, user_email, user_password, user_cpf, user_date_birth)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (user_name, user_email, hashed_password, user_cpf, user_date_birth)
        cursor.execute(query, values)
        connection.commit()
        print("\nUsuário cadastrado com sucesso!\n")
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
    finally:
        cursor.close()
        connection.close()
