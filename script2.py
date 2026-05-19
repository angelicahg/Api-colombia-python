import requests

response = requests.get("https://api-colombia.com/api/v1/Department")


#Mostrar departamentos y capitales

departments = response.json()

for department in departments:
    print("-" * 30)
    print("Departamento:", department["name"])
    print("Capital:", department["cityCapital"])