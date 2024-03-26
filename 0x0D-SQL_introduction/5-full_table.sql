-- Description of table
USE "$1";
-- Description
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT
FROM information_schema.columns
WHERE table_name = 'first_table'
ORDER BY ORDINAL_POSITION;
