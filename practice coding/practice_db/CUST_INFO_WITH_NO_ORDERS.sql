use practice_db;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO customers (customer_id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie'),
(4, 'Diana'),
(5, 'Ethan'),
(6, 'Fiona'),
(7, 'George'),
(8, 'Hannah');


select c.customer_id, c.name
from customers c left join orders o
on c.customer_id = o.customer_id 
and o.order_date >= curdate() - interval 3 month
where o.order_id is null;