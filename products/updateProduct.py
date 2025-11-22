from connection.connection import connect_database
from style.colors import GREEN, RED, RESET, YELLOW

def update_product(product_id, product_name, product_price, product_unit, product_quantity, product_entry, product_exit, fk_categories_category_id):
    connection = connect_database()
    if not connection:
        print(f"{RED}Falha na conexão com o banco.{RESET}")
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
            print(f"{YELLOW}Nenhum produto encontrado com o ID {product_id}.{RESET}")
        else:
            print(f"{GREEN}Produto atualizado com sucesso!{RESET}")    

    except Exception:
        print(f"{RED}Erro ao atualizar produto{RESET}")

    finally:
        cursor.close()
        connection.close()