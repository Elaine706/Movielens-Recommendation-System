# Movielens-Recommendation-System
a genre-based movie recommendation system built with Python, Mariadb, SQL, and Streamlit using the MovieLens dataset
# Background
As a movie enthusiast, I often struggle with "what to watch." This project solves that problem: based on the user's selected genre, recommend the highest-rated movies with a reliable number of ratings.
# Data source
This project uses the Movielens dataset available on Kaggle, uploaded by Sherin Claudia. Due to license restrictions, the dataset is not included in this repository.
The dataset is used under the GroupLens Research usage agreement:
- For research and educational purposes only
- Redistribution of the dataset is not allowed
- No commercial use permitted
# Features
-Genre-based movie recommendation
-Movie rating analysis
-Data visualization
# Analysis
1. Split genres into separate table
2. Analyzed rating distribution → choose **50** as minimum rating count
3. Recommendation: filter by genre → keep movies with ≥50 ratings → sort by average rating
# Structure
## analysis/
- SQL analysis queries
- Rating distribution visualization
## data_processing/
- Genre preprocessing
## images/
- Visualization results
## recommendation.py
- Genre-based recommendation system
