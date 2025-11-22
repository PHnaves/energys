from app.users.cartMenu import cart_menu
from cart.addToCart import add_to_cart
from products.readProduct import read_product
from products.showProducts import show_products
from users.sessionUser import get_logged_user
from style.colors import CYAN, GREEN, RED, RESET, YELLOW

def product_menu_user():
    while True:
        print(f"\n{GREEN}=== MENU DE PRODUTOS ==={RESET}")
        print(f"{CYAN}1 - Listar produtos{RESET}")
        print(f"{CYAN}2 - Comprar produtos{RESET}")
        print(f"{CYAN}3 - Pesquisar produto{RESET}")
        print(f"{CYAN}4 - Carrinho{RESET}")
        print(f"{CYAN}5 - Voltar ao menu principal{RESET}")

        try:
            option = int(input(GREEN + "\nEscolha uma opção: " + RESET))
        except ValueError:
            print(f"{RED}Opção inválida! Digite somente números 1, 2, 3, 4 ou 5.{RESET}\n")
            continue

        match option:
            case 1:
                products = show_products()
                if products:
                    print(f"\n{GREEN}=== PRODUTOS DISPONÍVEIS ==={RESET}")
                    for product in products:
                        print(f"{CYAN}ID:{RESET} {product['product_id']}")
                        print(f"{CYAN}Nome:{RESET} {product['product_name']}")
                        print(f"{CYAN}Preço:{RESET} R$ {product['product_price']}")
                        print(f"{CYAN}Unidade:{RESET} {product['product_unit']}")
                        print(f"{CYAN}Categoria:{RESET} {product['category_name']}")
                        print(f"{CYAN}Quantidade disponível:{RESET} {product['product_quantity']}\n")
                else:
                    print(f"{YELLOW}Nenhum produto cadastrado.{RESET}")

            case 2:
                print(f"\n{GREEN}=== COMPRA DE PRODUTOS ==={RESET}")
                while True:
                    try:
                        product_id = int(input(CYAN + "Digite o ID do produto: " + RESET))
                    except ValueError:
                        print(f"{RED}ID inválido! Digite apenas números inteiros.{RESET}")
                        continue

                    try:
                        quantity = int(input(CYAN + "Digite a quantidade desejada: " + RESET))
                    except ValueError:
                        print(f"{RED}Quantidade inválida! Digite apenas números inteiros.{RESET}")
                        continue

                    user = get_logged_user()
                    add_to_cart(quantity, user["user_id"], product_id)

                    while True:
                        isContinue = input(CYAN + "Deseja comprar outro produto? (S/N): " + RESET).upper()
                        if isContinue not in ["S", "N"]:
                            print(f"{RED}Opção inválida! Digite S ou N.{RESET}\n")
                        else:
                            break

                    if isContinue == "N":
                        break

            case 3:
                print(f"\n{GREEN}=== PESQUISA DE PRODUTOS ==={RESET}")
                try:
                    product_id = int(input(CYAN + "Digite o ID do produto: " + RESET))
                except ValueError:
                    print(f"{RED}ID inválido! Digite apenas números inteiros.{RESET}")
                    continue

                product = read_product(product_id)
                if product:
                    print(f"\n{GREEN}=== PRODUTO ENCONTRADO ==={RESET}")
                    print(f"{CYAN}ID:{RESET} {product['product_id']}")
                    print(f"{CYAN}Nome:{RESET} {product['product_name']}")
                    print(f"{CYAN}Preço:{RESET} R$ {product['product_price']}")
                    print(f"{CYAN}Unidade:{RESET} {product['product_unit']}")
                    print(f"{CYAN}Categoria:{RESET} {product['category_name']}")
                    print(f"{CYAN}Quantidade disponível:{RESET} {product['product_quantity']}")
                else:
                    print(f"{YELLOW}Nenhum produto encontrado.{RESET}")

            case 4:
                user = get_logged_user()
                if user:
                    cart_menu(user)

            case 5:
                print(f"{YELLOW}Voltando ao menu principal...{RESET}")
                user = get_logged_user()
                if user:
                    from app.users.userMenu import user_menu
                    user_menu(user)

            case _:
                print(f"{RED}Opção inválida! Tente novamente. Opções: 1, 2, 3, 4, 5.{RESET}\n")
