from categories.createCategory import create_category
from categories.showCategories import show_categories
from categories.updateCategory import update_category
from categories.deleteCategory import delete_category
from style.colors import CYAN, YELLOW, GREEN, RED, RESET
from users.sessionUser import get_logged_user

def category_menu_admin():
    while True:
        print(f"\n{GREEN}=== MENU DE CATEGORIAS ADMIN ==={RESET}")
        print(f"{CYAN}1 - Criar categoria{RESET}")
        print(f"{CYAN}2 - Listar categorias{RESET}")
        print(f"{CYAN}3 - Excluir categoria{RESET}")
        print(f"{CYAN}4 - Atualizar categoria{RESET}")
        print(f"{CYAN}5 - Voltar ao menu principal{RESET}")

        try:
            option = int(input(GREEN + "\nEscolha uma opção: " + RESET))
        except ValueError:
            print(f"{RED}Opção inválida! Digite somente números 1, 2, 3, 4 ou 5.{RESET}\n")
            continue

        match option:
            case 1:
                print(f"\n{GREEN}=== CADASTRO DE CATEGORIA ==={RESET}")
                category_name = input(CYAN + "Nome da categoria: " + RESET)
                category_description = input(CYAN + "Descrição da categoria: " + RESET)
                create_category(category_name, category_description)

            case 2:
                categories = show_categories()
                if categories:
                    print(f"\n{GREEN}=== LISTA DE CATEGORIAS ==={RESET}")
                    for category in categories:
                        print(f"{CYAN}ID:{RESET} {category['category_id']}")
                        print(f"{CYAN}Nome:{RESET} {category['category_name']}")
                        print(f"{CYAN}Descrição:{RESET} {category['category_description']}\n")
                else:
                    print(f"{YELLOW}Nenhuma categoria cadastrada.{RESET}")

            case 3:
                print(f"\n{GREEN}=== EXCLUSÃO DE CATEGORIA ==={RESET}")
                try:
                    category_id = int(input(CYAN + "Digite o ID da categoria que deseja excluir: " + RESET))
                except ValueError:
                    print(f"{RED}ID inválido! Digite somente números.{RESET}\n")
                    continue
                delete_category(category_id)

            case 4:
                print(f"\n{GREEN}=== ATUALIZAR CATEGORIA ==={RESET}")
                try:
                    category_id = int(input(CYAN + "Digite o ID da categoria que deseja atualizar: " + RESET))
                except ValueError:
                    print(f"{RED}ID inválido! Digite somente números.{RESET}\n")
                    continue

                category_name = input(CYAN + "Novo nome da categoria: " + RESET)
                category_description = input(CYAN + "Nova descrição da categoria: " + RESET)
                update_category(category_id, category_name, category_description)

            case 5:
                print(f"{YELLOW}Voltando ao menu principal...{RESET}")
                user = get_logged_user()
                if user:
                    from app.admin.mainAdmin import main_admin
                    main_admin(user)
                return

            case _:
                print(f"{RED}Opção inválida! Digite somente números 1, 2, 3, 4 ou 5.{RESET}\n")
