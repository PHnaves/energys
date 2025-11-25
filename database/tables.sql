-- tabelas do banco de dados

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    product_price DECIMAL(10,2) NOT NULL,
    product_unit ENUM("UN", "ML", "L", "G", "KG") NOT NULL,
    product_quantity INT NOT NULL,
    product_entry INT NOT NULL,
    product_exit INT NOT NULL,
    fk_categories_category_id INT
);

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL,
    category_description TEXT NOT NULL
);

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) NOT NULL UNIQUE,
    user_password VARCHAR(255) NOT NULL,
    user_cpf VARCHAR(255) NOT NULL,
    user_date_birth DATE NOT NULL,
    type_user ENUM("ADM", "COMUM") DEFAULT "COMUM"
);

CREATE TABLE use_pro (
	id INT AUTO_INCREMENT PRIMARY KEY,
    quantity INT NOT NULL,
    fk_users_user_id INT,
    fk_products_product_id INT
);
 
ALTER TABLE products ADD CONSTRAINT FK_products_2
    FOREIGN KEY (fk_categories_category_id)
    REFERENCES categories (category_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
 
ALTER TABLE use_pro ADD CONSTRAINT FK_use_pro_1
    FOREIGN KEY (fk_users_user_id)
    REFERENCES users (user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
 
ALTER TABLE use_pro ADD CONSTRAINT FK_use_pro_2
    FOREIGN KEY (fk_products_product_id)
    REFERENCES products (product_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;