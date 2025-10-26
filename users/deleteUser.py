from connection.connection import connect_database

def delete_user(user_id):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return

    cursor = connection.cursor()

    query = "DELETE FROM users WHERE user_id = %s"
    try:
        cursor.execute(query, (user_id,))
        connection.commit()
        print("Usuário deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")
    finally:
        cursor.close()
        connection.close()
