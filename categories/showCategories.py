from connection.connection import connect_database
from style.colors import RED, RESET

def show_categories():
    connection = connect_database()
    if not connection:
        print(f"{RED}Falha na conexão com o banco.{RESET}")
        return

    cursor = connection.cursor(dictionary=True, buffered=True)

    try:
        query = """
            SELECT * FROM categories
        """
        cursor.execute(query)
        categories = cursor.fetchall()
        return categories
    except Exception:
        print(f"{RED}Erro ao buscar categorias{RESET}")
    finally:
        cursor.close()
        connection.close()
    