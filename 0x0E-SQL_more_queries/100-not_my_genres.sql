-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT name
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS sg
ON tg.id = sg.genre_id
INNER JOIN tv_shows AS ts
ON sg.show_id = ts.id
       WHERE tg.name NOT IN
             (SELECT name
                FROM tv_genres tg INNER JOIN tv_show_genres AS sg
ON tg.id = sg.genre_id JOIN tv_shows AS ts
ON sg.show_id = ts.id
WHERE ts.title = "Dexter")
ORDER BY tg.name;
