-- E-commerce sample database for text-to-SQL project
-- Run in MySQL Workbench after: CREATE DATABASE ecommerce; USE ecommerce;

USE ecommerce;

DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
  customer_id INT PRIMARY KEY AUTO_INCREMENT,
  customer_name VARCHAR(100) NOT NULL,
  state VARCHAR(50),
  city VARCHAR(50)
);

CREATE TABLE products (
  product_id INT PRIMARY KEY AUTO_INCREMENT,
  product_name VARCHAR(100) NOT NULL,
  category VARCHAR(50),
  price DECIMAL(10,2) NOT NULL
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date DATE NOT NULL,
  total_amount DECIMAL(12,2) NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
  item_id INT PRIMARY KEY AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  line_total DECIMAL(12,2) NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO customers (customer_name, state, city) VALUES
('Ravi Kumar', 'Andhra Pradesh', 'Visakhapatnam'),
('Priya Reddy', 'Andhra Pradesh', 'Vijayawada'),
('Amit Shah', 'Maharashtra', 'Mumbai'),
('Sneha Patel', 'Gujarat', 'Ahmedabad'),
('Karthik Nair', 'Kerala', 'Kochi'),
('Anita Das', 'West Bengal', 'Kolkata'),
('Rahul Verma', 'Delhi', 'New Delhi'),
('Meera Iyer', 'Tamil Nadu', 'Chennai');

INSERT INTO products (product_name, category, price) VALUES
('Wireless Mouse', 'Electronics', 899.00),
('USB-C Hub', 'Electronics', 1499.00),
('Office Chair', 'Furniture', 8999.00),
('Notebook Pack', 'Stationery', 299.00),
('Bluetooth Speaker', 'Electronics', 2499.00),
('Desk Lamp', 'Furniture', 1299.00),
('Water Bottle', 'Accessories', 499.00),
('Keyboard', 'Electronics', 1999.00);

INSERT INTO orders (customer_id, order_date, total_amount) VALUES
(1, '2025-01-05', 2398.00),
(1, '2025-02-12', 8999.00),
(2, '2025-01-18', 1499.00),
(2, '2025-03-02', 4998.00),
(3, '2025-01-22', 1999.00),
(3, '2025-02-28', 3798.00),
(4, '2025-02-05', 1299.00),
(4, '2025-03-15', 899.00),
(5, '2025-01-30', 2499.00),
(5, '2025-03-20', 1499.00),
(6, '2025-02-14', 299.00),
(6, '2025-03-08', 1999.00),
(7, '2025-01-10', 499.00),
(7, '2025-02-20', 2499.00),
(8, '2025-03-01', 8999.00),
(8, '2025-03-25', 1299.00),
(1, '2025-03-10', 1999.00),
(2, '2025-02-01', 899.00),
(3, '2025-03-18', 1499.00),
(4, '2025-01-28', 2499.00);

INSERT INTO order_items (order_id, product_id, quantity, line_total) VALUES
(1, 1, 2, 1798.00), (1, 4, 2, 598.00),
(2, 3, 1, 8999.00),
(3, 2, 1, 1499.00),
(4, 5, 2, 4998.00),
(5, 8, 1, 1999.00),
(6, 1, 1, 899.00), (6, 5, 1, 2499.00), (6, 7, 1, 499.00),
(7, 6, 1, 1299.00),
(8, 1, 1, 899.00),
(9, 5, 1, 2499.00),
(10, 2, 1, 1499.00),
(11, 4, 1, 299.00),
(12, 8, 1, 1999.00),
(13, 7, 1, 499.00),
(14, 5, 1, 2499.00),
(15, 3, 1, 8999.00),
(16, 6, 1, 1299.00),
(17, 8, 1, 1999.00),
(18, 1, 1, 899.00),
(19, 2, 1, 1499.00),
(20, 5, 1, 2499.00);
