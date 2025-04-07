use dataAnalytics;

create table users (
	userID int auto_increment primary key,   -- unique identifier for each record
    username varchar(150) unique not null,   -- 
    email varchar(100) unique not null,
    passwordHash varchar(255) not null,      -- stores hashed password not null
    FirstName varchar(255),
    LastName varchar(255),
    DateOFBirth Date,
    createdAt datetime default current_timestamp,   -- date the user was created, default is current time 
    lastLogin datetime,                            -- last login 
    status enum("Active", "Inactive", "Suspended") default "Active",   -- status of account
    index (email)                                                      -- index on email column to speed up searches
);

select * from users;

insert into users (username, email, passwordHash, FirstName, LastName, DateOfBirth, createdAt, lastLogin)
values("Prayagraj", "pshelar@gmail.com", "Password##", "Prayagraj", "Shelar", "2003-01-01", now(), now());

insert into users (username, email, passwordHash, FirstName, LastName, DateOfBirth, createdAt, lastLogin)
values("Abhishek", "abhi@gmail.com", "hello_world##","Abhishek", "More", "2002-8-21", now(), "2024-9-8 12:22:3");


create table student (
	studentID int auto_increment primary key,
	stud_name varchar(200) unique not null,
    age int check( age > 18),
    course varchar(200)
);
create table Employment (
	employIdD int Primary key,
    studentID int,
    course_id int,
    foreign key (studentID) references student(studentID)
);

insert into student(stud_name, age, course) values ("Prayagraj", 19, "Data analyst");
insert into student(stud_name, age, course) values ("Nikhilesh", 19, "Full stack");

insert into employment(employIdD, studentID, course_id ) values (01, 1, 20);
select * from student;
select * from employment;

update student set age = 20 where stud_name = "Nikhilesh";


create table orderDetails(
	order_id int,
    product_id int,
    quantity int,
    primary key(order_id, product_id)
);
drop table persons;

