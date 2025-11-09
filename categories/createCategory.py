from connection.connection import connect_database

def create_category(category_name, category_description):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
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
        print("\nCategoria cadastrada com sucesso!\n")

    except Exception as e:
        print(f"Erro ao cadastrar categoria: {e}")

    finally:
        cursor.close()
        connection.close()