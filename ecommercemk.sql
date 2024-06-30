CREATE DATABASE ecommercemk;

USE ecommercemk;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    size VARCHAR(50) NOT NULL,
    units INT NOT NULL,
    discount BOOLEAN NOT NULL
);

INSERT INTO products (name, price, size, units, discount) VALUES
('Beige Linen T-Shirt', 19.99, 'M', 50, FALSE),
('Black Cotton T-Shirt', 21.99, 'L', 40, FALSE),
('White V-Neck T-Shirt', 18.99, 'XL', 35, FALSE),
('Blue Striped T-Shirt', 22.99, 'S', 30, TRUE),
('Red Polo T-Shirt', 24.99, 'M', 25, TRUE),
('Green Graphic T-Shirt', 20.99, 'L', 20, TRUE),
('Dark Blue Denim Jeans', 49.99, 'M', 20, FALSE),
('Black Slim Fit Jeans', 54.99, 'L', 20, FALSE),
('Gray Straight Leg Jeans', 47.99, 'XL', 15, FALSE),
('Light Blue Skinny Jeans', 52.99, 'S', 25, TRUE),
('White Flared Jeans', 55.99, 'M', 20, TRUE),
('Black Bootcut Jeans', 53.99, 'L', 15, TRUE),
('Brown Leather Jacket', 89.99, 'M', 10, FALSE),
('Black Bomber Jacket', 95.99, 'L', 10, FALSE),
('Green Parka Jacket', 99.99, 'XL', 5, FALSE),
('Red Trench Coat', 109.99, 'S', 15, TRUE),
('Blue Denim Jacket', 79.99, 'M', 15, TRUE),
('Black Biker Jacket', 119.99, 'L', 10, TRUE),
('White Running Shoes', 59.99, '8', 20, TRUE),
('Black Leather Shoes', 69.99, '9', 20, TRUE),
('Red Canvas Shoes', 49.99, '10', 15, TRUE),
('Blue High Heels', 75.99, '6', 25, FALSE),
('Pink Ballet Flats', 45.99, '7', 20, FALSE),
('Black Ankle Boots', 89.99, '8', 15, FALSE),
('Beige Fedora Hat', 15.99, 'M', 50, TRUE),
('Black Baseball Cap', 17.99, 'L', 40, TRUE),
('Gray Beanie', 12.99, 'S', 30, FALSE),
('White Sun Hat', 18.99, 'M', 25, FALSE),
('Blue Winter Hat', 22.99, 'L', 20, FALSE),
('White Athletic Socks', 5.99, 'One Size', 100, TRUE),
('Black Dress Socks', 7.99, 'One Size', 100, TRUE),
('Red Wool Socks', 9.99, 'One Size', 100, TRUE),
('Blue Striped Socks', 6.99, 'One Size', 100, TRUE),
('Gray Ankle Socks', 4.99, 'One Size', 100, TRUE);
