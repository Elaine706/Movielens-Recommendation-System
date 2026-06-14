#Divide the movie genres
#In the original data, the "genres" field of the "movies" table is in the format of "Action|Adventure|Animation"
#It needs to be split into the "movie_genres" table, with one row for each genre.

import mariadb
import matplotlib.pyplot as plt
import numpy as np
mydb = mariadb.connect(
    host="localhost",
    user="root",
    password="elaine10",
    database="movie"
)
mycursor = mydb.cursor()
mycursor.execute("""Select movieid, genres from movies""")
rows = mycursor.fetchall()
genre_set = set()
for movieid, genres in rows:
    if genres:
        genre_list = genres.split("|")
        for genre in genre_list:
            genre = genre.strip()
            mycursor.execute("""Insert into movie_genres(movieid,genre) VALUES(?,?)""", (movieid,genre))
mydb.commit()
