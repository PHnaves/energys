from connection.connection import connect_database
import bcrypt
from users.sessionUser import set_logged_user

def update_user(user_id, user_name, user_email, user_password, user_cpf, user_phone, user_date_birth):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return

    cursor = connection.cursor(dictionary=True, buffered=True) 
    hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute("""
            UPDATE users
            SET user_name = %s, user_email = %s, user_password = %s,
                user_cpf = %s, user_phone = %s, user_date_birth = %s
            WHERE user_id = %s
        """, (user_name, user_email, hashed_password, user_cpf, user_phone, user_date_birth, user_id))
        connection.commit()
        print("Usuário atualizado com sucesso!")

        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        updated_user = cursor.fetchone()
        set_logged_user(updated_user)

    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")
    finally:
        cursor.close()
        connection.close()
