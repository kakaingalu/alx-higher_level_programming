-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
mysql -u root -p hbtn_0d_tvshows -e "title, genre_id FROM tv_shows INNER JOIN tv_show_genres ON id = tv_show_id ORDER BY title ASC, genre_id ASC;"

