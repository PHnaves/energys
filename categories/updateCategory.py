from connection.connection import connect_database

def update_category(category_id, category_name, category_description):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
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
            print(f"Nenhuma categoria encontrada com o ID {category_id}.")
        else:
            print("Categoria atualizada com sucesso!")

    except Exception as e:
        print(f"Erro ao atualizar categoria: {e}")
    finally:
        cursor.close()
        connection.close()