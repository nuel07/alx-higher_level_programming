-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT title, SUM(rate) AS rating
FROM tv_shows ts JOIN tv_show_ratings tr
ON ts.id = tr.show_id
GROUP BY title
ORDER BY rating DESC;
