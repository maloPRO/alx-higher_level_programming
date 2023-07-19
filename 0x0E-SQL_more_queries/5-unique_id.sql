-- creates table with unique id
DROP TABLE IF EXISTS unique_id;
CREATE TABLE unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
