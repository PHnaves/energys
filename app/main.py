from app.admin.mainAdmin import main_admin
from app.users.userMenu import user_menu
from users.createUser import create_user
from users.loginUser import login_user
from users.sessionUser import get_logged_user

# MENU INICIAL
def main():
    while True:
        print("=== BEM-VINDO(A) À ENERGYS ===")
        print("1 - Login")
        print("2 - Cadastro")
        print("3 - Sair")

        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida, tente novamente. Opções: 1, 2, 3\n")
            continue
    
        match option:
            case "1":
                print("\n=== LOGIN ===")
                email = input("Email: ")
                password = input("Senha: ").encode('utf-8')
                login_user(email, password)
                user = get_logged_user()
                if user:
                    if user["type_user"] == "ADM":
                        main_admin(user)
                    else:
                        user_menu(user)
            case "2":
                print("\n=== CADASTRO DE USUÁRIO ===")
                user_name = input("Nome: ")
                user_email = input("Email: ")
                user_password = input("Senha: ").encode('utf-8')
                user_cpf = input("CPF: ")
                user_phone = input("Telefone: ")
                user_date_birth = input("Data de nascimento (AAAA-MM-DD): ")
                create_user(user_name, user_email, user_password, user_cpf, user_phone, user_date_birth)
            case "3":
                print("Saindo... Até mais!")
                break
            case _:
                print("Opção inválida, tente novamente.\n")


if __name__ == "__main__":
    main()
