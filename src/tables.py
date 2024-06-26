from great_tables import GT, md


def create_table_airports(dataframe):
    dataframe['name_clean'] = dataframe['apt_nom'].str.title() + " _(" + dataframe['apt'] + ")_"
    dataframe.columns = ['name_clean'] + [col for col in dataframe.columns if col != 'name_clean']
    return (
        GT(dataframe.head(15))
        .tab_header(title=md("**Title**"), subtitle=md("_Subtitle_"))
        .fmt_number(columns=["apt_pax_dep", "apt_pax_arr", "apt_pax_tr", "traffic"], compact=True)
        .fmt_markdown(columns=["name_clean"])
        .cols_hide(columns=["apt", "apt_nom"])
        .tab_source_note(source_note=md("_note de bas de page_"))
        .cols_label(
            name_clean="Aéroport",
            apt_pax_dep="Départ",
            apt_pax_arr="Arrivée",
            apt_pax_tr="Transit"
            )
        )
