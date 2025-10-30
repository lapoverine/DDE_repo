import pandas as pd


def transform_data(raw_data):

    transformed_data = raw_data.copy()

    transformed_data["id"] = transformed_data["id"].astype("int")
    transformed_data["Name"] = transformed_data["Name"].astype("str")
    transformed_data["Gender"] = transformed_data["Gender"].astype("str")
    transformed_data["Age"] = transformed_data["Age"].astype("int")
    transformed_data["City"] = transformed_data["City"].astype("str")
    transformed_data["Working Professional or Student"] = transformed_data[
        "Working Professional or Student"
    ].astype("str")
    transformed_data["Profession"] = transformed_data["Profession"].astype("str")
    transformed_data["Academic Pressure"] = transformed_data[
        "Academic Pressure"
    ].astype("Int16")
    transformed_data["Work Pressure"] = transformed_data["Work Pressure"].astype(
        "Int16"
    )
    transformed_data["CGPA"] = transformed_data["CGPA"].astype("float64")
    transformed_data["Study Satisfaction"] = transformed_data[
        "Study Satisfaction"
    ].astype("Int16")
    transformed_data["Job Satisfaction"] = transformed_data["Job Satisfaction"].astype(
        "Int16"
    )
    transformed_data["Sleep Duration"] = transformed_data["Sleep Duration"].astype(
        "str"
    )
    transformed_data["Dietary Habits"] = transformed_data["Dietary Habits"].astype(
        "str"
    )
    transformed_data["Degree"] = transformed_data["Degree"].astype("str")
    transformed_data["Have you ever had suicidal thoughts ?"] = transformed_data[
        "Have you ever had suicidal thoughts ?"
    ].astype("str")
    transformed_data["Work/Study Hours"] = transformed_data["Work/Study Hours"].astype(
        "int"
    )
    transformed_data["Financial Stress"] = transformed_data["Financial Stress"].astype(
        "int"
    )
    transformed_data["Family History of Mental Illness"] = transformed_data[
        "Family History of Mental Illness"
    ].astype("str")

    print("Типы данных преобразованы")
    return transformed_data
