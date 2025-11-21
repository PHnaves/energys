
from cart.removeToCart import remove_to_cart
from cart.showCart import show_cart
from cart.updateCart import update_cart
from users.readUser import get_user_by_id


def cart_menu(user):
    while True:
        user = get_user_by_id(user['user_id'])
        if not user:
            print("Usuário não encontrado. Voltando ao menu principal.")
            from app.main import main 
            main()

        print(f"\n=== CARRINHO DO USUÁRIO ({user['user_name']}) ===")
        print("1 - Ver carrinho")
        print("2 - Remover produto do carrinho")
        print("3 - Atualizar produto do carrinho")
        print("4 - Voltar")

        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida, tente novamente. Opções: 1, 2, 3\n")
            continue

        match option:
            case 1:
                print("\n=== CARRINHO ===")
                products = show_cart(user['user_id'])
                if products:
                    sum = 0
                    for product in products:
                        print(f"Quantidade: {product['quantity']}")
                        print(f"Nome: {product['product_name']}")
                        print(f"Preço: {product['product_price']}")
                        print(f"Unidade: {product['product_unit']}")
                        print(f"Categoria: {product['category_name']}\n")
                        sum += product['product_price'] * product['quantity']
                    print(f"Total: {sum}")

                else:
                    print("Nenhum produto no carrinho.")
            case 2:
                print("\n=== REMOVER PRODUTO DO CARRINHO ===")
                try:
                    product_id = int(input("Digite o ID do produto qie deseja remover: "))
                except ValueError:
                    print("ID inválido, tente novamente.")
                    continue
                remove_to_cart(user['user_id'], product_id)
            case 3:
                print("\n=== ATUALIZAR PRODUTO DO CARRINHO ===")
                try:
                    product_id = int(input("Digite o ID do produto qie deseja atualizar: "))
                except ValueError:
                    print("ID inválido, tente novamente.")
                    continue

                try:
                    new_quantity = int(input("Digite a nova quantidade: "))
                except ValueError:
                    print("Quantidade inválida, tente novamente.")
                    continue

                update_cart(new_quantity, user['user_id'], product_id)
            case 4:
                from app.users.productsMenuUser import product_menu_user  
                product_menu_user()
            case _:
                print("Opção inválida, tente novamente. Opções: 1, 2, 3\n")