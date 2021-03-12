import pandas as pd
import matplotlib.pyplot as plt

def process():

    df = pd.read_excel('Haircut.xlsx', skiprows=2)
    df = df.drop(["Unnamed: 6", "Unnamed: 7"], axis=1)
    df = df.drop(df.index[[114,115]])

    cultureDF = df[["Unnamed: 9", "Culture Codes"]]
    cultureDF = cultureDF.dropna()
    cultureDF.columns = ['culture_name', 'code']
    df = df.drop(["Unnamed: 9", "Culture Codes"], axis=1)

    distinct_age = df["Age"].value_counts()
    df = pd.merge(df, cultureDF, left_on='Culture', right_on='code', how='left').drop('code', axis=1)

if __name__ == '__main__':
    process()