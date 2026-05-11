from dash import html, dcc
import dash

dash.register_page(__name__)

layout = html.Div([

    dcc.Store(
        id="agents-filters-store",
        storage_type="local"
    ),

    html.H1("Page Agents"),

    dcc.Dropdown(
        id="agent-region-filter",
        multi=True
    ),

    dcc.Graph(
        id="agents-graph"
    )

])
