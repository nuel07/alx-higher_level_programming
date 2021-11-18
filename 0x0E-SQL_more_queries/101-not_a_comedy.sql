-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT title
FROM tv_shows ts
LEFT JOIN tv_show_genres sg
ON sg.show_id = ts.id
LEFT JOIN tv_genres tg
ON tg.id = sg.genre_id
WHERE ts.title NOT IN
  (SELECT title
FROM tv_shows ts
INNER JOIN tv_show_genres AS sg
ON sg.show_id = ts.id
JOIN tv_genres tg
ON tg.id = sg.genre_id
WHERE tg.name = "Comedy")
ORDER BY title;
