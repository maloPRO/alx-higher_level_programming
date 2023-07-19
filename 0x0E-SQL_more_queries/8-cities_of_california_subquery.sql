-- Lists cities
SELECT id, name
FROM cities
WHERE name = (
	SELECT name
	FROM state
	WHERE name = 'California');

	

