import pandas as pd
from db_utils import connect_database

def export_to_csv():
    conn = connect_database()
    df = pd.read_sql("SELECT * FROM MOVIES", conn)
    df.to_csv("output/exported_movies.csv", index=False)
    print("Expoerted to output/exported_movies.csv")
    conn.close()
    