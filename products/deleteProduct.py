from connection.connection import connect_database

def delete_product(product_id):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return

    cursor = connection.cursor()

    try:
        query = """
            DELETE FROM products WHERE product_id = %s
        """
        cursor.execute(query, (product_id,))
        connection.commit()
        if cursor.rowcount == 0:
            print(f"Nenhum produto encontrado com o ID {product_id}.")
        else:
            print("\nProduto deletado com sucesso!\n")
    except Exception as e:
        print(f"Erro ao deletar produto: {e}")
    finally:
        cursor.close()
        connection.close()