from dash import (
    html,
    dcc
)

import dash

from utils.data_loader import load_data


dash.register_page(__name__)

df = load_data()


layout = html.Div(

    [

        dcc.Store(
            id="clients-filters-store",
            storage_type="local"
        ),

        html.H1("Analyse Clients"),

        html.Div(

            [

                dcc.Dropdown(

                    id="client-region-filter",

                    options=[

                        {
                            "label":i,
                            "value":i
                        }

                        for i in sorted(
                            df["region"]
                            .dropna()
                            .unique()
                        )
                    ],

                    multi=True,

                    placeholder="Région"
                ),

                dcc.Dropdown(

                    id="client-sexe-filter",

                    options=[

                        {
                            "label":i,
                            "value":i
                        }

                        for i in sorted(
                            df["sexe"]
                            .dropna()
                            .unique()
                        )
                    ],

                    multi=True,

                    placeholder="Sexe"
                )

            ],

            style={
                "display":"flex",
                "gap":"20px",
                "marginBottom":"20px"
            }
        ),

        html.Div(
            id="clients-kpi"
        ),

        dcc.Graph(
            id="clients-region-graph"
        ),

        dcc.Graph(
            id="clients-service-graph"
        ),

        dcc.Graph(
            id="clients-sexe-graph"
        )

    ]
)