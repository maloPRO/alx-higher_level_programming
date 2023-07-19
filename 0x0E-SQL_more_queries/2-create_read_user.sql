-- Creates database hbtn_0d_2 and user user_0d_2
DROP DATABASE IF EXISTS hbtn_0d_2;
CREATE DATABASE hbtn_0d_2;
DROP USER IF EXISTS user_0d_2;
CREATE USER 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
