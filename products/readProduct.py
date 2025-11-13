from connection.connection import connect_database

def read_product(product_id):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return None

    cursor = connection.cursor(dictionary=True, buffered=True)
    query = """
        SELECT p.product_id, p.product_name, p.product_price, p.product_unit, p.product_quantity, p.product_entry, p.product_exit, c.category_name
        FROM products p
        INNER JOIN categories c
        ON p.fk_categories_category_id = c.category_id
        WHERE p.product_id = %s
    """
    cursor.execute(query, (product_id,))
    product = cursor.fetchone()

    cursor.close()
    connection.close()
    return product