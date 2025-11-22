from connection.connection import connect_database
from style.colors import RED, RESET, YELLOW

def delete_product(product_id):
    connection = connect_database()
    if not connection:
        print(f"{RED}Falha na conexão com o banco.{RESET}")
        return

    cursor = connection.cursor()

    try:
        query = """
            DELETE FROM products WHERE product_id = %s
        """
        cursor.execute(query, (product_id,))
        connection.commit()
        if cursor.rowcount == 0:
            print(f"{YELLOW}Nenhum produto encontrado com o ID {product_id}.{RESET}")
        else:
            print("\nProduto deletado com sucesso!\n")
    except Exception:
        print(f"{RED}Erro ao deletar produto{RESET}")
    finally:
        cursor.close()
        connection.close()