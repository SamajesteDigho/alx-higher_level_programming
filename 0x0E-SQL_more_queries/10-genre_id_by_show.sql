-- select by count
SELECT tvs.title, COUNT(tvsg.genre_id) AS genre_id, tvsg.show_id
FROM tv_shows tvs, tv_show_genres tvsg
GROUP BY tvsg.genre_id
WHERE COUNT(tvsg.genre_id) > 0
ORDER BY tvs.title, tvsg.genre_id ASC;
