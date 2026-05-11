from dash import (
    html,
    dcc
)


sidebar = html.Div(

    [

        html.H2(
            "Dashboard"
        ),

        html.Hr(),

        dcc.Link(
            "Accueil",
            href="/"
        ),

        html.Br(),
        html.Br(),

        dcc.Link(
            "Agents",
            href="/agents"
        ),

        html.Br(),
        html.Br(),

        dcc.Link(
            "Clients",
            href="/clients"
        ),

    ],

    id="sidebar",

    style={

        "width":"250px",

        "height":"100vh",

        "position":"fixed",

        "background":"#1e293b",

        "padding":"20px",

        "color":"white"
    }
)