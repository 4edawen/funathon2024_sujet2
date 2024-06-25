import pandas as pd
from .clean_dataframe import clean_dataframe


def import_data(list_files, schema):
    list_df = [pd.read_csv(file, sep=";", dtype=schema) for file in list_files]
    concat_df = pd.concat(list_df)
    cleaned_df = clean_dataframe(concat_df)
    return cleaned_df


def import_aiport_data(list_files):
    col_types = {
        "ANMOIS": "str",
        "APT": "str",
        "APT_NOM": "str",
        "APT_ZON": "str",
        }
    return import_data(list_files, col_types)


def import_compagnies_data(list_files):
    col_types = {
        "ANMOIS": "str",
        "CIE": "str",
        "CIE_NOM": "str",
        "CIE_NAT": "str",
        "CIE_PAYS": "str"
        }
    return import_data(list_files, col_types)


def import_liaisons_data(list_files):
    col_types = {
        "ANMOIS": "str",
        "LSN": "str",
        "LSN_DEP_NOM": "str",
        "LSN_ARR_NOM": "str",
        "LSN_SCT": "str",
        "LSN_FSC": "str"
        }
    return import_data(list_files, col_types)
