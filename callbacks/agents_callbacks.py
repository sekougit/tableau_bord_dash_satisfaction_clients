from dash import (
    Input,
    Output,
    callback,
    html
)

from utils.data_loader import load_data

from utils.filters import filter_dataframe

from utils.kpi import (
    satisfaction_moyenne,
    nombre_agents
)

from utils.graphs import (
    graph_region,
    graph_agent
)

from components.kpi_card import create_kpi_card


# =========================================================
# SAVE FILTERS
# =========================================================

@callback(

    Output(
        "agents-filters-store",
        "data"
    ),

    Input(
        "agent-region-filter",
        "value"
    ),

    Input(
        "agent-filter",
        "value"
    )

)

def save_agents_filters(
    regions,
    agents
):

    return {

        "regions": regions,

        "agents": agents
    }


# =========================================================
# RESTORE FILTERS
# =========================================================

@callback(

    Output(
        "agent-region-filter",
        "value"
    ),

    Output(
        "agent-filter",
        "value"
    ),

    Input(
        "agents-filters-store",
        "data"
    )

)

def restore_agents_filters(data):

    if not data:

        return [], []

    return (

        data.get("regions", []),

        data.get("agents", [])
    )


# =========================================================
# UPDATE DASHBOARD
# =========================================================

@callback(

    Output(
        "agents-kpi",
        "children"
    ),

    Output(
        "agents-region-graph",
        "figure"
    ),

    Output(
        "agents-performance-graph",
        "figure"
    ),

    Input(
        "agent-region-filter",
        "value"
    ),

    Input(
        "agent-filter",
        "value"
    )

)

def update_agents_dashboard(
    regions,
    agents
):

    df = load_data()

    df = filter_dataframe(
        df,
        regions=regions,
        agents=agents
    )

    kpis = html.Div(

        [

            create_kpi_card(
                "Satisfaction Moyenne",
                satisfaction_moyenne(df)
            ),

            create_kpi_card(
                "Nombre Agents",
                nombre_agents(df)
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

        graph_agent(df)
    )