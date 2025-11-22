from connection.connection import connect_database
from style.colors import GREEN, RED, RESET

def create_category(category_name, category_description):
    connection = connect_database()
    if not connection:
        print(f"{RED}Falha na conexão com o banco.{RESET}")
        return

    cursor = connection.cursor(dictionary=True, buffered=True)

    try:
        query = """
            INSERT INTO categories (category_name, category_description)
            VALUES (%s, %s)
        """
        values = (category_name, category_description)
        cursor.execute(query, values)
        connection.commit()
        print(f"{GREEN}Categoria cadastrada com sucesso!{RESET}")
    except Exception:
        print(f"{RED}Erro ao cadastrar categoria{RESET}")
    finally:
        cursor.close()
        connection.close()