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
url_theme2 = dbc.themes.QUARTZ
template_theme1 = 'vapor'
template_theme2 = 'quartz'


#LENDO AS INFORMAÇÕES===================================
df = pd.read_csv('dadosUniversdade_limpo.csv')
#Layouttttt=============================================
app.layout = dbc.Container([
    #primeira linha
    dbc.Row([
        dbc.Col([
            ThemeSwitchAIO(aio_id='theme', themes=[url_theme2, url_theme1]),
            html.H1('Análise de inscrições em universidades(2022-2023)'),
            html.H3('Pagamentos x Distritos'),
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
    dbc.Row([
        dbc.Col([
            html.H3("Disparidade de Gênero por Curso"),
            dcc.Dropdown(
                    id='genero_curso_seletor',
                    options=major_options,  
                    value=[major['label'] for major in major_options[:3]],
                    multi=True
                ),
            dcc.Graph(id='disparidade_genero_grafico')
        ])
    ]),
    #terceira linha========================================
])

# Callbacks==============================================
@app.callback(
    Output('line_graph', 'figure'),
    Input('district', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)
def update_bar_plot(selected_districts, toggle):
    template = template_theme2 if toggle else template_theme1
    dfFILTRADOO = df[df['DISTRICT'].isin(selected_districts)]
    pagamentoPorDistrito = dfFILTRADOO.groupby('DISTRICT')['TUITION PAYMENT MARCH 2022'].sum().reset_index()

    fig = px.bar(
        pagamentoPorDistrito,
        x='DISTRICT',
        y='TUITION PAYMENT MARCH 2022',
        template=template,
        color='DISTRICT',
        text_auto=True
    )

    fig.update_layout(yaxis_title='Total de Pagamento (R$)', xaxis_title='Distrito')

    return fig


@app.callback(
    Output('disparidade_genero_grafico', 'figure'),
    Input('genero_curso_seletor', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)
def update_gender_disparity(cursoSelecionado, toggle):
    template = template_theme2 if toggle else template_theme1
    dfFILTRADO = df[df['PROGRAM/MAJOR'].isin(cursoSelecionado)]
    countsGenero = dfFILTRADO.groupby(['PROGRAM/MAJOR', 'GENDER']).size().reset_index(name='contagem')


    fig = px.bar(
        countsGenero,
        x='PROGRAM/MAJOR',
        y='contagem',
        color='GENDER',
        barmode='stack',
        template=template,
    )

    fig.update_layout(xaxis_tickangle=-45,xaxis_title='Curso',yaxis_title='Número de Inscrições')

    return fig


#Rodar o servidor -> RODOU
if __name__ == '__main__':
    app.run(debug=True, port='8050')
