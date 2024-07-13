SELECT name FROM people
WHERE people.id IN
(
    JOIN directors ON people.id = directors.person_id
    JOIN movies ON directors.movie_id = movies.id
    JOIN ratings ON movies.id = ratings.movie_id
    WHERE ratings.rating >= 9.0
);
