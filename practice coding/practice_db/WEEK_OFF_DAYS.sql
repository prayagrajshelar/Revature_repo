SELECT * 
FROM your_table
WHERE DAYOFWEEK(date_column) IN (1, 7);  -- Sunday or Saturday
