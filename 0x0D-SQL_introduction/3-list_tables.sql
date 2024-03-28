-- Display all tables of a given database
SELECT *
FROM information_schema.tables
WHERE table_schema = "mysql";
