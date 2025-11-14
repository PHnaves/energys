from connection.connection import connect_database

def get_user_by_id(user_id):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return None

    cursor = connection.cursor(dictionary=True, buffered=True)
    try:
        query = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        return user
    except Exception as e:
        print(f"Erro ao buscar usuário: {e}")
    finally:
        cursor.close()
        connection.close()