from cart.removeToCart import remove_to_cart
from cart.showCart import show_cart
from cart.updateCart import update_cart
from users.readUser import get_user_by_id
from style.colors import CYAN, GREEN, RED, RESET, YELLOW

def cart_menu(user):
    while True:
        user = get_user_by_id(user['user_id'])
        if not user:
            print(f"{RED}Usuário não encontrado. Voltando ao menu principal.{RESET}")
            from app.main import main 
            main()

        print(f"\n{GREEN}=== CARRINHO DO USUÁRIO ({user['user_name']}) ==={RESET}")
        print(f"{CYAN}1 - Ver carrinho{RESET}")
        print(f"{CYAN}2 - Remover produto do carrinho{RESET}")
        print(f"{CYAN}3 - Atualizar produto do carrinho{RESET}")
        print(f"{CYAN}4 - Voltar{RESET}")

        try:
            option = int(input(GREEN + "\nEscolha uma opção: " + RESET))
        except ValueError:
            print(f"{RED}Opção inválida! Tente novamente. Opções: 1, 2, 3, 4.{RESET}\n")
            continue

        match option:
            case 1:
                print(f"\n{GREEN}=== CARRINHO ==={RESET}")
                products = show_cart(user['user_id'])

                if products:
                    total = 0
                    for product in products:
                        print(f"{CYAN}Quantidade:{RESET} {product['quantity']}")
                        print(f"{CYAN}Nome:{RESET} {product['product_name']}")
                        print(f"{CYAN}Preço:{RESET} R$ {product['product_price']}")
                        print(f"{CYAN}Unidade:{RESET} {product['product_unit']}")
                        print(f"{CYAN}Categoria:{RESET} {product['category_name']}\n")

                        total += product['product_price'] * product['quantity']

                    print(f"{GREEN}Total: R$ {total}{RESET}")

                else:
                    print(f"{YELLOW}Nenhum produto no carrinho.{RESET}")

            case 2:
                print(f"\n{GREEN}=== REMOVER PRODUTO DO CARRINHO ==={RESET}")
                try:
                    product_id = int(input(CYAN + "Digite o ID do produto que deseja remover: " + RESET))
                except ValueError:
                    print(f"{RED}ID inválido! Tente novamente.{RESET}")
                    continue

                remove_to_cart(user['user_id'], product_id)

            case 3:
                print(f"\n{GREEN}=== ATUALIZAR PRODUTO DO CARRINHO ==={RESET}")
                try:
                    product_id = int(input(CYAN + "Digite o ID do produto que deseja atualizar: " + RESET))
                except ValueError:
                    print(f"{RED}ID inválido! Tente novamente.{RESET}")
                    continue

                try:
                    new_quantity = int(input(CYAN + "Digite a nova quantidade: " + RESET))
                except ValueError:
                    print(f"{RED}Quantidade inválida! Tente novamente.{RESET}")
                    continue

                update_cart(new_quantity, user['user_id'], product_id)

            case 4:
                from app.users.productsMenuUser import product_menu_user  
                product_menu_user()

            case _:
                print(f"{RED}Opção inválida! Tente novamente. Opções: 1, 2, 3, 4.{RESET}\n")
