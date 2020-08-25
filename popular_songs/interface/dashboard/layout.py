from datetime import datetime as dt
from datetime import date
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


def get_app_layout():
    date_select = dcc.DatePickerSingle(
        id='date-selector',
        min_date_allowed=dt(2020, 8, 1),
        max_date_allowed=date.today(),
        initial_visible_month=dt(2020, 8, 1)
    )
    country_select = dcc.Dropdown(
        id='selector',
        value=['Colombia'],
        multi=True
    )

    tab1_content = dbc.Card(
        dbc.CardBody([
            dcc.Loading(
                id="loading-1",
                type="default",
                children=html.Div(id="container-heatmap")
            )
        ]),
        className="mt-3",
    )

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
    return dbc.Container([
        dcc.Store(id='memory-output'),
        html.H1("Popular Songs!"),
        html.Hr(),
        html.Div([date_select]),
        dcc.Loading(
            id="loading-2",
            type="default",
            children=html.Div(id="loading-data-div")
        ),
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
