CREATE DATABASE foodiehub;
USE foodiehub;

CREATE TABLE menu_items (
    itemid INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    price DECIMAL (6,2)
);

INSERT INTO menu_items (name,price) VALUES 
('Briyani',180),
('paneer butter masala',150)
('Butter chicken',220),
('Veg meals',110),
('Pizza',210);

CREATE TABLE orders (
    orderid INT PRIMARY KEY AUTO_INCREMENT,
    items VARCHAR(200),
    address VARCHAR(100)
);