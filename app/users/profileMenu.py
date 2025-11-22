import bcrypt
from users.updateUser import update_user
from users.deleteUser import delete_user
from users.sessionUser import clear_session, set_logged_user
from users.readUser import get_user_by_id
from users.validationCpf import validation_cpf 
from style.colors import CYAN, GREEN, RED, RESET, YELLOW

def profile_menu(user):
    while True:
        user = get_user_by_id(user['user_id'])
        if not user:
            print(f"{RED}Usuário não encontrado. Voltando ao menu principal.{RESET}")
            from app.main import main 
            main()

        print(f"\n{GREEN}=== PERFIL DO USUÁRIO ({user['user_name']}) ==={RESET}")
        print(f"{CYAN}1 - Atualizar conta{RESET}")
        print(f"{CYAN}2 - Deletar conta{RESET}")
        print(f"{CYAN}3 - Ver meus dados{RESET}")
        print(f"{CYAN}4 - Logout{RESET}")
        print(f"{CYAN}5 - Voltar{RESET}")

        try:
            option = int(input(GREEN + "\nEscolha uma opção: " + RESET))
        except ValueError:
            print(f"{RED}Opção inválida! Tente novamente. Opções: 1, 2, 3, 4, 5.{RESET}\n")
            continue

        match option:
            case 1:
                print(f"\n{GREEN}=== ATUALIZAR CONTA ==={RESET}")
                print(f"{CYAN}1 - Nome{RESET}")
                print(f"{CYAN}2 - Email{RESET}")
                print(f"{CYAN}3 - Senha{RESET}")
                print(f"{CYAN}4 - CPF{RESET}")
                print(f"{CYAN}5 - Data de nascimento{RESET}")
                print(f"{CYAN}6 - Voltar{RESET}")

                try:
                    update_option = int(input(GREEN + "\nEscolha uma opção: " + RESET))
                except ValueError:
                    print(f"{RED}Opção inválida! Tente novamente. Opções: 1, 2, 3, 4, 5, 6.{RESET}\n")
                    continue
               
                match update_option:
                    case 1:
                        new_value = input(CYAN + "Novo nome: " + RESET)
                        update_user(user['user_id'], new_value, update_option)

                    case 2:
                        new_value = input(CYAN + "Novo email: " + RESET)
                        update_user(user['user_id'], new_value, update_option)

                    case 3:
                        old = input(CYAN + "Senha atual: " + RESET).encode('utf-8')
                        if not bcrypt.checkpw(old, user['user_password'].encode('utf-8')):
                            print(f"{RED}Senha atual incorreta!{RESET}")
                            continue

                        new_password = input(CYAN + "Nova senha: " + RESET)
                        update_user(user['user_id'], new_password, update_option)

                    case 4:
                        new_value = validation_cpf()
                        update_user(user['user_id'], new_value, update_option)

                    case 5:
                        new_value = input(CYAN + "Nova data de nascimento: " + RESET)
                        update_user(user['user_id'], new_value, update_option)

                    case 6:
                        continue

                    case _:
                        print(f"{RED}Opção inválida! Tente novamente.{RESET}")
                        continue

                updated_user = get_user_by_id(user['user_id'])
                set_logged_user(updated_user)

            case 2:
                confirm = input(CYAN + "Tem certeza que deseja deletar sua conta? (s/n): " + RESET).lower()
                if confirm == "s":
                    delete_user(user['user_id'])
                    clear_session()
                    print(f"{YELLOW}Conta deletada. Voltando à tela inicial...{RESET}")
                    from app.main import main 
                    main()
                    break

            case 3:
                print(f"\n{GREEN}=== SEUS DADOS ==={RESET}")
                print(f"{CYAN}Nome:{RESET} {user['user_name']}")
                print(f"{CYAN}Email:{RESET} {user['user_email']}")
                print(f"{CYAN}CPF:{RESET} {user['user_cpf']}")
                print(f"{CYAN}Data de nascimento:{RESET} {user['user_date_birth']}")

            case 4:
                clear_session()
                print(f"{YELLOW}Logout realizado com sucesso!{RESET}\n")
                from app.main import main  
                main()
            
            case 5:
                print(f"{YELLOW}Voltando ao menu principal...{RESET}")
                from app.users.userMenu import user_menu 
                user_menu(user)
                break

            case _:
                print(f"{RED}Opção inválida! Tente novamente. Opções: 1, 2, 3, 4, 5.{RESET}\n")
