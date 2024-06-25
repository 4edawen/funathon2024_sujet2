import pandas as pd


def summary_stat_airport(dataframe):
    cols = ["apt", "traffic", "apt_pax_dep", "apt_pax_arr", "apt_pax_tr"]
    return dataframe[cols].groupby("apt").sum().sort_values("traffic", ascending=False).reset_index()


def create_data_from_input(dataframe, year, month):
    return dataframe[(dataframe["an"] == year) & (dataframe["mois"] == month)]
