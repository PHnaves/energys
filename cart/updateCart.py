from connection.connection import connect_database

def update_cart(new_quantity, user_id, product_id):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return

    cursor = connection.cursor(dictionary=True, buffered=True)

    try:
        cursor.execute("""
            SELECT quantity FROM use_pro
            WHERE fk_users_user_id = %s AND fk_products_product_id = %s
        """, (user_id, product_id))
        item = cursor.fetchone()

        if not item:
            print("Produto não encontrado no carrinho.")
            return

        old_quantity = item["quantity"]
        difference = new_quantity - old_quantity 

        if difference == 0:
            print("\nA quantidade do produto já está atualizada.\n")
            return

        cursor.execute("""
            SELECT product_quantity FROM products WHERE product_id = %s
        """, (product_id,))
        product = cursor.fetchone()

        if not product:
            print(f"Produto com ID {product_id} não encontrado.")
            return

        if difference > 0 and difference > product['product_quantity']:
            print(f"\nEstoque insuficiente! Você quer adicionar {new_quantity} unidades, mas só há {product['product_quantity']} disponíveis.\n")
            return

        cursor.execute("""
            UPDATE use_pro
            SET quantity = %s
            WHERE fk_users_user_id = %s AND fk_products_product_id = %s
        """, (new_quantity, user_id, product_id))

        cursor.execute("""
            UPDATE products
            SET 
                product_quantity = product_quantity - %s,
                product_exit = product_exit + %s
            WHERE product_id = %s
        """, (difference, max(difference, 0), product_id))

        connection.commit()
        print("\nQuantidade do produto atualizada no carrinho e estoque ajustado com sucesso!\n")

    except Exception as e:
        print(f"Erro ao atualizar quantidade do carrinho: {e}")
        connection.rollback()

    finally:
        cursor.close()
        connection.close()
