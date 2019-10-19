#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go
from plotly.graph_objs import *

# Plotly mapbox public token
mapbox_access_token = 'pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNqdnBvNDMyaTAxYzkzeW5ubWdpZ2VjbmMifQ.TXcBE-xg9BFdV2ocecc_7g'


from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-pieplot/code", width="100%", height=500 ,frameBorder="0")

if 'DYNO' in os.environ:
    app_name = os.environ['DASH_APP_NAME']
else:
    app_name = 'dash-pieplot'



#############

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#############

mun_sp = pd.read_csv('mun_sp.csv')

mun_sp_1 = mun_sp[['ds_municipio', 'latitude', 'longitude']]

mun_sp_2 = mun_sp_1.set_index('ds_municipio').T.to_dict('list')


#consolida base de perguntas e respostas
file_name =  "Metas_ODS_filtrado.xlsx"
sheet =  "Sheet1"
perguntas_metas = pd.read_excel(io=file_name, sheet_name=sheet)

#To select rows whose column value is in list 
ods_item = [6, 6.1, 6.4, 6.5]
perguntas_metas_san = perguntas_metas[perguntas_metas.ods_item.isin(ods_item)]
perguntas_metas_san.columns = perguntas_metas_san.columns.str.strip().str.lower().str.replace(' ', '_')

#respostas dos municipios às perguntas
respostas = pd.read_csv("iegm.csv", sep=';',engine='python', encoding='latin-1')

#filtrando respostas às perguntas das metas da ODS
respostas_metas_san = respostas[respostas.cod_pergunta.isin(perguntas_metas_san.iegm_pergunta_codigo.unique())]
respostas_metas_san.columns = respostas_metas_san.columns.str.strip().str.lower().str.replace(' ', '_')

respostas_consol = respostas_metas_san.merge(perguntas_metas_san,left_on=['cod_pergunta','cod_resposta','ano_exercicio'], right_on=['iegm_pergunta_codigo','iegm_opcao_resposta_codigo','ano_base'], how='left')

