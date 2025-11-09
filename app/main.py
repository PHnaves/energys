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

        option = input("Escolha uma opção: ")
        match option:
            case "1":
                login_user()
                user = get_logged_user()
                if user:
                    if user["type_user"] == "ADM":
                        main_admin(user)
                    else:
                        user_menu(user)
            case "2":
                create_user()
            case "3":
                print("Saindo... Até mais!")
                break
            case _:
                print("Opção inválida, tente novamente.\n")


if __name__ == "__main__":
    main()
