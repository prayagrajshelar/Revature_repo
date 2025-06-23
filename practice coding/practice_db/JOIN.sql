use practice_db;

create table emp(
emp_id int,
first_name varchar(20),
last_name varchar(20),
hire_date date,
salary float,
manager_id int,
department_id int
);

insert into emp (emp_id, first_name, last_name, hire_date, salary, manager_id, department_id)
values
(100, 'Prayagraj', 'Shelar', '2020-06-20', 25000, 102, 90),
(101, 'Abhishek', 'More', '2020-05-10', 25000, 103, 50),
(102, 'Sreehari', 'Itha', '2021-07-18', 30000, 101, 80);

create table department(
department_id int,
department_name varchar(20)
);
insert into department values(20,"sales"),
(50, "analysis"),
(80,"Developer"),
(90,"Data Engineer");

select e.first_name, e.last_name, d.department_name
from emp e join department d
where e.department_id = d.department_id;