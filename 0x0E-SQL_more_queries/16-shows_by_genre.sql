-- lists all shows, and all genres linked to that show
SELECT tv_shows.title AS title, IFNULL(tv_genres.name, NULL) AS name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, name;
