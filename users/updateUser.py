from connection.connection import connect_database
import bcrypt
from users.sessionUser import set_logged_user

def update_user(user_id, new_value, option):
    connection = connect_database()
    if not connection:
        print("Falha na conexão com o banco.")
        return

    cursor = connection.cursor(dictionary=True, buffered=True)

    # Mapeando qual campo será atualizado
    fields = {
        1: "user_name",
        2: "user_email",
        3: "user_password",
        4: "user_cpf",
        5: "user_date_birth"
    }

    if option not in fields:
        print("Opção inválida para atualização.")
        return

    field_name = fields[option]

    # Senha precisa ser tratada com hash
    if option == 3:
        new_value = bcrypt.hashpw(new_value.encode('utf-8'), bcrypt.gensalt())

    try:
        query = f"UPDATE users SET {field_name} = %s WHERE user_id = %s"
        cursor.execute(query, (new_value, user_id))
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
