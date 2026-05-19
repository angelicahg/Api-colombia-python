import requests

while True:

    print("\n===== API COLOMBIA =====")
    print("1. Información general de Colombia")
    print("2. Departamentos y capitales")
    print("3. Regiones")
    print("4. Atracciones turísticas")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # OPCION 1
    if opcion == "1":

        response = requests.get(
            "https://api-colombia.com/api/v1/Country/Colombia"
        )

        country = response.json()

        print("\n--- INFORMACIÓN GENERAL ---")
        print("Nombre:", country["name"])
        print("Capital:", country["stateCapital"])
        print("Población:", country["population"])
        print("Región:", country["region"])
        print("Moneda:", country["currency"])

    # OPCION 2
    elif opcion == "2":

        response = requests.get(
            "https://api-colombia.com/api/v1/Department"
        )

        departments = response.json()

        print("\n--- DEPARTAMENTOS ---")

        for department in departments:
            print("*" * 30)
            print("Departamento:", department["name"])
            print("Capital:", department["cityCapital"])

    # OPCION 3
    elif opcion == "3":

        response = requests.get(
            "https://api-colombia.com/api/v1/Region"
        )

        regions = response.json()

        print("\n--- REGIONES ---")

        for region in regions:
            print("*" * 30)
            print("Región:", region["name"])
            print("Descripción:", region["description"])

    # OPCION 4
    elif opcion == "4":

        response = requests.get(
            "https://api-colombia.com/api/v1/TouristicAttraction"
        )

        attractions = response.json()

        print("\n--- ATRACCIONES TURÍSTICAS ---")

        for attraction in attractions:
            print("*" * 30)
            print("Nombre:", attraction["name"])
            print("Descripción:", attraction["description"])
            print("Ciudad:", attraction["city"]["name"])

    # OPCION 5
    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida")