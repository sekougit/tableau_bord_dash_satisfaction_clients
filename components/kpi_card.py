from dash import html


def create_kpi_card(
    title,
    value
):

    return html.Div(

        [

            html.H4(title),

            html.H2(value)

        ],

        style={

            "background":"white",

            "padding":"20px",

            "borderRadius":"12px",

            "boxShadow":"0 2px 10px rgba(0,0,0,0.1)",

            "width":"250px"
        }
    )