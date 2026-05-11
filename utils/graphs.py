import plotly.express as px


def graph_region(df):

    data = (
        df.groupby("region")["note_globale"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        data,
        x="region",
        y="note_globale",
        title="Satisfaction par région"
    )

    return fig


def graph_agent(df):

    data = (
        df.groupby("agent_appel")["note_globale"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        data,
        x="agent_appel",
        y="note_globale",
        title="Performance des agents"
    )

    return fig


def graph_service(df):

    fig = px.pie(
        df,
        names="service_principal",
        title="Répartition des services"
    )

    return fig


def graph_sexe(df):

    fig = px.pie(
        df,
        names="sexe",
        title="Répartition par sexe"
    )

    return fig