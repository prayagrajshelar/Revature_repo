import pandas as pd
from db_utils import connect_database

df = pd.read_csv("data/movies.csv")
df.dropna(
    subset=["Title", "Genre", "Director", "Year", "Runtime (Minutes)", "Rating", "Votes", "Revenue (Millions)"], inplace=True)
df = df.rename(columns={
    "Title":"title",
    "Genre":"genre",
    "Director":"director",
    "Year":"year",
    "Runtime (Minutes)":"runtime",
    "Rating":"rating",
    "Votes":"votes",
    "Revenue (Millions)":"revenue"
})

conn = connect_database()
cursor = conn.cursor()
cursor.execute("DELETE FROM movies")
for _, row in df.iterrows():
    cursor.execute("INSERT INTO movies (title, genre, director, year, runtime, rating, votes, revenue) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    (row['title'], 
     row['genre'], 
     row['director'], 
     int(row['year']),
     int(row['runtime']),
     float(row['rating']),
     int(row['votes']),
     float(row['revenue'])
     )
    )
conn.commit()
cursor.close()
conn.close()

print("Movies data restored successfully.")
