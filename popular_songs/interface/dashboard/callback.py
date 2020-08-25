import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html

from .data import DashController


def init_callback(app):
    @app.callback(Output('graph-container', 'figure'),
                  [Input('selector', 'value'),
                   Input('memory-output', 'data')])
    def compare_countries(value, data):
        """
        This callback updates scatter polar graph based on filter's selected options.
        :param value: selected countries
        :return: Scatter polar graph
        """
        if data is None:
            raise PreventUpdate

        df = pd.DataFrame.from_dict(data)
        categories = list(df.columns)

        fig = go.Figure()

        filter_df = df[df.index.isin(value)]

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

    @app.callback([Output('memory-output', 'data'),
                   Output('loading-data-div', 'children')],
                  [Input('date-selector', 'date')])
    def get_data_from_date(date):
        if date is None:
            raise PreventUpdate
        dc = DashController(date)

        df = dc.create_dataframe()
        kpi = dc.get_kpi_from_df(df)

        return kpi.to_dict(), html.Div()

    @app.callback(Output('container-heatmap', 'children'),
                  [Input('memory-output', 'data')])
    def on_data_set_heatmap(data):
        df = pd.DataFrame.from_dict(data)
        categories = list(df.columns)
        countries = list(df.index.values)

        fig_heatmap = go.Figure(data=go.Heatmap(
            z=[df[a].values.tolist() for a in categories],
            x=countries,
            y=categories,
            colorscale='Portland',
            hoverongaps=False))

        return dcc.Graph(figure=fig_heatmap)

    @app.callback(Output('selector', 'options'),
                  [Input('memory-output', 'data')])
    def on_data_set_country_selector(data):
        df = pd.DataFrame.from_dict(data)
        countries = list(df.index.values)

        return [{'label': c, 'value': c} for c in countries]

