# Nicolás Vlaeminch Div K | Ejercicio 1 - 6

lista = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

mayor = lista[0]

for i in lista:
    if i > mayor:
        mayor = i

print(mayor)