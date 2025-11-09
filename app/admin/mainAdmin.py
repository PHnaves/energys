from app.admin.categoriesMenuAdmin import category_menu_admin
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

        option = input("Escolha uma opção: ")

        match option:
            case "1":
                print("Menu dos produtos")
            case "2":
                category_menu_admin()
            case "3":
                print("Saindo... Até mais!")
                from app.main import main
                main()
           
            case _:
                print("Opção inválida, tente novamente.\n")

