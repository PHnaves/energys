from connection.connection import connect_database
from style.colors import RED, RESET

def read_product(product_id):
    connection = connect_database()
    if not connection:
        print(f"{RED}Falha na conexão com o banco.{RESET}")
        return None

    cursor = connection.cursor(dictionary=True, buffered=True)
    try:
        query = """
            SELECT p.product_id, p.product_name, p.product_price, p.product_unit, p.product_quantity, p.product_entry, p.product_exit, c.category_name
            FROM products p
            INNER JOIN categories c
            ON p.fk_categories_category_id = c.category_id
            WHERE p.product_id = %s
        """
        cursor.execute(query, (product_id,))
        product = cursor.fetchone()
        return product
    except Exception:
        print(f"{RED}Erro ao buscar produto{RESET}")
    finally:
        cursor.close()
        connection.close()