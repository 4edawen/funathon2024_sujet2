import geopandas as gpd

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
stats_aeroports = summary_stat_airport(create_data_from_input(pax_apt_all, year, month))

# Valorisation --

figure_plotly = plot_airport_line(pax_apt_all, default_airport)

table_airports = create_table_airports(stats_aeroports)

carte_interactive = map_leaflet_airport(pax_apt_all, airports_location, month, year)
