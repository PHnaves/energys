from categories.showCategories import show_categories
from products.showProducts import show_products
from products.createProduct import create_product
from products.updateProduct import update_product
from products.deleteProduct import delete_product
from style.colors import CYAN, YELLOW, GREEN, RED, RESET
from users.sessionUser import get_logged_user

def product_menu_admin():
    while True:
        print(f"\n{GREEN}=== MENU DE PRODUTOS ADMIN ==={RESET}")

        print(f"{CYAN}1 - Criar produto{RESET}")
        print(f"{CYAN}2 - Listar produtos{RESET}")
        print(f"{CYAN}3 - Excluir produto{RESET}")
        print(f"{CYAN}4 - Atualizar produto{RESET}")
        print(f"{CYAN}5 - Voltar ao menu principal{RESET}")

        try:
            option = int(input(GREEN + "\nEscolha uma opção: " + RESET))
        except ValueError:
            print(f"{RED}Opção inválida! Digite números de 1 a 5.{RESET}\n")
            continue

        match option:
            # ---------------------------------------------------------
            # Criar Produto
            # ---------------------------------------------------------
            case 1:
                print(f"\n{GREEN}=== CADASTRO DE PRODUTO ==={RESET}")
                
                product_name = input(CYAN + "Nome do produto: " + RESET)
                
                try:
                    product_price = float(input(CYAN + "Preço do produto: " + RESET))
                except ValueError:
                    print(f"{RED}Preço inválido! Digite apenas números.{RESET}")
                    continue

                while True:
                    product_unit = input(CYAN + "Unidade (UN, ML, L, G, KG): " + RESET).upper()
                    if product_unit not in ["UN", "ML", "L", "G", "KG"]:
                        print(f"{RED}Unidade inválida! Opções: UN, ML, L, G, KG.{RESET}")
                    else:
                        break

                try:
                    product_quantity = int(input(CYAN + "Quantidade do produto: " + RESET))
                except ValueError:
                    print(f"{RED}Quantidade inválida! Digite apenas números inteiros.{RESET}")
                    continue

                product_entry = product_quantity
                product_exit = 0

                print(f"\n{GREEN}=== SELECIONE A CATEGORIA ==={RESET}")
                categories = show_categories()

                if categories:
                    for category in categories:
                        print(f"{CYAN}ID:{RESET} {category['category_id']}")
                        print(f"{CYAN}Nome:{RESET} {category['category_name']}")
                        print(f"{CYAN}Descrição:{RESET} {category['category_description']}\n")

                    try:
                        fk_categories_category_id = int(input(CYAN + "ID da categoria: " + RESET))
                    except ValueError:
                        print(f"{RED}ID inválido! Digite apenas números.{RESET}")
                        continue

                    create_product(product_name, product_price, product_unit,
                                   product_quantity, product_entry, product_exit,
                                   fk_categories_category_id)
                else:
                    print(f"{YELLOW}Nenhuma categoria cadastrada! Cadastre uma categoria primeiro.{RESET}")

            # ---------------------------------------------------------
            # Listar Produtos
            # ---------------------------------------------------------
            case 2:
                products = show_products()

                if products:
                    print(f"\n{GREEN}=== LISTA DE PRODUTOS ==={RESET}")
                    for product in products:
                        print(f"{CYAN}ID:{RESET} {product['product_id']}")
                        print(f"{CYAN}Nome:{RESET} {product['product_name']}")
                        print(f"{CYAN}Preço:{RESET} {product['product_price']}")
                        print(f"{CYAN}Unidade:{RESET} {product['product_unit']}")
                        print(f"{CYAN}Quantidade:{RESET} {product['product_quantity']}")
                        print(f"{CYAN}Entrada:{RESET} {product['product_entry']}")
                        print(f"{CYAN}Saída:{RESET} {product['product_exit']}")
                        print(f"{CYAN}Categoria:{RESET} {product['category_name']}\n")
                else:
                    print(f"{YELLOW}Nenhum produto cadastrado.{RESET}")

            # ---------------------------------------------------------
            # Excluir Produto
            # ---------------------------------------------------------
            case 3:
                print(f"\n{GREEN}=== EXCLUSÃO DE PRODUTO ==={RESET}")
                try:
                    product_id = int(input(CYAN + "ID do produto: " + RESET))
                except ValueError:
                    print(f"{RED}ID inválido! Digite apenas números inteiros.{RESET}")
                    continue

                delete_product(product_id)

            # ---------------------------------------------------------
            # Atualizar Produto
            # ---------------------------------------------------------
            case 4:
                print(f"\n{GREEN}=== ATUALIZAR PRODUTO ==={RESET}")
                try:
                    product_id = int(input(CYAN + "ID do produto: " + RESET))
                except ValueError:
                    print(f"{RED}ID inválido! Digite apenas números inteiros.{RESET}")
                    continue

                product_name = input(CYAN + "Novo nome do produto: " + RESET)

                try:
                    product_price = float(input(CYAN + "Novo preço: " + RESET))
                except ValueError:
                    print(f"{RED}Preço inválido! Digite apenas números.{RESET}")
                    continue

                while True:
                    product_unit = input(CYAN + "Unidade (UN, ML, L, G, KG): " + RESET).upper()
                    if product_unit not in ["UN", "ML", "L", "G", "KG"]:
                        print(f"{RED}Unidade inválida! Opções: UN, ML, L, G, KG.{RESET}")
                    else:
                        break

                try:
                    product_quantity = int(input(CYAN + "Nova quantidade: " + RESET))
                except ValueError:
                    print(f"{RED}Quantidade inválida! Digite apenas números inteiros.{RESET}")
                    continue

                product_entry = product_quantity
                product_exit = 0

                print(f"\n{GREEN}=== SELECIONE A NOVA CATEGORIA ==={RESET}")

                categories = show_categories()

                if categories:
                    for category in categories:
                        print(f"{CYAN}ID:{RESET} {category['category_id']}")
                        print(f"{CYAN}Nome:{RESET} {category['category_name']}")
                        print(f"{CYAN}Descrição:{RESET} {category['category_description']}\n")

                    try:
                        fk_categories_category_id = int(input(CYAN + "ID da categoria: " + RESET))
                    except ValueError:
                        print(f"{RED}ID inválido! Digite apenas números.{RESET}")
                        continue

                    update_product(product_id, product_name, product_price, product_unit,
                                   product_quantity, product_entry, product_exit,
                                   fk_categories_category_id)
                else:
                    print(f"{YELLOW}Nenhuma categoria cadastrada! Cadastre uma categoria primeiro.{RESET}")

            # ---------------------------------------------------------
            # Voltar ao menu principal
            # ---------------------------------------------------------
            case 5:
                print(f"{YELLOW}Voltando ao menu principal...{RESET}")
                user = get_logged_user()
                if user:
                    from app.admin.mainAdmin import main_admin
                    main_admin(user)
                return

            case _:
                print(f"{RED}Opção inválida! Digite somente números de 1 a 5.{RESET}\n")
