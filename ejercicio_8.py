# Nicolás Vlaeminch Div K | Ejercicio 1 - 8

lista = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]

numeros_repetidos = []
diccionario = {}

for elemento in lista:
    if elemento in diccionario:
        diccionario[elemento] += 1
    else:
        diccionario[elemento] = 1
        
for elemento, diccionario in diccionario.items():
    if diccionario > 1:
        numeros_repetidos.append(elemento)

print(numeros_repetidos)