SELECT COUNT(title)
FROM movies
WHERE movies.id = ratings.movie_id
AND rating = 10.0;
