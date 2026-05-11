from dash import (
    Input,
    Output,
    callback,
    html
)

from utils.data_loader import load_data

from utils.filters import filter_dataframe

from utils.kpi import (
    nombre_clients,
    satisfaction_moyenne,
    satisfaction_positive
)

from utils.graphs import (
    graph_region,
    graph_service,
    graph_sexe
)

from components.kpi_card import create_kpi_card


# =========================================================
# SAVE FILTERS
# =========================================================

@callback(

    Output(
        "clients-filters-store",
        "data"
    ),

    Input(
        "client-region-filter",
        "value"
    ),

    Input(
        "client-sexe-filter",
        "value"
    )

)

def save_clients_filters(
    regions,
    sexes
):

    return {

        "regions": regions,

        "sexes": sexes
    }


# =========================================================
# RESTORE FILTERS
# =========================================================

@callback(

    Output(
        "client-region-filter",
        "value"
    ),

    Output(
        "client-sexe-filter",
        "value"
    ),

    Input(
        "clients-filters-store",
        "data"
    )

)

def restore_clients_filters(data):

    if not data:

        return [], []

    return (

        data.get("regions", []),

        data.get("sexes", [])
    )


# =========================================================
# UPDATE DASHBOARD
# =========================================================

@callback(

    Output(
        "clients-kpi",
        "children"
    ),

    Output(
        "clients-region-graph",
        "figure"
    ),

    Output(
        "clients-service-graph",
        "figure"
    ),

    Output(
        "clients-sexe-graph",
        "figure"
    ),

    Input(
        "client-region-filter",
        "value"
    ),

    Input(
        "client-sexe-filter",
        "value"
    )

)

def update_clients_dashboard(
    regions,
    sexes
):

    df = load_data()

    df = filter_dataframe(
        df,
        regions=regions,
        sexes=sexes
    )

    kpis = html.Div(

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
                "Satisfaction Positive (%)",
                satisfaction_positive(df)
            )

        ],

        style={
            "display":"flex",
            "gap":"20px",
            "marginBottom":"20px"
        }
    )

    return (

        kpis,

        graph_region(df),

        graph_service(df),

        graph_sexe(df)
    )