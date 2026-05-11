import dash

from dash import (
    Dash,
    html,
    dcc
)

import dash_bootstrap_components as dbc

from components.sidebar import sidebar

import callbacks.refresh_callbacks


# =========================================================
# APP
# =========================================================

app = Dash(

    __name__,

    use_pages=True,

    suppress_callback_exceptions=True,

    external_stylesheets=[
        dbc.themes.FLATLY
    ]
)

server = app.server


# =========================================================
# IMPORT CALLBACKS
# =========================================================

import callbacks.agents_callbacks
import callbacks.clients_callbacks


# =========================================================
# LAYOUT
# =========================================================

app.layout = html.Div(

    [
        dcc.Interval(
    id="auto-refresh",
    interval=300000,  # 5 minutes
    n_intervals=0
),
        dcc.Location(id="url"),

        sidebar,

        html.Div(

            dash.page_container,

            style={
                "marginLeft":"270px",
                "padding":"20px"
            }
        ),
        html.Div(
    id="refresh-output",
    style={"display":"none"}
)

    ]
)


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )