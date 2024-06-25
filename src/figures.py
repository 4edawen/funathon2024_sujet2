import plotly.express as px
import pandas as pd


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
