import requests

response = requests.get("https://api-colombia.com/api/v1/Region")

#Mostrar regiones y descripción
regions = response.json()

for region in regions:
    print("-" * 30)
    print("Región:", region["name"])
    print("Descripción:", region["description"])