from app.admin.categoriesMenuAdmin import category_menu_admin
from app.admin.productsMenuAdmin import product_menu_admin
from users.readUser import get_user_by_id

# MENU PRINCIPAL ADM
def main_admin(user):
    while True:
        user = get_user_by_id(user['user_id'])
        if not user:
            print("Usuário não encontrado.")
            from app.main import main
            main()

        print(f"\n=== BEM VINDO(A) DE VOLTA ADM, ({user['user_name']}) ===")
        print("1 - Menu dos produtos")
        print("2 - Menu das categorias")
        print("3 - Sair")

        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida, tente novamente. Opções: 1, 2, 3, 4, 5\n")
            continue

        match option:
            case "1":
                product_menu_admin()
            case "2":
                category_menu_admin()
            case "3":
                print("Saindo... Até mais!")
                from app.main import main
                main()
           
            case _:
                print("Opção inválida, tente novamente.\n")

