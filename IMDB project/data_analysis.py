import pandas as pd
import numpy as np
from db_utils import connect_database, get_movie_by_title

def top_rated_movies():
    conn = connect_database()
    df = pd.read_sql("""SELECT * FROM MOVIES
                     ORDER BY RATING DESC
                     LIMIT 10
                     """, conn)
    print("\n TOP 10 MOVIES by RATING: ")
    print(df[["title", "rating"]])
    conn.close()

def average_statistics():
    conn = connect_database()
    df = pd.read_sql("SELECT * FROM MOVIES", conn)
    print("/n Average Statistics: ")
    print("Average Rating: ", np.round(df["rating"].mean(), 2))
    print("Average Runtime:", np.round(df['runtime'].mean(), 2))
    print("Average Revenue (in millions):", np.round(df['revenue'].mean(), 2))
    conn.close()

def search_movie():
    title = input("Enter the movie title to search: ")
    movie = get_movie_by_title(title)
    if movie:
        print("\nMovie Details\n")
        print(f"Title: {movie['title']}")
        print(f"Genre: {movie['genre']}")
        print(f"Direcotr: {movie['director']}")
        print(f"Year: {movie['year']}")
        print(f"Runtime: {movie['runtime']} minutes")
        print(f"Rating: {movie['rating']}/10 ⭐")
        print(f"Votes: {movie['votes']}")
        print(f"Revenue: ${movie['revenue']} million")
    else:
        print("❌ Movie not found in database.")