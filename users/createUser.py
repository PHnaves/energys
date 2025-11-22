import bcrypt
from connection.connection import connect_database
from style.colors import GREEN, RED, RESET

def create_user(user_name, user_email, user_password, user_cpf, user_date_birth):
    connection = connect_database()
    if not connection:
        print(f"{RED}Falha na conexão com o banco.{RESET}")
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
        print(f"{GREEN}Usuário cadastrado com sucesso!{RESET}")
    except Exception:
        print(f"{RED}Erro ao cadastrar usuário{RESET}")
    finally:
        cursor.close()
        connection.close()
