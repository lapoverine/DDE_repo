import sqlite3
import pandas as pd
from sqlalchemy import create_engine

sqlite_conn = sqlite3.connect('creds.db')
cursor = sqlite_conn.cursor()
cursor.execute("SELECT * FROM access")

row = cursor.fetchone()
url, port, user, password = row
sqlite_conn.close()

connection_string = f"postgresql://{user}:{password}@{url}:{port}/homeworks"
engine = create_engine(connection_string)

df = pd.read_parquet('data/mental_health_data.parquet')
data = df.head(100)

table_name = "rafikov"

data.to_sql(
    name=table_name,
    con=engine,
    index=False,
    if_exists='replace'
)
