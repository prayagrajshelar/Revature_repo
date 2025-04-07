create database dataAnalytics;
show databases;
use dataAnalytics;
create table Persons(
PersonID int,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255)
);

insert into Persons values(01, "Shelar", "Prayagraj", "Solapur, Maharashtra", "Chennai");

insert into Persons values
(13, "Dikshit", "Sai", "Andhra Pradesh", "Chennai"),
(14, "Mohammad", "Abdul", "Haidrabad", "Chennai")
;
select * from Persons;
SET SQL_SAFE_UPDATES = 0;

delete from Persons where PersonID = 1;
delete from Persons where PersonID = 13;

insert into Persons values(01, "Shelar", "Prayagraj", "Pune, Maharashtra", "Chennai");
select * from Persons;

update Persons set LastName = "Shaikh" where personID = 14;
delete from Persons where PersonID = 14;

insert into Persons values(2, "Kumar", "Nitesh", "Pune, Maharashtra", "Banglore");

