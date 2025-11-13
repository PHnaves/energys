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

        option = input("Escolha uma opção: ")

        match option:
            case "1":
                print("\n=== CADASTRO DE PRODUTO ===")
                product_name = input("Nome do produto: ")
                product_price = input("Preço do produto: ")
                product_unit = input("Unidade do produto KG ou ML: ")
                product_quantity = input("Quantidade do produto: ")
                product_entry = product_quantity
                product_exit = 0
                print("\n=== SELECIONE A CATEGORIA DO PRODUTO ===")
                categories = show_categories()
                if categories:
                    for category in categories:
                        print(f"ID: {category['category_id']}")
                        print(f"Nome: {category['category_name']}")
                        print(f"Descrição: {category['category_description']}\n")
                    fk_categories_category_id = input("Digite o ID da categoria: ")
                    create_product(product_name, product_price, product_unit, product_quantity, product_entry, product_exit, fk_categories_category_id)
                else:
                    print("Nenhuma categoria cadastrada. Para criar um produto, primeiro cadastre uma categoria.")
            case "2":
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
            case "3":
                product_id = input("Digite o ID do produto que deseja excluir: ")
                delete_product(product_id)
            case "4":
                print("\n=== ATUALIZAR PRODUTO ===")
                product_id = input("Digite o ID do produto que deseja atualizar: ")
                product_name = input("Novo nome do produto: ")
                product_price = input("Novo preço do produto: ")
                product_unit = input("Nova unidade do produto: ")
                product_quantity = input("Nova quantidade do produto: ")
                product_entry = product_quantity
                product_exit = 0
                print("\n=== SELECIONE A CATEGORIA DO PRODUTO ===")
                categories = show_categories()
                if categories:
                    for category in categories:
                        print(f"ID: {category['category_id']}")
                        print(f"Nome: {category['category_name']}")
                        print(f"Descrição: {category['category_description']}\n")
                    fk_categories_category_id = input("Digite o ID da categoria: ")
                    update_product(product_id, product_name, product_price, product_unit, product_quantity, product_entry, product_exit, fk_categories_category_id)
                else:
                    print("Nenhuma categoria cadastrada. Para atualizar um produto, primeiro cadastre uma categoria.")
            case "5":
                print("Voltando ao menu principal...")
                user = get_logged_user()
                if user:
                    from app.admin.mainAdmin import main_admin
                    main_admin(user)
            case _:
                print("Opção inválida, tente novamente.\n")
           
                                   