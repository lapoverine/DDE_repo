import pandas as pd
import os
from validate import validate_raw_data


def extract_data(file_url):
    raw_data = pd.read_csv(file_url)

    if validate_raw_data(raw_data):
        os.makedirs("data/raw", exist_ok=True)
        raw_data.to_csv("data/raw/mental_health_data_raw.csv", index=False)

        print("Сырые данные сохранены в data/raw/mental_health_data_raw.csv")
        return raw_data
