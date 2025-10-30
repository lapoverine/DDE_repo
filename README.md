# DDE_repo

## Dataset Description

[Exploring Mental Health Data](https://drive.google.com/file/d/1rxD968JtKcD3NM8bsSf8t5tJhNCDjR_O/view?usp=sharing)

This dataset presents a synthetic yet highly realistic representation of mental health survey responses, meticulously crafted using a deep learning generative model trained on the original Depression Survey/Dataset for Analysis.

Designed to simulate complex mental health assessment patterns while preserving participant anonymity, this dataset invites exploration into psychological data modeling, ethical AI applications, and modern classification techniques.

## Column Descriptions
Columns: 19

* id: Unique identifier for each participant record.
* Name: Placeholder for the participant's name (anonymized or synthetic).
* Gender: Reported gender of the participant (e.g., Male, Female, Other).
* Age: Age of the respondent, typically in years.
* City: City or region of residence, possibly synthetic.
* Working Professional or Student: Indicates whether the respondent is currently a student or a working professional.
* Profession: Declared field of profession or study (e.g., Engineering, Business).
* Academic Pressure: Self-reported academic stress level (e.g., High, Moderate, Low).
* Work Pressure: Self-reported job-related stress level (for working professionals).
* CGPA: Cumulative Grade Point Average—numerical academic performance indicator.
* Study Satisfaction: Subjective measure of satisfaction with current study routine.
* Job Satisfaction: Subjective measure of satisfaction with current job role (for professionals).
* Sleep Duration: Average hours of sleep per day.
* Dietary Habits: Reported diet quality or eating patterns (e.g., Balanced, Skipped meals).
* Degree: Academic degree currently pursued or achieved (e.g., Diploma, Bachelor’s, Master’s).
* Have you ever had suicidal thoughts ?: Binary or categorical response indicating prior mental health challenges.
* Work/Study Hours: Average number of hours spent working or studying per day.
* Financial Stress: Level of financial burden or concern (e.g., Severe, Mild, None).
* Family History of Mental Illness: Whether the respondent has a known family history of mental health issues.


## How to start code

1. **Activate conda environment**
   ```
   conda env create -f environment.yml
   ```
3. **Install poetry and the necessary libraries**
   ```python
   pip install poetry
   poetry add jupiterlab pandas matplotlib wget
   ```
5. **Run code**
   ```python
   python data_loader.py
   ```

## Project structure
```
DDE_REPO/
│
├── api_example/                     # Пример с API (chemical compounds and their properties)
│   ├── api_reader.py                # Скрипт для загрузки данных из API
│   └── README.md                    # Документация к API
|
├── etl/                             
|   ├── __init__
|   ├── extract.py                   # Загрузка сырых данных с GD, валидация и сохранение в .csv
|   ├── load.py                      # Сохранение обработанных данных в .parquet и загрузка до 100 строк в БД
|   ├── main.py                      # Объединение всех модулей. Требуется минимум один аргумент — file_url
|   ├── transform.py                 # Преобразование типов данных
|   └──  validate.py                 # Проверки валидации данных                 
|
├── notebooks/                       # Ноутбуки
|   └── EDA.ipynb                    # EDA с графиками
|   └── dtypes.ipynb                 # Приведение типов данных
|
├── pyproject.toml                   # Poetry: описание зависимостей проекта
├── poetry.lock                      # Зафиксированные версии библиотек
├── environment.yml                  # Конфигурация окружения 
└── README.md                        # Основная документация проекта
```

## Dataset Representation

Here are the first 10 lines of the dataset

![dde_data](https://github.com/user-attachments/assets/59c4b77e-7bf3-41f9-aedb-cebb6882333a)

## Dataset information after data type conversion

```python
RangeIndex: 93800 entries, 0 to 93799
Data columns (total 19 columns):
 #   Column                                 Non-Null Count  Dtype
---  ------                                 --------------  -----
 0   id                                     93800 non-null  int64
 1   Name                                   93800 non-null  object
 2   Gender                                 93800 non-null  object
 3   Age                                    93800 non-null  int64
 4   City                                   93800 non-null  object
 5   Working Professional or Student        93800 non-null  object
 6   Profession                             93800 non-null  object
 7   Academic Pressure                      18767 non-null  Int16
 8   Work Pressure                          75022 non-null  Int16
 9   CGPA                                   18766 non-null  float64
 10  Study Satisfaction                     18767 non-null  Int16
 11  Job Satisfaction                       75026 non-null  Int16
 12  Sleep Duration                         93800 non-null  object
 13  Dietary Habits                         93800 non-null  object
 14  Degree                                 93800 non-null  object
 15  Have you ever had suicidal thoughts ?  93800 non-null  object
 16  Work/Study Hours                       93800 non-null  int64
 17  Financial Stress                       93800 non-null  int64
 18  Family History of Mental Illness       93800 non-null  object
```

## EDA with data visualization

[You can find it here!](https://nbviewer.org/github/lapoverine/DDE_repo/blob/main/notebooks/EDA.ipynb)

## Запуск ETL 
ETL-скрипт делает загрузку датасета, валидацию и преобразование сырых данных, сохранение сырого и преобразованного датасета в форматах .csv и .parquet соответственно и запись до 100 строк данных в БД.

1. **Настроить окружение**
   ```
   conda env create -f environment.yml
   ```
2. **Запуск ETL-процесса**
   ```
   python etl/main.py --input https://drive.google.com/uc?id=1rxD968JtKcD3NM8bsSf8t5tJhNCDjR_O --table mental_health_table
   ```
Пример вывода ETL:

<img width="503" height="108" alt="image" src="https://github.com/user-attachments/assets/72dfddf4-5153-4e0b-ab03-78fa82fb7cca" />
