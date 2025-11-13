from connection.connection import connect_database

def update_product(product_id, product_name, product_price, product_unit, product_quantity, product_entry, product_exit, fk_categories_category_id):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return

    cursor = connection.cursor(dictionary=True, buffered=True)

    try:
        query = """
            UPDATE products
            SET product_name = %s, product_price = %s, product_unit = %s, product_quantity = %s, product_entry = %s, product_exit = %s, fk_categories_category_id = %s
            WHERE product_id = %s
        """
        values = (product_name, product_price, product_unit, product_quantity, product_entry, product_exit, fk_categories_category_id, product_id)
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount == 0:
            print(f"Nenhum produto encontrado com o ID {product_id}.")
        else:
            print("Produto atualizado com sucesso!")    

    except Exception as e:
        print(f"Erro ao atualizar produto: {e}")

    finally:
        cursor.close()
        connection.close()