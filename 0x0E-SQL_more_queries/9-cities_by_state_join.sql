-- Lists all cities
SELECT *
FROM cities
	NATURAL JOIN states
ORDER BY id;
