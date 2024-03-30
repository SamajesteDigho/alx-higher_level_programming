-- All cities
SELECT DISTINCT c.id, c.name, s.name
FROM cities c, states s
ORDER BY c.id ASC;
