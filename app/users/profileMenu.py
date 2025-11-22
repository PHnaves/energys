import bcrypt
from users.updateUser import update_user
from users.deleteUser import delete_user
from users.sessionUser import clear_session, set_logged_user
from users.readUser import get_user_by_id
from users.validationCpf import validation_cpf 

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

        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida, tente novamente. Opções: 1, 2, 3, 4, 5\n")
            continue

        match option:
            case 1:
                print("\n=== ATUALIZAR CONTA ===")
                print("1 - Nome")
                print("2 - Email")
                print("3 - Senha")
                print("4 - CPF")
                print("5 - Data de nascimento")
                print("6 - Voltar")

                try:
                    update_option = int(input("Escolha uma opção: "))
                except ValueError:
                    print("Opção inválida, tente novamente. Opções: 1, 2, 3, 4, 5\n")
                    continue
               
                match update_option:
                    case 1:
                        new_value = input("Novo nome: ")
                        update_user(user['user_id'], new_value, update_option)

                    case 2:
                        new_value = input("Novo email: ")
                        update_user(user['user_id'], new_value, update_option)

                    case 3:
                        old = input("Senha atual: ").encode('utf-8')
                        if not bcrypt.checkpw(old, user['user_password'].encode('utf-8')):
                            print("Senha atual incorreta.")
                            continue

                        new_password = input("Nova senha: ")
                        update_user(user['user_id'], new_password, update_option)

                    case 4:
                        new_value = validation_cpf()
                        update_user(user['user_id'], new_value, update_option)

                    case 5:
                        new_value = input("Nova data de nascimento: ")
                        update_user(user['user_id'], new_value, update_option)

                    case 6:
                        continue

                    case _:
                        print("Opção inválida, tente novamente. Opções: 1, 2, 3, 4, 5\n")
                        continue

                updated_user = get_user_by_id(user['user_id'])
                set_logged_user(updated_user)

            case 2:
                confirm = input("Tem certeza que deseja deletar sua conta? (s/n): ").lower()
                if confirm == "s":
                    delete_user(user['user_id'])
                    clear_session()
                    print("Conta deletada. Voltando a tela inicial...")
                    from app.main import main 
                    main()
                    break

            case 3:
                print("\n=== SEUS DADOS ===")
                print(f"Nome: {user['user_name']}")
                print(f"Email: {user['user_email']}")
                print(f"CPF: {user['user_cpf']}")
                print(f"Data de nascimento: {user['user_date_birth']}")

            case 4:
                clear_session()
                print("Logout realizado com sucesso!\n")
                from app.main import main  
                main()
            
            case 5:
                print("Voltando ao menu principal...")
                from app.users.userMenu import user_menu 
                user_menu(user)
                break

            case _:
                print("Opção inválida, tente novamente. Opções: 1, 2, 3\n")
