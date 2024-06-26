import plotly.express as px
import pandas as pd
import folium
from src.divers_functions import create_data_from_input


def traffic_airport(dataframe, airport):
    dataframe["traffic"] = dataframe["apt_pax_dep"]+dataframe["apt_pax_tr"]+dataframe["apt_pax_arr"]
    pax_apt_airport = dataframe.set_index('apt').filter(like=airport, axis=0)
    pax_apt_airport["date"] = pd.to_datetime(
        pax_apt_airport["an"]+"/" + pax_apt_airport["mois"],
        format='%Y/%m')
    return pax_apt_airport


def plot_airport_line(dataframe, airport):
    airport_traffic_data = traffic_airport(dataframe, airport)
    fig = px.line(
        airport_traffic_data, x="date", y="traffic", title='Title', text="apt_nom",
        markers=True)
    fig.update_traces(
        mode="markers+lines", type="scatter",
        hovertemplate="<i>Aéroport:</i> %{text}<br>Trafic: %{y}"
    )
    return fig


def map_leaflet_airport(dataframe, airports_location, month, year):
    palette = ['green', 'orange', 'red']

    dataframe['date'] = pd.to_datetime(dataframe['anmois'] + '01', format='%Y%m%d')
    pd.options.mode.copy_on_write = True
    trafic_date = create_data_from_input(dataframe, year, month)
    trafic_date['volume'] = pd.qcut(x=trafic_date.traffic, q=3, labels=[1, 2, 3])
    trafic_aeroports = airports_location.merge(
        trafic_date,
        how='inner',
        left_on='Code.OACI',
        right_on='apt',
        suffixes=["_x", ""])
    trafic_aeroports['date'] = trafic_aeroports['date'].dt.strftime('%Y-%m-%d')
    trafic_aeroports['palette'] = trafic_aeroports['volume'].apply(lambda x: palette[x-1])

    map = folium.Map()

    for idx, row in trafic_aeroports.iterrows():
        coord = row['geometry']
        name = row['Nom']
        code_oaci = row['Code.OACI']
        trafic = int(row['trafic'])
        color = row['palette']
        popup_content = f"{name} ({code_oaci}) : {trafic} voyageurs"
        folium.Marker(
            location=[coord.y, coord.x],
            popup=folium.Popup(popup_content, parse_html=True),
            icon=folium.Icon(icon="send", color=color)
            ).add_to(map)

    return map
