def filter_region(df, regions):

    if regions:
        df = df[
            df["region"].isin(regions)
        ]

    return df
