# Nicolás Vlaeminch Div K | Ejercicio 1 - 10

i = 0
list_nombre = []
list_sexo = []
list_nota = []
acumulador_notas_mujeres = 0
contador_mujeres = 0
bandera_nota_baja = True

while i < 5:

    nombre = input('Ingrese un nombre: ')
    list_nombre.append(nombre) 

    nota = int(input('Ingrese una nota entre 0-10: '))

    while nota < 0 or nota > 10:
        nota = int(input('ERROR, ingrese una nota valida entre 0-10: '))

    list_nota.append(nota)

    sexo = input('Ingrese su genero (f/m): ')

    while sexo !=  'f' and sexo != 'm':
        sexo = input('ERROR, ingrese un genero valido (f/m): ')

    list_sexo.append(sexo)

    if sexo == 'm':
        if bandera_nota_baja == True or nota < nota_mas_baja:
            nombre_nota_mas_baja = nombre
            nota_mas_baja = nota
            bandera_nota_baja = False
    else:
        contador_mujeres += 1
        acumulador_notas_mujeres +=nota


    i += 1

promedio_notas_mujeres = acumulador_notas_mujeres/contador_mujeres

print('lista de nombres: ', list_nombre)
print('lista de sexos: ', list_sexo)
print('lista de notas: ', list_nota)
print('Nombre del hombre con la nota mas baja: ', nombre_nota_mas_baja)
print('el promedio de las notas de las mujeres es: ', promedio_notas_mujeres)