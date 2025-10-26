import bcrypt
from connection.connection import connect_database
from users.sessionUser import set_logged_user

def login_user():
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return

    cursor = connection.cursor(dictionary=True, buffered=True)

    print("\n=== LOGIN ===")
    email = input("Email: ")
    password = input("Senha: ").encode('utf-8')

    try:
        query = "SELECT * FROM users WHERE user_email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user and bcrypt.checkpw(password, user['user_password'].encode('utf-8')):
            print(f"\nBem-vindo(a), {user['user_name']}!\n")
            set_logged_user(user)  
        else:
            print("\nEmail ou senha incorretos.\n")

    except Exception as e:
        print(f"Erro ao realizar login: {e}")

    finally:
        cursor.close()
        connection.close()
