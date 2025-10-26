import bcrypt
from connection.connection import connect_database

def create_user():
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return

    cursor = connection.cursor(dictionary=True, buffered=True) 

    print("\n=== CADASTRO DE USUÁRIO ===")
    user_name = input("Nome: ")
    user_email = input("Email: ")
    user_password = input("Senha: ").encode('utf-8')
    user_cpf = input("CPF: ")
    user_phone = input("Telefone: ")
    user_date_birth = input("Data de nascimento (AAAA-MM-DD): ")

    hashed_password = bcrypt.hashpw(user_password, bcrypt.gensalt())

    try:
        query = """
            INSERT INTO users (user_name, user_email, user_password, user_cpf, user_phone, user_date_birth)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (user_name, user_email, hashed_password, user_cpf, user_phone, user_date_birth)
        cursor.execute(query, values)
        connection.commit()
        print("\nUsuário cadastrado com sucesso!\n")

    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
    finally:
        cursor.close()
        connection.close()
