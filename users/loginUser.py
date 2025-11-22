import bcrypt
from connection.connection import connect_database
from style.colors import RED, RESET, YELLOW
from users.sessionUser import set_logged_user

def login_user(email, password):
    connection = connect_database()
    if not connection:
        print(f"{RED}Falha na conexão com o banco.{RESET}")
        return

    cursor = connection.cursor(dictionary=True, buffered=True)

    try:
        query = """ 
            SELECT * FROM users WHERE user_email = %s
        """
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        if user and bcrypt.checkpw(password, user['user_password'].encode('utf-8')):
            set_logged_user(user)  
        else:
            print(f"{YELLOW}Email ou senha incorretos.{RESET}")
    except Exception:
        print(f"{RED}Erro ao realizar login{RESET}")
    finally:
        cursor.close()
        connection.close()
