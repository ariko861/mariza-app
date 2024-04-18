import solara
from dotenv import load_dotenv
import plotly.express as px
import os

from marizaapp.data import prepare_dataframe_from_geojson

data_dir = 'datas'
load_dotenv()


data_set = os.listdir(data_dir)
data = solara.reactive(data_set[0])
public_baths = prepare_dataframe_from_geojson(os.path.join(data_dir, data.value))

@solara.component
def Page():

    px.set_mapbox_access_token(os.getenv('MAPBOX_ACCESS_TOKEN'))
    fig = px.scatter_mapbox(prepare_dataframe_from_geojson(os.path.join(data_dir, data.value)), lat='lat', lon='lon', hover_data=['properties.name', 'properties.website'], height=800, zoom=3 )
    solara.FigurePlotly(fig)
    with solara.Card():
        solara.Select(label="Food", value=data, values=data_set)
