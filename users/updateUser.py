from connection.connection import connect_database
import bcrypt
from style.colors import GREEN, RED, RESET, YELLOW
from users.sessionUser import set_logged_user

def update_user(user_id, new_value, option):
    connection = connect_database()
    if not connection:
        print(f"{RED}Falha na conexão com o banco.{RESET}")
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
        print(f"{YELLOW}Opção inválida para atualização.{RESET}")
        return

    field_name = fields[option]

    # Senha precisa ser tratada com hash
    if option == 3:
        new_value = bcrypt.hashpw(new_value.encode('utf-8'), bcrypt.gensalt())

    try:
        query = f"UPDATE users SET {field_name} = %s WHERE user_id = %s"
        cursor.execute(query, (new_value, user_id))
        connection.commit()

        print(f"{GREEN}Usuário atualizado com sucesso!{RESET}")

        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        updated_user = cursor.fetchone()
        set_logged_user(updated_user)

    except Exception:
        print(f"{RED}Erro ao atualizar usuário{RESET}")

    finally:
        cursor.close()
        connection.close()
