-- Create table name
if [ -z "$1" ]; then
    exit 1
fi
-- Open database
USE "$1";
-- Create a table
CREATE TABLE IF NOT EXISTS first_table (
    id int,
    name VARCHAR(256)
);
