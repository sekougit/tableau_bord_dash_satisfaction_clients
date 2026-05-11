def satisfaction_moyenne(df):

    return round(
        df["satisfaction_globale"].mean(),
        2
    )
