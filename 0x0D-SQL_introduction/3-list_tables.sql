-- Display all tables of a given database
if [ -z "$1" ]; then
    exit 1
fi
SELECT *
FROM information_schema.tables
WHERE table_schema = "$1";
