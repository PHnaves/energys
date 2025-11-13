from connection.connection import connect_database

def create_product(product_name, product_price, product_unit, product_quantity, product_entry, product_exit, fk_categories_category_id):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return

    cursor = connection.cursor(dictionary=True, buffered=True)

    try:
        query = """
            INSERT INTO products (product_name, product_price, product_unit, product_quantity, product_entry, product_exit, fk_categories_category_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (product_name, product_price, product_unit, product_quantity, product_entry, product_exit, fk_categories_category_id)
        cursor.execute(query, values)
        connection.commit()
        print("\nProduto cadastrado com sucesso!\n")

    except Exception as e:
        print(f"Erro ao cadastrar produto: {e}")

    finally:
        cursor.close()
        connection.close()