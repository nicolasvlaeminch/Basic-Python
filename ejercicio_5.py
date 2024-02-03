# Nicolás Vlaeminch Div K | Ejercicio 1 - 5

estacion = input("Ingrese una estación: ")
while estacion != "Invierno" and estacion != "Otoño" and estacion != "Verano" and estacion != "Primavera":
    estacion = input("Error: Ingrese una estación: ")


localidad = input("Ingrese una localidad: ")
while localidad != "Bariloche" and localidad != "Cataratas" and localidad != "Mar del plata" and localidad != "Cordoba":
    localidad = input("Error: Ingrese una localidad: ")
    
precio_base = 15000

precio_final = 0

match estacion:
    case "Invierno":
        if localidad == "Bariloche":
            precio_final = precio_base * 1.20
        elif localidad == "Cataratas":
            precio_final = precio_base * 0.9
        elif localidad == "Cordoba":
            precio_final = precio_base * 0.9
        else:
            precio_final = precio_base * 0.8
    case "Otoño":
        if localidad == "Bariloche":
            precio_final = precio_base * 1.10
        elif localidad == "Cataratas":
            precio_final = precio_base * 1.10
        elif localidad == "Cordoba":
            precio_final = precio_base * 1.10
        else:
            precio_final = precio_base
    case "Verano":
        if localidad == "Bariloche":
            precio_final = precio_base * 0.8
        elif localidad == "Cataratas":
            precio_final = precio_base * 1.10
        elif localidad == "Cordoba":
            precio_final = precio_base * 1.10
        else:
            precio_final = precio_base * 1.20
    case "Primavera":
        if localidad == "Bariloche":
            precio_final = precio_base * 1.10
        elif localidad == "Cataratas":
            precio_final = precio_base * 1.10
        elif localidad == "Cordoba":
            precio_final = precio_base * 1.10
        else:
            precio_final = precio_base


                
print(f"El precio final es: {precio_final}")