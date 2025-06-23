
-- Drop tables if they exist
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

-- Customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    registration_date DATE
);

-- Products
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock INT
);

-- Orders
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Order Items
CREATE TABLE order_items (
    item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Sample data
INSERT INTO customers VALUES
(1, 'Alice', 'alice@example.com', '2024-01-15'),
(2, 'Bob', 'bob@example.com', '2024-02-10'),
(3, 'Charlie', 'charlie@example.com', '2024-03-05');

INSERT INTO products VALUES
(1, 'Laptop', 'Electronics', 1200.00, 15),
(2, 'Smartphone', 'Electronics', 800.00, 5),
(3, 'Desk Chair', 'Furniture', 150.00, 25),
(4, 'Monitor', 'Electronics', 300.00, 8),
(5, 'Notebook', 'Stationery', 5.00, 200);

INSERT INTO orders VALUES
(101, 1, '2024-05-10', 2000.00),
(102, 2, '2024-05-15', 950.00),
(103, 1, '2024-06-01', 305.00);

INSERT INTO order_items VALUES
(1001, 101, 1, 1, 1200.00),
(1002, 101, 2, 1, 800.00),
(1003, 102, 3, 1, 150.00),
(1004, 102, 5, 10, 5.00),
(1005, 103, 4, 1, 300.00),
(1006, 103, 5, 1, 5.00);
