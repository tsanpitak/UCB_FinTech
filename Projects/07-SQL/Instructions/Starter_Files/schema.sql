-- Clean DB
DROP TABLE IF EXISTS card_holder CASCADE;
DROP TABLE IF EXISTS credit_card CASCADE;
DROP TABLE IF EXISTS merchant_category CASCADE;
DROP TABLE IF EXISTS merchant CASCADE;
DROP TABLE IF EXISTS transactions CASCADE;

-- Create Tables
CREATE TABLE card_holder(
	card_holder_id INT PRIMARY KEY NOT NULL,
	card_holder_name VARCHAR(255)
);

CREATE TABLE credit_card(
	card_id VARCHAR(20) PRIMARY KEY NOT NULL,
	card_holder_id INT NOT NULL,
	FOREIGN KEY (card_holder_id) REFERENCES card_holder(card_holder_id)
);

CREATE TABLE merchant_category(
	merchant_cat_id INT PRIMARY KEY NOT NULL,
	merchant_cat_desc VARCHAR(255)
);

CREATE TABLE merchant(
	merchant_id INT PRIMARY KEY NOT NULL,
	merchant_name VARCHAR(255),
	merchant_cat_id INT,
	FOREIGN KEY (merchant_cat_id) REFERENCES merchant_category(merchant_cat_id)
);

CREATE TABLE transactions(
    transac_id INT PRIMARY KEY NOT NULL,
    transac_timestamp TIMESTAMP,
    amount DECIMAL,
    card_id VARCHAR(20),
    FOREIGN KEY (card_id) REFERENCES credit_card(card_id),
    merchant_id INT,
    FOREIGN KEY (merchant_id) REFERENCES merchant(merchant_id)
)