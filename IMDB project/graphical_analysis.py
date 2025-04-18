import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
from db_utils import connect_database

def plot_top_rated_movies():
    conn = connect_database()
    df = pd.read_sql("SELECT title, rating FROM movies ORDER BY rating DESC LIMIT 10", conn)
    conn.close()
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x = "rating",
        y = "title",
        data = df,
        palette = "coolwarm"
    )
    plt.title("Top 10 Movies by IMDb Rating")
    plt.xlabel("Rating")
    plt.ylabel("Movie Title")
    plt.tight_layout()
    plt.show()


def plot_avg_rating_yearwise():
    conn = connect_database()
    df = pd.read_sql("SELECT year, AVG(rating) AS avg_rating FROM movies GROUP BY year ORDER BY year", conn)
    conn.close()
    plt.figure(figsize=(12, 6))
    sns.lineplot(
        x = "year",
        y = "avg_rating",
        data = df,
        marker = 'o'
    )
    plt.title("Average IMDb Rating By Year")
    plt.xlabel("Year")
    plt.ylabel("Average Rating")
    plt.grid(True)
    plt.tight_layout()
    plt.show()



def plot_movies_by_genre():
    conn = connect_database()
    df = pd.read_sql("SELECT genre FROM movies", conn)
    conn.close()

    df = df["genre"].str.split(',').explode().str.strip()
    genre_counts = df.value_counts().reset_index()
    genre_counts.columns = ['genre', 'count']

    plt.figure(figsize=(12, 6))
    sns.barplot(
        x = 'count',
        y = 'genre',
        data = genre_counts.head(10),
        palette = 'viridis'
    )
    plt.title("Top 10 Most Common Genres")
    plt.xlabel("Number of Movies")
    plt.ylabel("Genre")
    plt.tight_layout()
    plt.show()

