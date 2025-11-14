from users.readUser import get_user_by_id
from app.users.profileMenu import profile_menu

# MENU PRINCIPAL
def user_menu(user):
    while True:
        user = get_user_by_id(user['user_id'])
        if not user:
            print("Usuário não encontrado.")
            from app.main import main
            main()

        print(f"\n=== BEM VINDO(A) DE VOLTA, ({user['user_name']}) ===")
        print("1 - Perfil")
        print("2 - Produtos")
        print("3 - Sair")

        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida, tente novamente. Opções: 1, 2, 3\n")
            continue

        match option:
            case "1":
                profile_menu(user)
            case "2":
                print("Menu dos produtos")
            case "3":
                print("Saindo... Até mais!")
                break
            case _:
                print("Opção inválida, tente novamente.\n")