-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_show.name
FROM tv_genres
INNER JOIN show_genres 
ON show_genres.show.id = tv_show_id
INNER JOIN tv_genres 
ON tv_genres.id = show_genres.genre_id
WHERE tv.shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
