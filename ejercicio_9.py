# Nicolás Vlaeminch Div K | Ejercicio 1 - 9

#Ejercicio 9: Dadas las siguientes listas: edades = [25,36,18,23,45] nombre = ["Juan","Ana","Sol","Mario","Sonia"] y considerando que la posición en la lista corresponde a la misma persona, 
#mostar el nombre de la persona más joven

edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
bandera_mas_joven = True

for i in edades:
    if bandera_mas_joven or i < numero_menor:
        numero_menor = i #hallamos el menor numero de la lista
        posicion_persona_mas_joven = edades.index(numero_menor) #Con la funcion index hallamos la posicion de la persona mas joven
        nombre_persona_mas_joven = nombre[posicion_persona_mas_joven]
        bandera_mas_joven = False
        
print("La persona más joven es:", nombre_persona_mas_joven)