from categories.showCategories import show_categories
from products.showProducts import show_products
from products.createProduct import create_product
from products.updateProduct import update_product
from products.deleteProduct import delete_product
from users.sessionUser import get_logged_user

def product_menu_admin():
    while True:
        print("\n=== MENU DE PRODUTOS ===")
        print("1 - Criar produto")
        print("2 - Listar produtos")
        print("3 - Excluir produto")
        print("4 - Atualizar produto")
        print("5 - Voltar ao menu principal")

        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida, tente novamente. Opções: 1, 2, 3, 4, 5\n")
            continue

        match option:
            case 1:
                print("\n=== CADASTRO DE PRODUTO ===")
                product_name = str(input("Nome do produto: "))
                try:
                    product_price = float(input("Preço do produto: "))
                except ValueError:
                    print("Preço inválido, digite somente numeros.")
                    continue
                while True:
                    product_unit = str(input("Unidade do produto UN, ML, L, G, KG: ")).upper()
                    if product_unit not in ["UN", "ML", "L", "G", "KG"]:
                        print("Unidade inválida, tente novamente. Opções: UN, ML, L, G, KG\n")
                    else:
                        break
                try:
                    product_quantity = int(input("Quantidade do produto: "))
                except ValueError:
                    print("Quantidade inválida, digite somente numeros inteiros.")
                    continue
                product_entry = product_quantity
                product_exit = 0
                print("\n=== SELECIONE A CATEGORIA DO PRODUTO ===")
                categories = show_categories()
                if categories:
                    for category in categories:
                        print(f"ID: {category['category_id']}")
                        print(f"Nome: {category['category_name']}")
                        print(f"Descrição: {category['category_description']}\n")
                    try:
                        fk_categories_category_id = int(input("ID da categoria: "))
                    except ValueError:
                        print("ID inválido, digite somente numeros inteiros.")
                        continue
                    create_product(product_name, product_price, product_unit, product_quantity, product_entry, product_exit, fk_categories_category_id)
                else:
                    print("Nenhuma categoria cadastrada. Para criar um produto, primeiro cadastre uma categoria.")
            case 2:
                products = show_products()
                if products:
                    print("\n=== LISTA DE PRODUTOS ===")
                    for product in products:
                        print(f"ID: {product['product_id']}")
                        print(f"Nome: {product['product_name']}")
                        print(f"Preço: {product['product_price']}")
                        print(f"Unidade: {product['product_unit']}")
                        print(f"Quantidade: {product['product_quantity']}")
                        print(f"Entrada: {product['product_entry']}")
                        print(f"Saida: {product['product_exit']}")
                        print(f"Categoria: {product['category_name']}\n")
                else:
                    print("Nenhum produto cadastrado.")
            case 3:
                print("\n=== EXCLUSÃO DE PRODUTO ===")
                try:
                    product_id = int(input("Digite o ID do produto que deseja excluir: "))
                except ValueError:
                    print("ID inválido, digite somente numeros inteiros.")
                    continue
                delete_product(product_id)
            case 4:
                print("\n=== ATUALIZAR PRODUTO ===")
                try:
                    product_id = int(input("Digite o ID do produto que deseja atualizar: "))
                except ValueError:
                    print("ID inválido, digite somente numeros inteiros.")
                    continue
                product_name = str(input("Novo nome do produto: "))
                try:
                    product_price = float(input("Novo preço do produto: "))
                except ValueError:
                    print("Preço inválido, digite somente numeros.")
                    continue
                while True:
                    product_unit = str(input("Unidade do produto UN, ML, L, G, KG: ")).upper()
                    if product_unit not in ["UN", "ML", "L", "G", "KG"]:
                        print("Unidade inválida, tente novamente. Opções: UN, ML, L, G, KG\n")
                    else:
                        break
                try:
                    product_quantity = int(input("Nova quantidade do produto: "))
                except ValueError:
                    print("Quantidade inválida, digite somente numeros inteiros.")
                    continue
                product_entry = product_quantity
                product_exit = 0
                print("\n=== SELECIONE A CATEGORIA DO PRODUTO ===")
                categories = show_categories()
                if categories:
                    for category in categories:
                        print(f"ID: {category['category_id']}")
                        print(f"Nome: {category['category_name']}")
                        print(f"Descrição: {category['category_description']}\n")
                    try:
                        fk_categories_category_id = int(input("Digite o ID da categoria: "))
                    except ValueError:
                        print("ID inválido, digite somente numeros inteiros.")
                        continue
                    update_product(product_id, product_name, product_price, product_unit, product_quantity, product_entry, product_exit, fk_categories_category_id)
                else:
                    print("Nenhuma categoria cadastrada. Para atualizar um produto, primeiro cadastre uma categoria.")
            case 5:
                print("Voltando ao menu principal...")
                user = get_logged_user()
                if user:
                    from app.admin.mainAdmin import main_admin
                    main_admin(user)
            case _:
                print("Opção inválida, tente novamente. Opções: 1, 2, 3\n")
           
                                   