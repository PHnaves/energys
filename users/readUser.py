from connection.connection import connect_database
from style.colors import RED, RESET

def get_user_by_id(user_id):
    connection = connect_database()
    if not connection:
        print(f"{RED}Falha na conexão com o banco.{RESET}")
        return None

    cursor = connection.cursor(dictionary=True, buffered=True)
    
    try:
        query = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        return user
    except Exception:
        print(f"{RED}Erro ao buscar usuário{RESET}")
    finally:
        cursor.close()
        connection.close()