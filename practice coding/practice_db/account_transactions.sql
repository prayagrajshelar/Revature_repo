use practice_db;
drop table account;

CREATE TABLE account (
    ano INT PRIMARY KEY,
    aname VARCHAR(20),
    address VARCHAR(50)
);
INSERT INTO account (ano, aname, address) VALUES
(101, 'nirja singh', 'bangalore'),
(102, 'rohan gupta', 'chennai'),
(103, 'ali reza', 'hydrabad'),
(104, 'rishabh jain', 'chennai'),
(105, 'simran kaur', 'chandigarh');


CREATE TABLE TRANSACT (
    TRNO VARCHAR(10) PRIMARY KEY,
    ANO INT,
    AMOUNT INT,
    TYPE VARCHAR(20),
    DOT DATE,
    FOREIGN KEY (ANO) REFERENCES account(ano)
);
ALTER TABLE account ADD CONSTRAINT unique_ano UNIQUE (ano);

INSERT INTO TRANSACT VALUES ('T001', 101, 2500, 'Withdraw', '2017-12-21');
INSERT INTO TRANSACT VALUES ('T002', 103, 3000, 'Deposit', '2017-06-01');
INSERT INTO TRANSACT VALUES ('T003', 102, 2000, 'Withdraw', '2017-05-12');
INSERT INTO TRANSACT VALUES ('T004', 103, 1000, 'Deposit', '2017-10-22');
INSERT INTO TRANSACT VALUES ('T005', 102, 12000, 'Deposit', '2017-11-06');


SELECT * FROM TRANSACT
WHERE TYPE = 'Withdraw';


-- To display ANO and AMOUNT of all Deposit and Withdrawals 
-- done in month of ‘May’ 2017 from table TRANSACT
SELECT ANO, AMOUNT FROM TRANSACT
WHERE MONTH(DOT) = 5 AND YEAR(DOT) = 2017;


-- To display first date of transaction (DOT) from table TRANSACT for Account having ANO as 102
SELECT MIN(DOT) FROM TRANSACT
WHERE ANO = 102;

 -- To display ANO, ANAME, AMOUNT and DOT of those persons from ACCOUNT and TRANSACT 
-- table who have done transaction less than or equal to 3000
SELECT A.ANO, A.ANAME, T.AMOUNT, T.DOT
FROM ACCOUNT A
JOIN TRANSACT T ON A.ANO = T.ANO
WHERE T.AMOUNT <= 3000;

