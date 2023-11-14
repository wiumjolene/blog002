import dash
import dash_bootstrap_components as dbc

import pandas as pd

from visuals import MakeVisualisation
from get_data import ManageCoordinates

mv = MakeVisualisation()
mc = ManageCoordinates()


df=mc.manage_vessels()
coastline=mc.get_coastline()
fig = mv.make_mapboxplot(df, coastline)

dash_app = dash.Dash(__name__,
                     external_stylesheets=[dbc.themes.MINTY, 
                                           dbc.icons.FONT_AWESOME])
dash_app.title = 'Blog post about RSA load ports'
app = dash_app.server


first_card = dbc.Card(
    dbc.CardBody(
        [
            dash.html.H5("Explanation", className="card-title"),
            dash.html.P(mc.get_text_for_dash()),
        ]
    )
)

second_card = dbc.Card(
    dbc.CardBody(
        [
            dash.dcc.Graph(
                        id='example-graph',
                        figure=fig
                    ),
        ]
    )
)

cards = dbc.Row(
    [
        dbc.Col(first_card, width=4),
        dbc.Col(second_card, width=8),
    ]
)

footer = dash.html.Div(
    dash.html.P(
        """
        This is site maintained and hosted by Jolene Wium on Azure web services.
        """
    ),
    className="p-2 mt-5 bg-light text-dark small",
)

dash_app.layout = dbc.Container(
        [
            dbc.Row(
                dbc.Col([
                    dash.html.H2(
                        "Boost your analytics workflow with Python!",
                        className="text-center bg-primary text-white p-2",
                    ),]
                )
            ),
            cards ,
            dbc.Row(dbc.Col(footer)),
        ],
        fluid=True,
    )


if __name__ == '__main__':
    dash_app.run_server(debug=False)

