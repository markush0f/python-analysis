import pandas as pd
import matplotlib.pyplot as plt

continents = [
    "Asia",
    "South America",
    "Africa",
    "North America",
    "Europe",
    "Oceana",
    "Oceania",
]

for continent in continents:
    path_continent = f"World-population-growth-rate-by-cities-2024/continents/{continent}/{continent}-population-growth-rate-by-cities-2023-sorted.csv"
    print(path_continent)
    df = pd.read_csv(path_continent)
    plt.figure(figsize=(12, 8))
    plt.scatter(df["City"], df["Population (2023)"], color="red", alpha=0.5)
    plt.xlabel("City")
    plt.ylabel("Population (2023)")     
    plt.title(f"Population of {continent } Cities (2023)")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
# print(df.head())
