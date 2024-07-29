import os

continents = [
    "Asia",
    "South America",
    "Africa",
    "North America",
    "Europe",
    "Oceana",
    "Oceania",
]
base_path = "World-population-growth-rate-by-cities-2024/continents"

for continent in continents:
    continent_path = os.path.join(base_path, continent)
    os.makedirs(continent_path, exist_ok=True)
    print(f"Carpeta creada en: {continent_path}")

for continent in continents:
    continent_path = os.path.join(base_path, continent)
    os.makedirs(continent_path, exist_ok=True)
    print(f"Carpeta creada en: {continent_path}")