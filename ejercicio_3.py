# Nicolás Vlaeminch Div K | Ejercicio 1 - 3

numeros = []
pares = 0
impares = 0
suma_positivos = 0
bandera_menor = True
bandera_mayor = True
suma_positivos = 0
producto_negativos = 1

for i in range(0, 5):
    numeros.append(int(input("Ingrese un numero: ")))

for i in numeros:
    if i % 2 == 0:
        pares += 1
        if bandera_mayor or numero_mayor < i:
            numero_mayor = i
            bandera_mayor = False
    else:
        impares += 1

    if bandera_menor or numero_menor > i:
        numero_menor = i
        bandera_menor = False

    if i > 0:
        suma_positivos += i
    else:
        producto_negativos *= i

if producto_negativos == 1:
        producto_negativos = 0

print(f"La cantidad de numeros pares es: {pares} y de impares es {impares}.")
print(f"El menor numero ingresado es {numero_menor}.")
print(f"El mayor de los numero pares ingresado es {numero_mayor}.")
print(f"La suma de los positivos ingresados es {suma_positivos}.")
print(f"El producto de los negativos ingresados es {producto_negativos}.")