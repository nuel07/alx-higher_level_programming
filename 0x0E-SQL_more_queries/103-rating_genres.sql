--  lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT name, SUM(rate) AS rating
FROM tv_genres tg
INNER JOIN tv_show_genres sg
ON sg.genre_id = tg.id
INNER JOIN tv_show_ratings tr
ON tr.show_id = sg.show_id
GROUP BY name
ORDER BY rating DESC;
