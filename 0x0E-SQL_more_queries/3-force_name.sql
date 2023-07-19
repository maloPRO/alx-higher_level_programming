-- Creates a table
-- name cant be NULL
DROP TABLE IF EXISTS force_name;
CREATE TABLE force_name(
	id INT,
	name VARCHAR(256) NOT NULL
);
