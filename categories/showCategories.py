from connection.connection import connect_database

def show_categories():
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return

    cursor = connection.cursor(dictionary=True, buffered=True)

    try:
        query = """
            SELECT * FROM categories
        """
        cursor.execute(query)
        categories = cursor.fetchall()
        return categories
    except Exception as e:
        print(f"Erro ao buscar categorias: {e}")
    finally:
        cursor.close()
        connection.close()
    