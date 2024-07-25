def create_csv_continents(df_continents, name_file):
    for continent in df_continents:
        df_continents[continent].to_csv(
            f"continents/{continent}/{continent}-{name_file}.csv", index=False
        )