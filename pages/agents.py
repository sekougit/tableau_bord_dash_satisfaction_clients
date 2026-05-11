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
            id="agents-filters-store",
            storage_type="local"
        ),

        html.H1("Analyse Agents"),

        html.Div(

            [

                dcc.Dropdown(

                    id="agent-region-filter",

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

                    id="agent-filter",

                    options=[

                        {
                            "label":i,
                            "value":i
                        }

                        for i in sorted(
                            df["agent_appel"]
                            .dropna()
                            .unique()
                        )
                    ],

                    multi=True,

                    placeholder="Agent"
                )

            ],

            style={
                "display":"flex",
                "gap":"20px",
                "marginBottom":"20px"
            }
        ),

        html.Div(
            id="agents-kpi"
        ),

        dcc.Graph(
            id="agents-region-graph"
        ),

        dcc.Graph(
            id="agents-performance-graph"
        )

    ]
)