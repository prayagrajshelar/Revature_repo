use practice_db;
SELECT * FROM practice_db.emp;

insert into emp values
(103, "Prayagraj", "Shelar","2020-06-20",25000,102,90);


SELECT first_name, last_name, COUNT(*)
FROM emp
GROUP BY first_name, last_name
HAVING COUNT(*) > 1;