#dataframe para grafico de porte
porte = respostas_consol[['municipio','porte','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
porte2 = porte.groupby(["ano_exercicio", "porte"])["municipio"].count().reset_index(name="count")

#dataframe para pergunta1
pergunta1 = respostas_consol[respostas_consol.cod_pergunta.isin(['M05Q01100'])]
pergunta1_2 = pergunta1[['municipio','valor_resposta','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
pergunta1_3 = pergunta1_2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

respostas_total1 = pergunta1_2.copy()
respostas_total1['municipio']='todas'
pergunta1t = respostas_total1.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

frames1 = [pergunta1t, pergunta1_3]
result1 = pd.concat(frames1)

#dataframe para pergunta2
pergunta2 = respostas_consol[respostas_consol.cod_pergunta.isin(['M05Q01100'])]
pergunta2_2 = pergunta2[['municipio','valor_resposta','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
pergunta2_3 = pergunta2_2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

respostas_total2 = pergunta2_2.copy()
respostas_total2['municipio']='todas'
pergunta2t = respostas_total2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

frames2 = [pergunta2t, pergunta2_3]
result2 = pd.concat(frames2)

#dataframe para pergunta3
pergunta3 = respostas_consol[respostas_consol.cod_pergunta.isin(['M05Q02000'])]
pergunta3_2 = pergunta3[['municipio','valor_resposta','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
pergunta3_3 = pergunta3_2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

respostas_total3 = pergunta3_2.copy()
respostas_total3['municipio']='todas'
pergunta3t = respostas_total3.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

frames3 = [pergunta3t, pergunta3_3]
result3 = pd.concat(frames3)

#dataframe para pergunta4
pergunta4 = respostas_consol[respostas_consol.cod_pergunta.isin(['M05Q02100'])]
pergunta4_2 = pergunta4[['municipio','valor_resposta','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
pergunta4_3 = pergunta4_2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

respostas_total4 = pergunta4_2.copy()
respostas_total4['municipio']='todas'
pergunta4t = respostas_total4.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

frames4 = [pergunta4t, pergunta4_3]
result4 = pd.concat(frames4)

#dataframe para pergunta5
pergunta5 = respostas_consol[respostas_consol.cod_pergunta.isin(['M05Q02700'])]
pergunta5_2 = pergunta5[['municipio','valor_resposta','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
pergunta5_3 = pergunta5_2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

respostas_total5 = pergunta5_2.copy()
respostas_total5['municipio']='todas'
pergunta5t = respostas_total5.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

frames5 = [pergunta5t, pergunta5_3]
result5 = pd.concat(frames5)

#dataframe para pergunta6
pergunta6 = respostas_consol[respostas_consol.cod_pergunta.isin(['M05Q02800'])]
pergunta6_2 = pergunta6[['municipio','valor_resposta','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
pergunta6_3 = pergunta6_2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

respostas_total6 = pergunta6_2.copy()
respostas_total6['municipio']='todas'
pergunta6t = respostas_total6.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

frames6 = [pergunta6t, pergunta6_3]
result6 = pd.concat(frames6)

#dataframe para pergunta7
pergunta7 = respostas_consol[respostas_consol.cod_pergunta.isin(['M05Q01600'])]
pergunta7_2 = pergunta7[['municipio','valor_resposta','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
pergunta7_3 = pergunta7_2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

respostas_total7 = pergunta7_2.copy()
respostas_total7['municipio']='todas'
pergunta7t = respostas_total7.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

frames7 = [pergunta7t, pergunta7_3]
result7 = pd.concat(frames7)

#dataframe para pergunta8
pergunta8 = respostas_consol[respostas_consol.cod_pergunta.isin(['M05Q01700'])]
pergunta8_2 = pergunta8[['municipio','valor_resposta','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
pergunta8_3 = pergunta8_2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

respostas_total8 = pergunta8_2.copy()
respostas_total8['municipio']='todas'
pergunta8t = respostas_total8.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

frames8 = [pergunta8t, pergunta8_3]
result8 = pd.concat(frames8)

#dataframe para pergunta9
pergunta9 = respostas_consol[respostas_consol.cod_pergunta.isin(['M05Q01800'])]
pergunta9_2 = pergunta9[['municipio','valor_resposta','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
pergunta9_3 = pergunta9_2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

respostas_total9 = pergunta9_2.copy()
respostas_total9['municipio']='todas'
pergunta9t = respostas_total9.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

frames9 = [pergunta9t, pergunta9_3]
result9 = pd.concat(frames9)

#dataframe para pergunta10
pergunta10 = respostas_consol[respostas_consol.cod_pergunta.isin(['M05Q01900'])]
pergunta10_2 = pergunta10[['municipio','valor_resposta','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
pergunta10_3 = pergunta10_2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

respostas_total10 = pergunta10_2.copy()
respostas_total10['municipio']='todas'
pergunta10t = respostas_total10.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

frames10 = [pergunta10t, pergunta10_3]
result10 = pd.concat(frames10)

#dataframe para pergunta11
pergunta11 = respostas_consol[respostas_consol.cod_pergunta.isin(['M05Q01600'])]
pergunta11_2 = pergunta11[['municipio','valor_resposta','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
pergunta11_3 = pergunta11_2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

respostas_total11 = pergunta11_2.copy()
respostas_total11['municipio']='todas'
pergunta11t = respostas_total11.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

frames11 = [pergunta11t, pergunta11_3]
result11 = pd.concat(frames11)

#dataframe para pergunta12
pergunta12 = respostas_consol[respostas_consol.cod_pergunta.isin(['M05Q01700'])]
pergunta12_2 = pergunta12[['municipio','valor_resposta','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
pergunta12_3 = pergunta12_2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

respostas_total12 = pergunta12_2.copy()
respostas_total12['municipio']='todas'
pergunta12t = respostas_total12.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

frames12 = [pergunta12t, pergunta12_3]
result12 = pd.concat(frames12)

#dataframe para pergunta13
pergunta13 = respostas_consol[respostas_consol.cod_pergunta.isin(['M05Q01800'])]
pergunta13_2 = pergunta13[['municipio','valor_resposta','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
pergunta13_3 = pergunta13_2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

respostas_total13 = pergunta13_2.copy()
respostas_total13['municipio']='todas'
pergunta13t = respostas_total13.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

frames13 = [pergunta13t, pergunta13_3]
result13 = pd.concat(frames13)

#dataframe para pergunta14
pergunta14 = respostas_consol[respostas_consol.cod_pergunta.isin(['M05Q01900'])]
pergunta14_2 = pergunta14[['municipio','valor_resposta','ano_exercicio']].drop_duplicates(subset=None, keep='first', inplace=False)
pergunta14_3 = pergunta14_2.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

respostas_total14 = pergunta14_2.copy()
respostas_total14['municipio']='todas'
pergunta14t = respostas_total14.groupby(["municipio", "ano_exercicio", "valor_resposta"])["municipio"].count().reset_index(name="count")

frames14 = [pergunta14t, pergunta14_3]
result14 = pd.concat(frames14)

#gera tabela para plotar no dash
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


#preenche as lacunas com ''
respostas_consol['municipio'] = respostas_consol['municipio'].fillna('')
municipios = result1['municipio'].unique()
ano_exercicio = respostas_consol['ano_exercicio'].unique()

app.layout = html.Div([
    
    html.H1(children='Objetivos de Desenvolvimento Sustentável'),

    html.H2(children='''
        6. Água potável e saneamento
    '''),

    html.Div([
        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in municipios],
                value='value'
            )
        ],style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in ano_exercicio],
                value='label'
            )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})


    ]),

    html.Div([
      html.Div([html.H1("Distribuição de Portes")],
        style={"textAlign": "center"}),
    dcc.Graph(id="my-graph")
    ], 
        className="container"),
        
    html.Div([
    html.Div([
# Dropdown for locations on map
        dcc.Dropdown(
            id="location-dropdown",
            options=[{"label": key, "value": key} for key,value in mun_sp_2.items()],
            placeholder="Select a location"
        )
    ],style={'width': '40%', 'display': 'inline-block'}),

    html.Div([html.H1("Mapa dos municípios")], style={"textAlign": "center"}),
        dcc.Graph(id="my-graph15"),
    ],className="container"),

    html.Div([
    html.Div([html.H1("Meta 6.0")], style={"textAlign": "center"}),
    dcc.Graph(id="my-graph2"),
    dcc.Graph(id="my-graph3"),
    dcc.Graph(id="my-graph4"),
    dcc.Graph(id="my-graph5"),
    dcc.Graph(id="my-graph6"),
    ], className="container"),

    html.Div([
    html.Div([html.H1("Meta 6.4")], style={"textAlign": "center"}),
    dcc.Graph(id="my-graph7"),
    dcc.Graph(id="my-graph8"),
    dcc.Graph(id="my-graph9"),
    dcc.Graph(id="my-graph10")
    ], className="container"),

    html.Div([
    html.Div([html.H1("Meta 6.5")], style={"textAlign": "center"}),
    dcc.Graph(id="my-graph11"),
    dcc.Graph(id="my-graph12"),
    dcc.Graph(id="my-graph13"),
    dcc.Graph(id="my-graph14")
    ], className="container"),

    html.H4(children='TABELA'),
    generate_table(respostas_consol)
])

@app.callback(
    dash.dependencies.Output("my-graph", "figure"),
    [dash.dependencies.Input("yaxis-column", "value")]
)
def update_graph(selected):
    return {
        "data": [go.Pie(labels=porte2["porte"].unique().tolist(), values=porte2[porte2["ano_exercicio"] == selected]["count"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title=f"Distribuição de Portes", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}

#####

@app.callback(
    dash.dependencies.Output("my-graph2", "figure"),
    [dash.dependencies.Input("yaxis-column", "value"),
    dash.dependencies.Input("xaxis-column", "value")]
)
def update_graph_1(selected1, selected2):
    return {
        "data": [go.Pie(labels=result1["valor_resposta"].unique().tolist(), values=result1[(result1["ano_exercicio"].astype(int) == selected1) & (result1["municipio"] == selected2)]["count"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title=f"O município possui seu Plano Municipal de Saneamento Básico instituído?", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}

#######

@app.callback(
    dash.dependencies.Output("my-graph3", "figure"),
    [dash.dependencies.Input("yaxis-column", "value"),
    dash.dependencies.Input("xaxis-column", "value")]
)
def update_graph_2(selected1, selected2):
    return {
        "data": [go.Pie(labels=result2["valor_resposta"].unique().tolist(), values=result2[(result2["ano_exercicio"].astype(int) == selected1) & (result2["municipio"] == selected2)]["count"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title=f"O município participa do programa Município VerdeAzul?", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}

@app.callback(
    dash.dependencies.Output("my-graph4", "figure"),
    [dash.dependencies.Input("yaxis-column", "value"),
    dash.dependencies.Input("xaxis-column", "value")]
)
def update_graph_3(selected1, selected2):
    return {
        "data": [go.Pie(labels=result3["valor_resposta"].unique().tolist(), values=result3[(result3["ano_exercicio"].astype(int) == selected1) & (result3["municipio"] == selected2)]["count"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title=f"O município está habilitado junto ao CONSEMA para licenciar os empreendimentos de impacto local de conformidade com a Deliberação Normativa Consema 01/2014?", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}

@app.callback(
    dash.dependencies.Output("my-graph5", "figure"),
    [dash.dependencies.Input("yaxis-column", "value"),
    dash.dependencies.Input("xaxis-column", "value")]
)
def update_graph_4(selected1, selected2):
    return {
        "data": [go.Pie(labels=result4["valor_resposta"].unique().tolist(), values=result4[(result4["ano_exercicio"].astype(int) == selected1) & (result4["municipio"] == selected2)]["count"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title=f"Os serviços de abastecimento e distribuição de água são executados de forma direta pelo município?", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}

@app.callback(
    dash.dependencies.Output("my-graph6", "figure"),
    [dash.dependencies.Input("yaxis-column", "value"),
    dash.dependencies.Input("xaxis-column", "value")]
)
def update_graph_5(selected1, selected2):
    return {
        "data": [go.Pie(labels=result5["valor_resposta"].unique().tolist(), values=result5[(result5["ano_exercicio"].astype(int) == selected1) & (result5["municipio"] == selected2)]["count"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title=f"Os serviços de coleta e tratamento de esgoto são executados de forma direta pelo Município?", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}

@app.callback(
    dash.dependencies.Output("my-graph7", "figure"),
    [dash.dependencies.Input("yaxis-column", "value"),
    dash.dependencies.Input("xaxis-column", "value")]
)
def update_graph_6(selected1, selected2):
    return {
        "data": [go.Pie(labels=result6["valor_resposta"].unique().tolist(), values=result6[(result6["ano_exercicio"].astype(int) == selected1) & (result6["municipio"] == selected2)]["count"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title=f"Existem ações e medidas de contingenciamento para os períodos de estiagem?", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}

@app.callback(
    dash.dependencies.Output("my-graph8", "figure"),
    [dash.dependencies.Input("yaxis-column", "value"),
    dash.dependencies.Input("xaxis-column", "value")]
)
def update_graph_7(selected1, selected2):
    return {
        "data": [go.Pie(labels=result7["valor_resposta"].unique().tolist(), values=result7[(result7["ano_exercicio"].astype(int) == selected1) & (result7["municipio"] == selected2)]["count"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title=f"Existem ações e medidas de contingenciamento para provisão de água potável e de uso comum para a Rede Municipal de Ensino?", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}

@app.callback(
    dash.dependencies.Output("my-graph9", "figure"),
    [dash.dependencies.Input("yaxis-column", "value"),
    dash.dependencies.Input("xaxis-column", "value")]
)
def update_graph_8(selected1, selected2):
    return {
        "data": [go.Pie(labels=result8["valor_resposta"].unique().tolist(), values=result8[(result8["ano_exercicio"].astype(int) == selected1) & (result8["municipio"] == selected2)]["count"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title=f"Existem ações e medidas de contingenciamento para provisão de água potável e de uso comum para a rede municipal da Atenção Básica da Saúde?", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}

@app.callback(
    dash.dependencies.Output("my-graph10", "figure"),
    [dash.dependencies.Input("yaxis-column", "value"),
    dash.dependencies.Input("xaxis-column", "value")]
)
def update_graph_9(selected1, selected2):
    return {
        "data": [go.Pie(labels=result9["valor_resposta"].unique().tolist(), values=result9[(result9["ano_exercicio"].astype(int) == selected1) & (result9["municipio"] == selected2)]["count"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title=f"Há um plano emergencial com ações para fornecimento de água potável à população em caso de sua escassez?", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}


@app.callback(
    dash.dependencies.Output("my-graph11", "figure"),
    [dash.dependencies.Input("yaxis-column", "value"),
    dash.dependencies.Input("xaxis-column", "value")]
)
def update_graph_10(selected1, selected2):
    return {
        "data": [go.Pie(labels=result10["valor_resposta"].unique().tolist(), values=result10[(result10["ano_exercicio"].astype(int) == selected1) & (result10["municipio"] == selected2)]["count"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title=f"Existem ações e medidas de contingenciamento para os períodos de estiagem?", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}


@app.callback(
    dash.dependencies.Output("my-graph12", "figure"),
    [dash.dependencies.Input("yaxis-column", "value"),
    dash.dependencies.Input("xaxis-column", "value")]
)
def update_graph_11(selected1, selected2):
    return {
        "data": [go.Pie(labels=result11["valor_resposta"].unique().tolist(), values=result11[(result11["ano_exercicio"].astype(int) == selected1) & (result11["municipio"] == selected2)]["count"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title=f"Existem ações e medidas de contingenciamento para provisão de água potável e de uso comum para a Rede Municipal de Ensino?", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}

@app.callback(
    dash.dependencies.Output("my-graph13", "figure"),
    [dash.dependencies.Input("yaxis-column", "value"),
    dash.dependencies.Input("xaxis-column", "value")]
)
def update_graph_12(selected1, selected2):
    return {
        "data": [go.Pie(labels=result12["valor_resposta"].unique().tolist(), values=result12[(result12["ano_exercicio"].astype(int) == selected1) & (result12["municipio"] == selected2)]["count"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title=f"Existem ações e medidas de contingenciamento para provisão de água potável e de uso comum para a rede municipal da Atenção Básica da Saúde?", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}


@app.callback(
    dash.dependencies.Output("my-graph14", "figure"),
    [dash.dependencies.Input("yaxis-column", "value"),
    dash.dependencies.Input("xaxis-column", "value")]
)
def update_graph_13(selected1, selected2):
    return {
        "data": [go.Pie(labels=result13["valor_resposta"].unique().tolist(), values=result13[(result13["ano_exercicio"].astype(int) == selected1) & (result13["municipio"] == selected2)]["count"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title=f"Há um plano emergencial com ações para fornecimento de água potável à população em caso de sua escassez?", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}

# Update Map Graph based on date-picker, selected data on histogram and location dropdown

@app.callback(
    dash.dependencies.Output("my-graph15", "figure"),
    [

        dash.dependencies.Input("location-dropdown", "value")
    ],
)

def update_graph_15(selectedLocation):
    zoom = 12.0
    latInitial = -23.5489
    lonInitial = -46.6388
    bearing = 0

    if selectedLocation:
        zoom = 15.0
        latInitial = mun_sp_2[selectedLocation][0]
        lonInitial = mun_sp_2[selectedLocation][-1]



    return go.Figure(
        data=[
            # Data for all rides based on date and time
            Scattermapbox(
                lat=[mun_sp_2[i][0] for i in mun_sp_2],
                lon=[mun_sp_2[i][-1] for i in mun_sp_2],
                mode="markers",
                hoverinfo="lat+lon+text",
                marker=dict(
                    showscale=True,
                    opacity=0.5,
                    size=5,
                    colorscale=[
                        [0, "#F4EC15"],
                        [0.04167, "#DAF017"],
                        [0.0833, "#BBEC19"],
                        [0.125, "#9DE81B"],
                        [0.1667, "#80E41D"],
                        [0.2083, "#66E01F"],
                        [0.25, "#4CDC20"],
                        [0.292, "#34D822"],
                        [0.333, "#24D249"],
                        [0.375, "#25D042"],
                        [0.4167, "#26CC58"],
                        [0.4583, "#28C86D"],
                        [0.50, "#29C481"],
                        [0.54167, "#2AC093"],
                        [0.5833, "#2BBCA4"],
                        [1.0, "#613099"],
                    ],
                    colorbar=dict(
                        title="Time of<br>Day",
                        x=0.93,
                        xpad=0,
                        nticks=24,
                        tickfont=dict(color="#d8d8d8"),
                        titlefont=dict(color="#d8d8d8"),
                        thicknessmode="pixels",
                    ),
                ),
            ),
            # Plot of important locations on the map
            Scattermapbox(
                lat=[mun_sp_2[i][0] for i in mun_sp_2],
                lon=[mun_sp_2[i][-1] for i in mun_sp_2],
                mode="markers",
                hoverinfo="text",
                text=[i for i in mun_sp_2],
                marker=dict(size=8, color="#ffa0a0"),
            ),
        ],
        layout=Layout(
            autosize=True,
            margin=go.layout.Margin(l=0, r=35, t=0, b=0),
            showlegend=False,
            mapbox=dict(
                accesstoken=mapbox_access_token,
                center=dict(lat=latInitial, lon=lonInitial),  # 40.7272  # -73.991251
                style="dark",
                bearing=bearing,
                zoom=zoom,
            ),
            updatemenus=[
                dict(
                    buttons=(
                        [
                            dict(
                                args=[
                                    {
                                        "mapbox.zoom": 12,
                                        "mapbox.center.lon": "-46.6388",
                                        "mapbox.center.lat": "-23.5489",
                                        "mapbox.bearing": 0,
                                        "mapbox.style": "dark",
                                    }
                                ],
                                label="Reset Zoom",
                                method="relayout",
                            )
                        ]
                    ),
                    direction="left",
                    pad={"r": 0, "t": 0, "b": 0, "l": 0},
                    showactive=False,
                    type="buttons",
                    x=0.45,
                    y=0.02,
                    xanchor="left",
                    yanchor="bottom",
                    bgcolor="#323130",
                    borderwidth=1,
                    bordercolor="#6d6d6d",
                    font=dict(color="#FFFFFF"),
                )
            ],
        ),
    )

if __name__ == '__main__':
    app.run_server(debug=True)