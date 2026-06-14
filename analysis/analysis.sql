--Statistics of the number of various types of films
select 
genre,
COUNT(*) AS movie_count
from movie_genres
group by genre
order by movie_count

--Statistics of average scores for all types
select
mg.genre,
ROUND(AVG(r.rating),2) AS avg_rating,
COUNT(r.rating) AS total_ratings
from movie_genres mg
join ratings r
on mg.movieid = r.movieid
group by mg.genre
order by avg_rating DESC;

-- Determine the recommendation threshold (Why 50? )
-- Count the number of movies with a rating score of 20 or higher
select 
COUNT(*)
from(
    select movieid 
    from ratings
    group by movieid
    having COUNT(*) >= 20
)t;

-- Count the number of movies with a rating score of 50 or higher
select 
COUNT(*)
from(
    select movieid 
    from ratings
    group by movieid
    having COUNT(*) >= 50
)t;

-- Count the number of movies with a rating score of 100 or higher
select 
COUNT(*)
from(
    select movieid 
    from ratings
    group by movieid
    having COUNT(*) >= 100
)t;

-- Conclusion: Set the recommendation threshold at 50
-- Statistical results:
--   Threshold 20 → 1,303 films 
--   Threshold 50 → 453 films 
--   Threshold 100 → 151 films 
-- Therefore, 50 was chosen as the threshold for the minimum number of votes.
-- This ensures both the reliability of the statistics and the retention of sufficient recommendation results.