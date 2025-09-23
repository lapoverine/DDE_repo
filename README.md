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
   ```python
   conda env create -f environment.yml
   ```
3. **Install poetry and the necessary libraries**
   ```python
   pip install poetry
   poetry add jupiterlab pandas matplotlib wget
   ```
5. **Run code**
   ```python
   cd dde_project
   python data_loader.py
   ```

## Dataset Visualization

Here are the first 10 lines of the dataset
![dde_data](https://github.com/user-attachments/assets/59c4b77e-7bf3-41f9-aedb-cebb6882333a)