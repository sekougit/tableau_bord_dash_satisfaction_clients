from dash import html, dcc

sidebar = html.Div([

    html.H2("Dashboard"),

    html.Hr(),

    dcc.Link("Accueil", href="/"),
    html.Br(),

    dcc.Link("Agents", href="/agents"),
    html.Br(),

    dcc.Link("Clients", href="/clients"),

], id="sidebar")
