import pandas as pd 
from db_utils import connect_database

def clean_and_update_mysql():

    conn = connect_database()
    df = pd.read_sql("SELECT * FROM movies", conn)

    df.dropna(subset = ["rating", "revenue", "title", "genre"], inplace=True)

    df = df[ df["rating"] > 0 ]
    df["title"] = df["title"].str.strip()
    df["genre"] = df["genre"].str.strip().str.lower()
    df["direcotr"] = df["director"].fillna("unknown").str.strip()

    # coverting to appropriste types
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
    df["votes"] = pd.to_numeric(df["votes"], errors="coerce", downcast="integer")
    df["runtime"] = pd.to_numeric(df["runtime"], errors="coerce", downcast="integer")
    df["year"] = pd.to_numeric(df["year"], errors="coerce", downcast="integer")

    df.dropna(subset=["revenue", "votes", "runtime", "year"], inplace=True)

    df.drop_duplicates(subset=["title", "year"], inplace=True)

    cursor = conn.cursor()

    cursor.execute("DELETE FROM movies")

    conn.commit()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO movies (title, genre, director, year, runtime, rating, votes, revenue)
                values (%s, %s, %s, %s, %s, %s, %s, %s)
        """,(
            row["title"],
            row["genre"],
            row["direcotr"],
            int(row["year"]),
            int(row["runtime"]),
            float(row["rating"]),
            int(row["votes"]),
            float(row["revenue"])
        ))
    conn.commit()
    conn.close()

    print("Cleaned data has been updated in the MYSQL database")

if __name__ == "__main__":
    clean_and_update_mysql()
