--  a script that lists all the cities of California that can be found in the database hbtn_0d_uu
SELECT cities.id, cities.name
FROM hbtn_0d_usa.cities cities, hbtn_0d_usa.states states
WHERE cities.state_id = states.id AND states.name = 'California'
ORDER BY cities.id ASC;
