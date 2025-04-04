from dash import html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from Project import *
from app import *
from dash_bootstrap_templates import ThemeSwitchAIO
import dash_bootstrap_components as dbc

#ESTILOS================================================
url_theme1 = dbc.themes.VAPOR
url_theme2 = dbc.themes.FLATLY
template_theme1 = 'vapor'
template_theme2 = 'flatly'


#LENDO AS INFORMAÇÕES===================================
df = pd.read_csv('dadosUniversdade_limpo.csv')
#Layouttttt=============================================
app.layout = dbc.Container([
    #primeira linha
    dbc.Row([
        dbc.Col([
            ThemeSwitchAIO(aio_id='theme', themes=[url_theme2, url_theme1]),
            html.H3('Analise de inscrições na universidade'),
            dcc.Dropdown(
                id='district',
                value=[district['label'] for district in district_options[:3]],
                multi=True,
                options=district_options
            ),
            dcc.Graph(id='line_graph')
        ])
    ]),
    #segunda linha=======================================
])

# Callbacks==============================================
@app.callback(
    Output('line_graph', 'figure'),
    Input('district', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)
def line(district, toggle):
    template = template_theme2 if toggle else template_theme1

    print(district)
    df_data = df2.copy(deep=True)
    mask = df_data['DISTRICT'].isin(district)

    fig = px.line(df_data[mask], x='TUITION PAYMENT MARCH 2022', y='PROGRAM/MAJOR',
                  color='DISTRICT', template=template)

    return fig

#Rodar o servidor -> RODOU
if __name__ == '__main__':
    app.run(debug=True, port='8051')
