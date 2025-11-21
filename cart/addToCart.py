from connection.connection import connect_database

def add_to_cart(quantity, user_id, product_id):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return

    cursor = connection.cursor(dictionary=True, buffered=True)

    try:
        cursor.execute("""
            SELECT product_quantity FROM products WHERE product_id = %s
        """, (product_id,))
        product = cursor.fetchone()

        if not product:
            print(f"Produto com ID {product_id} não encontrado.")
            return

        if quantity > product['product_quantity']:
            print(f"\nQuantidade solicitada ({quantity}) é maior que o estoque disponível.\n")
            return

        query_select = """
            SELECT id, quantity FROM use_pro
            WHERE fk_users_user_id = %s AND fk_products_product_id = %s
        """
        cursor.execute(query_select, (user_id, product_id))
        existing = cursor.fetchone()

        if existing:
            new_quantity = existing['quantity'] + quantity

            if new_quantity > product['product_quantity']:
                print(f"\nVocê já tem {existing['quantity']} unidades no carrinho. Não há estoque suficiente para adicionar mais.\n")
                return

            query_update = "UPDATE use_pro SET quantity = %s WHERE id = %s"
            cursor.execute(query_update, (new_quantity, existing['id']))
        else:
            query_insert = """
                INSERT INTO use_pro (quantity, fk_users_user_id, fk_products_product_id)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query_insert, (quantity, user_id, product_id))

        update_stock_query = """
            UPDATE products
            SET 
                product_quantity = product_quantity - %s,
                product_exit = product_exit + %s
            WHERE product_id = %s
        """
        cursor.execute(update_stock_query, (quantity, quantity, product_id))

        connection.commit()
        print("\nProduto adicionado ao carrinho e estoque atualizado com sucesso!\n")

    except Exception as e:
        print(f"Erro ao adicionar produto ao carrinho: {e}")
        connection.rollback()

    finally:
        cursor.close()
        connection.close()
