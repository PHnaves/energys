
from connection.connection import connect_database
from style.colors import GREEN, RED, RESET

def remove_to_cart(user_id, product_id):
    connection = connect_database()
    if not connection:
        print(f"{RED}Falha na conexão com o banco.{RESET}")
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
            print(f"{RED}Produto com ID {product_id} não encontrado.{RESET}")
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
        print(f"{GREEN}\nProduto removido do carrinho e estoque atualizado com sucesso!{RESET}\n")
    except Exception:
       print(f"{RED}Erro ao remover produto do carrinho: {RESET}")

    finally:
        cursor.close()
        connection.close()