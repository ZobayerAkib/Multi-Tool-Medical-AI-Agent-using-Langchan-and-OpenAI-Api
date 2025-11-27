import pandas as pd
import sqlite3

def csv_to_sqlite(csv_file, db_file, table_name):
    df = pd.read_csv(csv_file)
    conn = sqlite3.connect(db_file)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"Created {db_file} ({table_name})")

csv_to_sqlite("heart.csv", "heart_disease.db", "heart")
csv_to_sqlite("cancer.csv", "cancer.db", "cancer")
csv_to_sqlite("diabetes.csv", "diabetes.db", "diabetes")
