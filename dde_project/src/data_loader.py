import pandas as pd

FILE_ID = '1rxD968JtKcD3NM8bsSf8t5tJhNCDjR_O'
file_url = f"https://drive.google.com/uc?id={FILE_ID}"
file_url = "https://drive.google.com/uc?id=1rxD968JtKcD3NM8bsSf8t5tJhNCDjR_O"

raw_data = pd.read_csv(file_url)

print(raw_data.head(10))

