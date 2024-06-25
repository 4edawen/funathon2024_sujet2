import pandas as pd
from .clean_dataframe import clean_dataframe


def import_aiport_data(list_files):
    col_types = {
        "ANMOIS": "str",
        "APT": "str",   
        "APT_NOM": "str",
        "APT_ZON": "str",
        }
    list_df = [pd.read_csv(file, sep=";",dtype=col_types) for file in list_files]
    concat_df = pd.concat(list_df)
    cleaned_df = clean_dataframe(concat_df)
    return cleaned_df
