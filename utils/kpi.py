def nombre_clients(df):

    return df.shape[0]


def satisfaction_moyenne(df):

    if df.shape[0] == 0:
        return 0

    return round(
        df["note_globale"].mean(),
        2
    )


def nombre_agents(df):

    return df["agent_appel"].nunique()


def satisfaction_positive(df):

    total = df.shape[0]

    if total == 0:
        return 0

    positif = df[
        df["note_globale"] >= 8
    ].shape[0]

    return round(
        (positif / total) * 100,
        2
    )