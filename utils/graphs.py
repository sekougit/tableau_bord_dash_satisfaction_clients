import plotly.express as px

def graph_region(df):

    fig = px.bar(
        df,
        x="region",
        y="note_globale"
    )

    return fig
