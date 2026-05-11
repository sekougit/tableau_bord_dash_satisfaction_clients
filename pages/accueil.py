from dash import html

import dash

from utils.data_loader import load_data

from utils.kpi import (
    nombre_clients,
    satisfaction_moyenne,
    nombre_agents
)

from components.kpi_card import create_kpi_card


dash.register_page(

    __name__,

    path="/"
)

df = load_data()


layout = html.Div(

    [

        html.H1(
            "Dashboard Satisfaction"
        ),

        html.Br(),

        html.Div(

            [

                create_kpi_card(
                    "Nombre Clients",
                    nombre_clients(df)
                ),

                create_kpi_card(
                    "Satisfaction Moyenne",
                    satisfaction_moyenne(df)
                ),

                create_kpi_card(
                    "Nombre Agents",
                    nombre_agents(df)
                ),

            ],

            style={
                "display":"flex",
                "gap":"20px"
            }
        )
    ]
)