from connection.connection import connect_database

def get_user_by_id(user_id):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return None

    cursor = connection.cursor(dictionary=True, buffered=True)
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()

    cursor.close()
    connection.close()
    return user
