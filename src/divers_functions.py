

def summary_stat_airport(dataframe):
    return dataframe.groupby("apt").agg(
        {"apt_nom": "first",
            "apt_pax_dep": "sum",
            "apt_pax_arr": "sum",
            "apt_pax_tr": "sum",
            "traffic": "sum"}
        ).sort_values("traffic", ascending=False).reset_index()


def create_data_from_input(dataframe, year, month):
    return dataframe[(dataframe["an"] == year) & (dataframe["mois"] == month)]
