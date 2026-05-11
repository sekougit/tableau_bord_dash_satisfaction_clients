import dash

from dash import (
    Dash,
    html,
    dcc
)

import dash_bootstrap_components as dbc

from components.sidebar import sidebar


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

        dcc.Location(id="url"),

        sidebar,

        html.Div(

            dash.page_container,

            style={
                "marginLeft":"270px",
                "padding":"20px"
            }
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