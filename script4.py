import requests

response = requests.get("https://api-colombia.com/api/v1/TouristicAttraction")

touristic_attractions = response.json()
#Mostrar atracciones turísticas


for attraction in touristic_attractions:
    print("*" * 30)
    print("Nombre:", attraction["name"])
    print("Descripción:", attraction["description"])
    print("Ciudad:", attraction["city"]["name"])