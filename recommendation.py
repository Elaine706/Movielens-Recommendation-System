import mariadb
import streamlit as st
st.title("🎬 movie recommendation")

mydb = mariadb.connect(
    host="localhost",
    user="root",
    password="elaine10",
    database="movie"
)
mycursor = mydb.cursor()
genres = [
    "Action",
    "Adventure",
    "Animation",
    "Children",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Fantasy",
    "Film-Noir",
    "Horror",
    "IMAX",
    "Musical",
    "Mystery",
    "Romance",
    "Sci-Fi",
    "Thriller",
    "War",
    "Western"]

selected_genre = st.selectbox("Select a genre:", genres)

if st.button("Recommend Movies🔍"):
    with st.spinner("Searching..."):
        query = """
        select
        m.title,
        ROUND(AVG(r.rating),2) AS avg_rating,
        COUNT(*) AS rating_count
        from movies m
        join ratings r
        on m.movieid = r.movieid
        join movie_genres mg
        on m.movieid = mg.movieid
        where mg.genre = ?
        group by m.movieid, m.title
        having COUNT(*) >= 50
        order by avg_rating DESC
        limit 10
        """
        mycursor.execute(query,(selected_genre,))
        results = mycursor.fetchall()

        if results:
            st.subheader(f"🏆 Top {selected_genre} Movies")
            for i, row in enumerate(results, start=1):
                title = row[0]
                rating = row[1]
                count = row[2]
                with st.container():
                    st.markdown(f"{i}.{title}")
                    st.markdown(f"Average Rating: **{rating}** (from {count} ratings)")
                    st.divider()
        else: st.warning(f"No movies found for genre: {selected_genre}")




