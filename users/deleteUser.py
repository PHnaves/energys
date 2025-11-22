from connection.connection import connect_database
from style.colors import GREEN, RED, RESET

def delete_user(user_id):
    connection = connect_database()
    if not connection:
        print(f"{RED}Falha na conexão com o banco.{RESET}")
        return

    cursor = connection.cursor(dictionary=True, buffered=True) 

    try:
        query = """
            DELETE FROM users WHERE user_id = %s
        """
        cursor.execute(query, (user_id,))
        connection.commit()
        print(f"{GREEN}Usuário deletado com sucesso!{RESET}")
    except Exception:
        print(f"{RED}Erro ao deletar usuário{RESET}")
    finally:
        cursor.close()
        connection.close()
