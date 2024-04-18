import solara
from dotenv import load_dotenv
import plotly.express as px
import os

from marizaapp.data import data

public_baths = data['public_baths']

load_dotenv()

name = public_baths['properties.name']

@solara.component
def Page():
    with solara.Sidebar():
        solara.HTML("blabla")

    with solara.Card():
        px.set_mapbox_access_token(os.getenv('MAPBOX_ACCESS_TOKEN'))
        fig = px.scatter_mapbox(public_baths, lat='lat', lon='lon', hover_name='properties.name', )
        solara.FigurePlotly(fig)
