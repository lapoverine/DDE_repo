import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('DB_URL')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')


connection_string = f"postgresql://{user}:{password}@{url}:{port}/{db_name}"
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
