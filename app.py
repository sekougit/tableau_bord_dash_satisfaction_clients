from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.FLATLY
    ]
)

server = app.server

app.layout = html.Div([

    dcc.Location(id="url"),

    dash.page_container

])

if __name__ == "__main__":
    app.run(debug=True)
