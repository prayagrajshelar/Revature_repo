use practice_db;
create table employee_info(
empno int,
ename varchar(20),
dept varchar(20),
salary int,
comm int
);

insert into employee_info (empno, ename, dept, salary, comm) values
(1, 'ankit','hr',20000, 1200),
(2, 'sujeet','accounts', 24000, null),
(3, 'vijay', 'hr', 28000, 2000),
(4, 'nitin', 'sales', 18000, 3000),
(5, 'vikram', 'sales', 22000, 1700);


select ename, salary from employee_info
where ename like 'v%'
order by salary;

select * from employee_info
where dept = 'sales' and salary > 20000;


select COUNT(DISTINCT dept) AS distinct_dept_count
from employee_info;


update employee_info
set salary = 20000
where ename = 'nitin' and salary = 18000;


insert into employee_info (empno, ename, dept, salary, comm) values
(6, 'sumit', 'hr', 40000, 2000);


select avg(comm) from employee_info;

select ename, dept from employee_info
where dept in ('hr','account');

select ename, salary+100 as new_salary
from employee_info;