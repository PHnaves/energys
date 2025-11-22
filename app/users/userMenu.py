from app.users.productsMenuUser import product_menu_user
from users.readUser import get_user_by_id
from app.users.profileMenu import profile_menu
from users.sessionUser import clear_session
from style.colors import CYAN, GREEN, RED, RESET, YELLOW

# MENU PRINCIPAL
def user_menu(user):
    while True:
        user = get_user_by_id(user['user_id'])
        if not user:
            print(f"{RED}Usuário não encontrado.{RESET}")
            from app.main import main
            main()

        print(f"\n{GREEN}=== BEM VINDO(A) DE VOLTA, ({user['user_name']}) ==={RESET}")
        print(f"{CYAN}1 - Perfil{RESET}")
        print(f"{CYAN}2 - Produtos{RESET}")
        print(f"{CYAN}3 - Sair{RESET}")

        try:
            option = int(input(GREEN + "\nEscolha uma opção: " + RESET))
        except ValueError:
            print(f"{RED}Opção inválida! Digite apenas números 1, 2 ou 3.{RESET}\n")
            continue

        match option:
            case 1:
                profile_menu(user)

            case 2:
                product_menu_user()

            case 3:
                clear_session()
                print(f"{YELLOW}Saindo... Até mais! 👋{RESET}")
                from app.main import main  
                main()

            case _:
                print(f"{RED}Opção inválida! Digite somente 1, 2 ou 3.{RESET}\n")
