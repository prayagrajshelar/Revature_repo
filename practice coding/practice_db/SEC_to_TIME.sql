use practice_db;

create table events(
id int,
event_name varchar(100),
duration_sec int
);

insert into events (id, event_name, duration_sec) values
(1, 'Login Session', 3661),
(2, 'Video Play', 542),
(3, 'File Download', 128),
(4, 'Page View', 59),
(5, 'Session Timeout', 86399);


SELECT 
    id,
    event_name,
    duration_sec,
    SEC_TO_TIME(duration_sec) AS duration_time
FROM 
    events;
