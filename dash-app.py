import os
import dash
import pandas as pd
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

# App creation
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Read data from csv file
df = pd.read_csv(os.environ['POPULAR_SONGS_DATA'])

# Find the average by country for each audio features
df_kpi = df.groupby('country').mean()[['energy', 'danceability', 'acousticness',
                                       'liveness', 'valence', 'speechiness']]

categories = list(df_kpi.columns)

countries = list(df_kpi.index.values)

# Select multiple countries
country_select = dcc.Dropdown(
    id='selector',
    options=[{'label': c, 'value': c} for c in countries],
    value=['Colombia'],
    multi=True
)

# Heatmap graph
fig_heatmap = go.Figure(data=go.Heatmap(
    z=[df_kpi[a].values.tolist() for a in categories],
    x=countries,
    y=categories,
    colorscale='Portland',
    hoverongaps=False))

# Defining layout for tab1
tab1_content = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_heatmap)
    ]),
    className="mt-3",
)

# Defining layout for tab2
tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div([
                dbc.Row(dbc.Col(country_select, width={"size": 6, "offset": 3})),
                dbc.Row(dbc.Col(dcc.Graph(id='graph-container'), width={"size": 6, "offset": 3}))
            ], style={"padding-top": "20px"})
        ]
    ),
    className="mt-3",
)

# Setting general layout for dash app
app.layout = dbc.Container([
    html.H1("Popular Songs!"),
    html.Hr(),
    dbc.Tabs(
        [
            dbc.Tab(label='Audio Features Heatmap', tab_id='heatmap', children=tab1_content),
            dbc.Tab(label='Compare countries', tab_id='scatter_polar', children=tab2_content)
        ],
        id='tabs',
        active_tab='heatmap'
    ),
    html.Div(id='tab-content', className='p-4')
])


# Defining a callback function for return a figure with filtered data
@app.callback(Output('graph-container', 'figure'),
              [Input('selector', 'value')])
def compare_countries(value):
    """
    This callback updates scatter polar graph based on filter's selected options.
    :param value: selected countries
    :return: Scatter polar graph
    """
    fig = go.Figure()

    filter_df = df_kpi[df_kpi.index.isin(value)]

    for index, row in filter_df.iterrows():
        fig.add_trace(go.Scatterpolar(
            r=row.values.flatten().tolist(),
            theta=categories,
            fill='toself',
            name=index
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )),
        showlegend=True,
        width=700,
        height=700
    )
    return fig


# Run app
app.run_server(debug=True, use_reloader=True)
