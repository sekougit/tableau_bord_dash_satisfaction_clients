def filter_dataframe(
    df,
    regions=None,
    sexes=None,
    agents=None
):

    if regions is not None and len(regions) > 0:

        df = df[
            df["region"].isin(regions)
        ]

    if sexes is not None and len(sexes) > 0:

        df = df[
            df["sexe"].isin(sexes)
        ]

    if agents is not None and len(agents) > 0:

        df = df[
            df["agent_appel"].isin(agents)
        ]

    return df