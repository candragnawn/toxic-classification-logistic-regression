import pandas as pd

def exploratory_data_analysis(data):
    print("Data Shape:", data.shape)
    print("\nData Types:\n", data.dtypes)
    print("\nMissing Values:\n", data.isnull().sum())
    print("\nStatistical Summary:\n", data.describe())
    print("\nClass Distribution:\n", data['label'].value_counts())
    return data