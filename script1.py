import json
import requests

response = requests.get("https://api-colombia.com/api/v1/Country/Colombia")

#Mostrar información general de Colombia
country = response.json()

print("Nombre:", country["name"])
print("Capital:", country["stateCapital"])
print("Población:", country["population"])
print("Región:", country["region"])
print("Moneda:", country["currency"])
