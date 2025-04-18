import pandas as pd
import mysql.connector

# Step 1: Load and clean the CSV
df = pd.read_csv('data/movies.csv')

# Step 2: Select and rename columns to match your database schema
df = df[['Title', 'Genre', 'Director', 'Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)']]
df.columns = ['title', 'genre', 'director', 'year', 'runtime', 'rating', 'votes', 'revenue']

# Step 3: Fill any missing revenue values with 0
df['revenue'] = df['revenue'].fillna(0)

# Step 4: Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',  
    database='imdb'
)
cursor = conn.cursor()

# Step 5: Insert rows into the `movies` table
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO movies (title, genre, director, year, runtime, rating, votes, revenue)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
conn.close()
print("IMDb data inserted into MySQL successfully!")
