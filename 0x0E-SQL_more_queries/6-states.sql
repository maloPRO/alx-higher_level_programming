-- creates the database hbtn_0d_usa and the table states
DROP DATABASE IF EXISTS hbtn_0d_usa;
CREATE DATABASE hbtn_0d_usa;
DROP TABLE IF EXISTS states;
CREATE TABLE states(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
