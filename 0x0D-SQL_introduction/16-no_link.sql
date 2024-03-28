-- List all records
SELECT `score`, `name`
FROM second_table
HAVING `name` is NOT NULL
ORDER BY `score` DESC;
