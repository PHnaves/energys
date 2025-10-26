from users.createUser import create_user
from users.loginUser import login_user
from users.updateUser import update_user
from users.deleteUser import delete_user
from users.sessionUser import get_logged_user, clear_session, set_logged_user
from users.readUser import get_user_by_id 

def main():
    while True:
        print("=== BEM-VINDO(A) À ENERGYS ===")
        print("1 - Login")
        print("2 - Cadastro")
        print("3 - Sair")

        option = input("Escolha uma opção: ")
        match option:
            case "1":
                login_user()
                user = get_logged_user()
                if user:
                    menu(user)
            case "2":
                create_user()
            case "3":
                print("Saindo... Até mais!")
                break
            case _:
                print("Opção inválida, tente novamente.\n")


def menu(user):
    while True:
        user = get_user_by_id(user['user_id'])
        if not user:
            print("Usuário não encontrado. Voltando ao menu principal.")
            break

        print(f"\n=== MENU DO USUÁRIO ({user['user_name']}) ===")
        print("1 - Atualizar conta")
        print("2 - Deletar conta")
        print("3 - Ver meus dados")
        print("4 - Logout")

        option = input("Escolha uma opção: ")

        match option:
            case "1":
                print("=== ATUALIZAR CONTA ===")
                name = input("Novo nome: ")
                email = input("Novo email: ")
                password = input("Nova senha: ")
                cpf = input("Novo CPF: ")
                phone = input("Novo telefone: ")
                date = input("Nova data de nascimento (AAAA-MM-DD): ")
                update_user(user['user_id'], name, email, password, cpf, phone, date)

                updated_user = get_user_by_id(user['user_id'])
                set_logged_user(updated_user)

            case "2":
                confirm = input("Tem certeza que deseja deletar sua conta? (s/n): ").lower()
                if confirm == "s":
                    delete_user(user['user_id'])
                    clear_session()
                    print("Conta deletada. Voltando ao menu principal...")
                    break

            case "3":
                print("\n=== SEUS DADOS ===")
                print(f"Nome: {user['user_name']}")
                print(f"Email: {user['user_email']}")
                print(f"CPF: {user['user_cpf']}")
                print(f"Telefone: {user['user_phone']}")
                print(f"Data de nascimento: {user['user_date_birth']}")

            case "4":
                clear_session()
                print("Logout realizado com sucesso!\n")
                break

            case _:
                print("Opção inválida, tente novamente.")



if __name__ == "__main__":
    main()
