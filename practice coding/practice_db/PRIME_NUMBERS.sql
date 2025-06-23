use practice_db;

with recursive 
numbers as (
select 2 as num
union all
select num + 1 from numbers where num + 1 <= 20
),
primes AS (
    SELECT n.num
    FROM numbers n
    WHERE NOT EXISTS (
        SELECT 1
        FROM numbers d
        WHERE d.num < n.num AND d.num > 1 AND n.num % d.num = 0
    )
)
SELECT GROUP_CONCAT(num SEPARATOR '&') AS prime_list
FROM primes;

