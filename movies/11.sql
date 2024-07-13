SELECT title FROM movies
WHERE movies.id IN
(
    SELECT(movies.id) FROM movies
    JOIN stars ON movies.id = stars.movie_id
    JOIN ratings ON stars.movie_id = ratings.movie_id
    WHERE stars.person_id = "Chadwick Boseman"
    ORDER BY ratings.rating
)
LIMIT 5;
