use practice_db;

select * from orders;

INSERT INTO orders (order_id, customer_id, order_date, total_amount) VALUES
(6, 2, '2025-05-27', 120.00),
(7, 3, '2025-05-28', 180.00),
(8, 4, '2025-05-30', 250.00),
(9, 5, '2025-06-01', 175.75),
(10, 6, '2025-06-02', 99.00);

select curdate();
select curdate() - interval 7 day;

select *
from orders
where order_date >= curdate() - interval 7 day;

