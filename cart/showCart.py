from connection.connection import connect_database
from style.colors import RED, RESET

def show_cart(user_id):
    connection = connect_database()
    if not connection:
        print(f"{RED}Falha na conexão com o banco.{RESET}")
        return

    cursor = connection.cursor(dictionary=True, buffered=True)

    try:
        query = """
            SELECT up.quantity, p.product_name, p.product_price, p.product_unit, c.category_name
            FROM use_pro up
            INNER JOIN products p ON up.fk_products_product_id = p.product_id
            LEFT JOIN categories c ON p.fk_categories_category_id = c.category_id
            WHERE up.fk_users_user_id = %s
        """
        cursor.execute(query, (user_id,))
        cart = cursor.fetchall()
        return cart
    
    except Exception:
        print(f"{RED}Erro ao buscar carrinho: {RESET}")
    
    finally:
        cursor.close()
        connection.close()
