import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv


def load_data(transformed_data, table_name="rafikov", max_rows=100):

    data_to_load = transformed_data.head(max_rows)

    os.makedirs("data/processed", exist_ok=True)
    data_to_load.to_parquet(
        "data/processed/mental_health_data_processed.parquet", index=False
    )
    print("Данные сохранены в data/processed/mental_health_data_processed.parquet")

    load_dotenv()

    url = os.getenv("DB_URL")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    db_name = os.getenv("DB_NAME")

    connection_string = f"postgresql://{user}:{password}@{url}:{port}/{db_name}"
    engine = create_engine(connection_string)

    data_to_load.to_sql(name=table_name, con=engine, index=False, if_exists="replace")

    print(f"Данные успешно загружены в таблицу {table_name}")
