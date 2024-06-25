import pandas as pd
import geopandas as gpd
import plotly.express as px
from plotnine import ggplot, geom_line, aes

import src.import_data as sid
from src.create_data_list import create_data_list
from src.figures import plot_airport_line
from src.divers_functions import summary_stat_airport, create_data_from_input

# Load data ----------------------------------
urls = create_data_list("./sources.yml")


pax_apt_all = sid.import_airport_data(urls['airports'].values())
pax_cie_all = sid.import_airport_data(urls['compagnies'].values())
pax_lsn_all = sid.import_airport_data(urls['liaisons'].values())


airports_location = gpd.read_file(
    urls['geojson']['airport']
)


liste_aeroports = pax_apt_all['apt'].unique()
default_airport = liste_aeroports[0]

plot_airport_line(pax_apt_all, "FMEE")

YEARS_LIST = [str(year) for year in range(2018, 2023)]
MONTHS_LIST = [str(month) for month in range(1, 13)]
year = YEARS_LIST[0]
month = MONTHS_LIST[0]

stats_aeroports = summary_stat_airport(create_data_from_input(pax_apt_all, year, month))

stats_aeroports['name_clean'] = stats_aeroports['apt_nom'].str.title() + " _(" + stats_aeroports['apt'] + ")_"
stats_aeroports = stats_aeroports[['name_clean'] + [col for col in stats_aeroports.columns if col != 'name_clean']]
