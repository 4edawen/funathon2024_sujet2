import geopandas as gpd
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from streamlit_folium import st_folium

import src.import_data as sid
from src.create_data_list import create_data_list
from src.figures import plot_airport_line, map_leaflet_airport
from src.divers_functions import summary_stat_airport, create_data_from_input
from src.tables import create_table_airports

YEARS_LIST = [str(year) for year in range(2018, 2023)]
MONTHS_LIST = [str(month) for month in range(1, 13)]
year = YEARS_LIST[0]
month = MONTHS_LIST[0]
# Load data ----------------------------------
urls = create_data_list("./sources.yml")


pax_apt_all = sid.import_airport_data(urls['airports'].values())
pax_cie_all = sid.import_airport_data(urls['compagnies'].values())
pax_lsn_all = sid.import_airport_data(urls['liaisons'].values())


airports_location = gpd.read_file(urls['geojson']['airport'])


liste_aeroports = pax_apt_all['apt'].unique()
default_airport = liste_aeroports[0]

pax_apt_all["traffic"] = pax_apt_all["apt_pax_dep"] + \
    pax_apt_all["apt_pax_tr"] + \
    pax_apt_all["apt_pax_arr"]


# Streamlit Layout --

st.set_page_config(
  page_title="Tableau de bord des aéroports français", layout="wide",
  page_icon="✈️"
  )
col1, col2 = st.columns(2)

selected_date = col1.date_input(
    "Mois choisi",
    pd.to_datetime("2019-01-01"),
    min_value=pd.to_datetime("2018-01-01"),
    max_value=pd.to_datetime("2022-12-01")
  )
year = selected_date.year
month = selected_date.month

stats_aeroports = summary_stat_airport(create_data_from_input(pax_apt_all, year, month))

table_airports = (
  create_table_airports(stats_aeroports)
  .as_raw_html()
)

with col1:
    components.html(table_airports, height=600)

