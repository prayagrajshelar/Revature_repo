use practice_db;
create table occupations(
name varchar(50),
occupation varchar(50)
);

INSERT INTO occupations (Name, Occupation) VALUES
('Jenny', 'Doctor'),
('Samantha', 'Doctor'),
('Ashley', 'Professor'),
('Christeen', 'Professor'),
('Ketty', 'Professor'),
('Meera', 'Singer'),
('Priya', 'Singer'),
('Jane', 'Actor'),
('Julia', 'Actor'),
('Maria', 'Actor');


select 
	max(case when occupation = "Doctor" then name end) as Doctor,
	max(case when occupation = "Professor" then name end) as Professor,
	max(case when occupation = "Singer" then name end) as Singer,
	max(case when occupation = "Actor" then name end) as Actor
from (
	select name, occupation,
    ROW_NUMBER() over (partition by occupation order by name) as row_num
    from occupations
) as ordered_occupations
group by row_num
order by row_num;