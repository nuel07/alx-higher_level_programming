--  lists all cities contained in the database hbtn_0d_usa
SELECT *
FROM cities INNER JOIN states
ON cities.state_id = states.id
ORDER BY  cities.id;
