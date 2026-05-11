from dash import (
    callback,
    Input,
    Output,
    html
)

from scripts.ETL_DATA_FINANCE_KOBO import run_etl


@callback(

    Output(
        "refresh-output",
        "children"
    ),

    Input(
        "auto-refresh",
        "n_intervals"
    )

)

def auto_refresh(_):

    run_etl()

    return html.Div()