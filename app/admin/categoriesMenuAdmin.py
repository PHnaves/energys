from categories.createCategory import create_category
from categories.showCategories import show_categories
from categories.updateCategory import update_category
from categories.deleteCategory import delete_category
from users.sessionUser import get_logged_user

def category_menu_admin():
    while True:
        print("\n=== MENU DE CATEGORIAS ADMIN ===")
        print("1 - Criar categoria")
        print("2 - Listar categorias")
        print("3 - Excluir categoria")
        print("4 - Atualizar categoria")
        print("5 - Voltar ao menu principal")

        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida, tente novamente. Opções: 1, 2, 3, 4, 5\n")
            continue

        match option:
            case 1:
                print("\n=== CADASTRO DE CATEGORIA ===")
                category_name = str(input("Nome da categoria: "))
                category_description = str(input("Descrição da categoria: "))
                create_category(category_name, category_description)
            case 2:
                categories = show_categories()
                if categories:
                    print("\n=== LISTA DE CATEGORIAS ===")
                    for category in categories:
                        print(f"ID: {category['category_id']}")
                        print(f"Nome: {category['category_name']}")
                        print(f"Descrição: {category['category_description']}\n")
                else:
                    print("Nenhuma categoria cadastrada.")
            case 3:
                print("\n=== EXCLUSÃO DE CATEGORIA ===")
                try:
                    category_id = int(input("Digite o ID da categoria que deseja excluir: "))
                except ValueError:
                    print("Opção inválida, digite somente numeros inteiros\n")
                    continue
                delete_category(category_id)
            case 4:
                print("\n=== ATUALIZAR CATEGORIA ===")
                try:
                    category_id = int(input("Digite o ID da categoria que deseja atualizar: "))
                except ValueError:
                    print("Opção inválida, digite somente numeros inteiros\n")
                    continue
                category_name = str(input("Novo nome da categoria: "))
                category_description = str(input("Nova descrição da categoria: "))
                update_category(category_id, category_name, category_description)
            case 5:
                print("Voltando ao menu principal...")
                user = get_logged_user()
                if user:
                    from app.admin.mainAdmin import main_admin
                    main_admin(user)
            case _:
                print("Opção inválida, tente novamente. Opções: 1, 2, 3\n")
           