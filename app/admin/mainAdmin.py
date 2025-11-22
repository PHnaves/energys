from app.admin.categoriesMenuAdmin import category_menu_admin
from app.admin.productsMenuAdmin import product_menu_admin
from style.colors import CYAN, GREEN, RED, RESET, YELLOW
from users.readUser import get_user_by_id

# MENU PRINCIPAL ADM
def main_admin(user):
    while True:
        user = get_user_by_id(user['user_id'])
        if not user:
            print(f"{RED}Usuário não encontrado.{RESET}")
            from app.main import main
            main()

        print(f"\n{GREEN}=== BEM VINDO(A) DE VOLTA, ADM ({user['user_name']}) ==={RESET}")

        # Opções
        print(f"{CYAN}1 - Menu de produtos{RESET}")
        print(f"{CYAN}2 - Menu de categorias{RESET}")
        print(f"{CYAN}3 - Sair{RESET}")

        try:
            option = int(input(GREEN + "\nEscolha uma opção: " + RESET))
        except ValueError:
            print(f"{RED}Opção inválida! Digite apenas números 1, 2 ou 3.{RESET}\n")
            continue

        match option:
            case 1:
                product_menu_admin()

            case 2:
                category_menu_admin()

            case 3:
                print(f"{YELLOW}Saindo... Até mais! 👋{RESET}")
                from app.main import main
                main()

            case _:
                print(f"{RED}Opção inválida! Digite somente 1, 2 ou 3.{RESET}\n")
