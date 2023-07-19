-- Lists all cities
SELECT id, name, name
FROM cities
	NATURAL JOIN states
ORDER BY id;
