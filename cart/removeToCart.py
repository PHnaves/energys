
from connection.connection import connect_database

def remove_to_cart(user_id, product_id):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return

    cursor = connection.cursor(dictionary=True, buffered=True)

    try:
        select_query = """
            SELECT quantity FROM use_pro
            WHERE fk_users_user_id = %s AND fk_products_product_id = %s
        """
        cursor.execute(select_query, (user_id, product_id))
        item = cursor.fetchone()

        if not item:
            print("Produto não encontrado no carrinho.")
            return

        quantity = item["quantity"]

        delete_query = """
            DELETE FROM use_pro
            WHERE fk_users_user_id = %s AND fk_products_product_id = %s
        """
        cursor.execute(delete_query, (user_id, product_id))

        update_stock_query = """
            UPDATE products
            SET 
                product_quantity = product_quantity + %s,
                product_exit = product_exit - %s
            WHERE product_id = %s
        """
        cursor.execute(update_stock_query, (quantity, quantity, product_id))

        connection.commit()
        print("\nProduto removido do carrinho e estoque restaurado com sucesso!\n")

    except Exception as e:
        print(f"Erro ao remover produto do carrinho: {e}")

    finally:
        cursor.close()
        connection.close()