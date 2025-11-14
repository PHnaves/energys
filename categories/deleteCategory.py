from connection.connection import connect_database

def delete_category(category_id):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return

    cursor = connection.cursor(dictionary=True, buffered=True)

    try:
        query = """
            DELETE FROM categories WHERE category_id = %s
        """
        cursor.execute(query, (category_id,))
        connection.commit()
    
        if cursor.rowcount == 0:
            print(f"Nenhuma categoria encontrada com o ID {category_id}.")
        else:
            print("Categoria deletada com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar categoria: {e}")
    finally:
        cursor.close()
        connection.close()