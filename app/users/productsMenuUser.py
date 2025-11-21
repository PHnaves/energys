from app.users.cartMenu import cart_menu
from cart.addToCart import add_to_cart
from products.readProduct import read_product
from products.showProducts import show_products
from users.sessionUser import get_logged_user

def product_menu_user():
    while True:
        print("\n=== MENU DE PRODUTOS ===")
        print("1 - Listar produtos")
        print("2 - Comprar produtos")
        print("3 - Pesquisar produto")
        print("4 - Carrinho")
        print("5 - Voltar ao menu principal")

        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida, tente novamente. Opções: 1, 2, 3, 4, 5\n")
            continue

        match option:
            case 1:
                products = show_products()
                if products:
                    print("\n=== PRODUTOS DISPONIVEIS===")
                    for product in products:
                        print(f"ID: {product['product_id']}")
                        print(f"Nome: {product['product_name']}")
                        print(f"Preço: {product['product_price']}")
                        print(f"Unidade: {product['product_unit']}")
                        print(f"Categoria: {product['category_name']}\n")
                        print(f"Quantidade disponível: {product['product_quantity']}\n")
                else:
                    print("Nenhum produto cadastrado.")
            case 2:
                print("\n=== COMPRA DE PRODUTOS ===")
                while True:
                    try:
                        product_id = int(input("Digite o ID do produto: "))
                    except ValueError:
                        print("ID inválido, digite somente numeros inteiros.")
                        continue

                    try:
                        quantity = int(input("Digite a quantidade desejada: "))
                    except ValueError:
                        print("Quantidade inválida, digite somente numeros inteiros.")
                        continue

                    user = get_logged_user()
                    add_to_cart(quantity, user["user_id"], product_id)
                    
                    while True:
                        isContinue = input("Deseja comprar outro produto? (S/N): ").upper()
                        if isContinue not in ["S", "N"]:
                            print("Opção inválida, tente novamente. Opções: S, N\n")
                        else:
                            break

                    if isContinue == "N":
                        break
            case 3:
                print("\n=== PESQUISA DE PRODUTOS ===")
                try:
                    product_id = int(input("Digite o ID do produto: "))
                except ValueError:
                    print("ID inválido, digite somente numeros inteiros.")
                    continue

                product = read_product(product_id)
                if product:
                    print("\n=== PRODUTO ENCONTRADO ===")
                    print(f"ID: {product['product_id']}")
                    print(f"Nome: {product['product_name']}")
                    print(f"Preço: {product['product_price']}")
                    print(f"Unidade: {product['product_unit']}")
                    print(f"Categoria: {product['category_name']}\n")
                    print(f"Quantidade disponível: {product['product_quantity']}")
                else:   
                    print("Nenhum produto encontrado.")
            case 4:
                user = get_logged_user()
                if user:
                    cart_menu(user)
            case 5:
                print("Voltar ao menu principal")
                user = get_logged_user()
                if user:
                    from app.users.userMenu import user_menu
                    user_menu(user)
            case _:
                print("Opção inválida, tente novamente. Opções: 1, 2, 3\n")
