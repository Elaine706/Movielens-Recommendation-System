import mariadb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
mydb = mariadb.connect(
    host="localhost",
    user="root",
    password="elaine10",
    database="movie"
)
mycursor = mydb.cursor()
query = """
SELECT
    m.title,
    ROUND(AVG(r.rating),2) AS avg_rating,
    COUNT(*) AS rating_count
FROM ratings r
JOIN movies m
ON r.movieId = m.movieId
GROUP BY m.movieId, m.title
"""

mycursor.execute(query)

rows = mycursor.fetchall()

df = pd.DataFrame(
    rows,
    columns=["title", "avg_rating", "rating_count"]
)

print(df.head())
df_filtered = df[df["rating_count"]<=100]
plt.figure(figsize=(10,6))

plt.scatter(
    df_filtered["rating_count"],
    df_filtered["avg_rating"],
    alpha=0.4
)

plt.xlabel("Rating Count")
plt.ylabel("Average Rating")
plt.title("Rating Count vs Average Rating")

plt.show()