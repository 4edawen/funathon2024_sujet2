import pandas as pd


def extract_month_year(row):
    row['an'] = row['ANMOIS'][:4]
    row['mois'] = str(int(row['ANMOIS'][4:]))
    return row['an'], row['mois']


def clean_dataframe(df):
    df['an'], df['mois'] = df.apply(extract_month_year, axis=1, result_type='expand')[0],
    df.apply(extract_month_year, axis=1, result_type='expand')[1]
    df.columns = map(str.lower, df.columns)
    return df