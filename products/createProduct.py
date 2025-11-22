from connection.connection import connect_database
from style.colors import GREEN, RED, RESET

def create_product(product_name, product_price, product_unit, product_quantity, product_entry, product_exit, fk_categories_category_id):
    connection = connect_database()
    if not connection:
        print(f"{RED}Falha na conexão com o banco.{RESET}")
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
        print(f"{GREEN}Produto cadastrado com sucesso!{RESET}")
    except Exception:
        print(f"{RED}Erro ao cadastrar produto{RESET}")
    finally:
        cursor.close()
        connection.close()