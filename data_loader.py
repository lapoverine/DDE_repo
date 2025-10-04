import pandas as pd

data_path = 'data/mental_health_data.csv'

raw_data = pd.read_csv(data_path)

print(raw_data.head(10))

raw_data['id'] = raw_data['id'].astype('int')
raw_data['Name'] = raw_data['Name'].astype('str')
raw_data['Gender'] = raw_data['Gender'].astype('str')
raw_data['Age'] = raw_data['Age'].astype('int')
raw_data['City'] = raw_data['City'].astype('str')
raw_data['Working Professional or Student'] = raw_data['Working Professional or Student'].astype('str')
raw_data['Profession'] = raw_data['Profession'].astype('str')
raw_data['Academic Pressure'] = raw_data['Academic Pressure'].astype('Int16')
raw_data['Work Pressure'] = raw_data['Work Pressure'].astype('Int16')
raw_data['CGPA'] = raw_data['CGPA'].astype('float64')
raw_data['Study Satisfaction'] = raw_data['Study Satisfaction'].astype('Int16')
raw_data['Job Satisfaction'] = raw_data['Job Satisfaction'].astype('Int16')
raw_data['Sleep Duration'] = raw_data['Sleep Duration'].astype('str')
raw_data['Dietary Habits'] = raw_data['Dietary Habits'].astype('str')
raw_data['Degree'] = raw_data['Degree'].astype('str')
raw_data['Have you ever had suicidal thoughts ?'] = raw_data['Have you ever had suicidal thoughts ?'].astype('str')
raw_data['Work/Study Hours'] = raw_data['Work/Study Hours'].astype('int')
raw_data['Financial Stress'] = raw_data['Financial Stress'].astype('int')
raw_data['Family History of Mental Illness'] = raw_data['Family History of Mental Illness'].astype('str')

print(raw_data.info())

raw_data.to_parquet('data/mental_health_data.parquet', index=False)

