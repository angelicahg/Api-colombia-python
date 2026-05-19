import json
import requests

response = requests.get("https://api-colombia.com/api/v1/TouristicAttraction")

touristic_attractions = json.loads(response.content) 

for atraction in touristic_attractions:
    print("*"*20)
    print(atraction["name"])
    print(atraction["city"]["name"])