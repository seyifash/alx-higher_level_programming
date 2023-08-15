-- A script that lists all the tables of a database
-- in your MySQL server.
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
	AND TABLE_SCHEMA = 'mysql';
