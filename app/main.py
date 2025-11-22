from app.admin.mainAdmin import main_admin
from app.users.userMenu import user_menu
from style.colors import CYAN, GREEN, RED, RESET
from users.createUser import create_user
from users.loginUser import login_user
from users.sessionUser import get_logged_user
from users.validationCpf import validation_cpf

def main():
    while True:
        print(GREEN + "\n╔" + "═" * 38 + "╗")
        print("║        BEM-VINDO(A) À ENERGYS        ║")
        print("╚" + "═" * 38 + "╝" + RESET)

        print(f"{CYAN}1 - Login{RESET}")
        print(f"{CYAN}2 - Cadastro{RESET}")
        print(f"{CYAN}3 - Sair{RESET}")

        try:
            option = int(input(GREEN + "\nEscolha uma opção: " + RESET))
        except ValueError:
            print(f"{RED}Opção inválida! Digite somente números 1, 2, ou 3.{RESET}\n")
            continue
    
        match option:
            case 1:
                print(f"\n{GREEN}=== LOGIN ==={RESET}")
                email = input(CYAN + "Email: " + RESET)
                password = input(CYAN + "Senha: " + RESET).encode('utf-8')
                
                login_user(email, password)

                user = get_logged_user()
                if user:
                    if user["type_user"] == "ADM":
                        main_admin(user)
                    else:
                        user_menu(user)

            case 2:
                print(f"\n{GREEN}=== CADASTRO ==={RESET}")
                user_name = input(CYAN + "Nome: " + RESET)
                user_email = input(CYAN + "Email: " + RESET)
                user_password = input(CYAN + "Senha: " + RESET).encode('utf-8')
                user_cpf = validation_cpf()
                user_date_birth = input(CYAN + "Data de nascimento (AAAA-MM-DD): " + RESET)

                create_user(user_name, user_email, user_password, user_cpf, user_date_birth)

            case 3:
                print(f"{GREEN}Saindo... Até mais! 👋{RESET}")
                break

            case _:
                print(RED + "❌ Opção inválida, tente novamente!\n" + RESET)


if __name__ == "__main__":
    main()
