from connection.connection import connect_database
from style.colors import GREEN, RED, RESET

def update_category(category_id, category_name, category_description):
    connection = connect_database()
    if not connection:
        print(f"{RED}Falha na conexão com o banco.{RESET}")
        return

    cursor = connection.cursor(dictionary=True, buffered=True) 

    try:
        query = """
            UPDATE categories
            SET category_name = %s, category_description = %s
            WHERE category_id = %s
        """
        cursor.execute(query, (category_name, category_description, category_id))
        connection.commit()
        if cursor.rowcount == 0:
            print(f"{RED}Nenhuma categoria encontrada com o ID {category_id}.{RESET}")
        else:
            print(f"{GREEN}Categoria atualizada com sucesso!{RESET}")

    except Exception:
        print(f"{RED}Erro ao atualizar categoria{RESET}")
    finally:
        cursor.close()
        connection.close()