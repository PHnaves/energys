from users.updateUser import update_user
from users.deleteUser import delete_user
from users.sessionUser import clear_session, set_logged_user
from users.readUser import get_user_by_id 

def profile_menu(user):
    while True:
        user = get_user_by_id(user['user_id'])
        if not user:
            print("Usuário não encontrado. Voltando ao menu principal.")
            from app.main import main 
            main()

        print(f"\n=== PERFIL DO USUÁRIO ({user['user_name']}) ===")
        print("1 - Atualizar conta")
        print("2 - Deletar conta")
        print("3 - Ver meus dados")
        print("4 - Logout")
        print("5 - Voltar")

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
                    print("Conta deletada. Voltando a tela inicial...")
                    from app.main import main 
                    main()
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
                from app.main import main  
                main()
            
            case "5":
                print("Voltando ao menu principal...")
                from app.users.userMenu import user_menu 
                user_menu(user)
                break

            case _:
                print("Opção inválida, tente novamente.")
