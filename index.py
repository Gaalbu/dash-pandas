from dash import html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from app import *
from dash_bootstrap_templates import ThemeSwitchAIO
import dash_bootstrap_components as dbc
#LENDO AS INFORMAÇÕES
df = pd.read_csv('dadosUniversdade_limpo.csv')
#Layouttttt
app.layout = dbc.Container([
    html.H1('Teste'),
    html.H3('aaa')
])

#Rodar o servidor -> RODOU
if __name__ == '__main__':
    app.run(debug=True)