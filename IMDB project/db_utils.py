import mysql.connector
import pandas as pd

def connect_database():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "imdb"
    )
# print("Connection istablishsed")

def init_db():
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            genre VARCHAR(100),
            director VARCHAR(100),
            year INT,
            runtime INT,
            rating FLOAT,
            votes INT,
            revenue FLOAT
        )
    """)
    conn.commit()
    conn.close()
# init_db()
# print("Connection closed")

def fetch_all_movies():
    conn = connect_database()
    df = pd.read_sql("SELECT * FROM MOVIES", conn)
    print(df)
    conn.close()


def insert_movies():
    conn = connect_database()
    cursor = conn.cursor()
    print("Enter Movie Details:")
    title = input("Title: ")
    genre = input("Genre: ")
    director = input("Director: ")
    year = input("Year: ")
    runtime = input("Runtime: ")
    rating = input("Rating: ")
    votes = int(input("Votes: "))
    revenue = float(input("Revenue (millions): "))
    cursor.execute("""
        INSERT INTO movies (title, genre, director, year, runtime, rating, votes, revenue)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (title, genre, director, year, runtime, rating, votes, revenue))
    conn.commit()
    conn.close()
    print("Movie added successfully!")


def delete_movie():
    conn = connect_database()
    cursor = conn.cursor()
    title = input("Enter the title of the movie to delete: ").strip()

    cursor.execute("DELETE FROM movies WHERE LOWER(title) = LOWER(%s)", (title,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"'{title}' has been deleted from the database.")
    else:
        print(f"⚠️  Movie titled '{title}' not found.")

    conn.close()
    

def get_movie_by_title(title):
    conn = connect_database()
    cursor = conn.cursor(dictionary = True)
    query = "SELECT * FROM movies WHERE LOWER(title) = LOWER(%s)"
    cursor.execute(query, (title,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_movies_by_year(year):
    conn = connect_database()
    try:
        query = "SELECT * FROM movies WHERE year = %s"
        df = pd.read_sql(query, conn, params=(year,))
        return df
    except Exception as e:
        print("Error:", e)
        return pd.DataFrame()
    finally:
        conn.close()
