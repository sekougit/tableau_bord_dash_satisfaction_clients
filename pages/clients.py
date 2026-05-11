from dash import html, dcc
import dash

dash.register_page(__name__)

layout = html.Div([

    dcc.Store(
        id="clients-filters-store",
        storage_type="local"
    ),

    html.H1("Page Clients"),

    dcc.Dropdown(
        id="client-region-filter",
        multi=True
    ),

    dcc.Graph(
        id="clients-graph"
    )

])
