#Escriba un programa de python que:

#1. Lea el archivo "texto.txt" usando readlines()

#2. Cuente el número de veces que aparece en el texto cada una de las letras del alfabeto inglés (abcdefghijklmnopqrstuvwxyz). Solamente tenga en cuenta las letras que se encuentran en minúscula en el texto.

#3. Escribe el resutado del conteo en el archivo "conteo.csv". El archivo debe contener dos columnas. La primera es la letra del alfabeto y la segunda es el número de veces que se encuentra esa letra en el texto. Si la letra no se encuentra debe escribir cero (0).

#Solamente son permitidas las operaciones en python que aparezcan en los videos de la playlist del curso. El programa debe funcionar correctamente si el contenido de "texto.txt" cambia (suponiendo siempre que el archivo no está vacío). 

#También puede utilizar que un diccionario vacío se crea como "a={}" y una lista vacía se crea como "b=[]".


# leo el texto
f = open('texto.txt', 'r')
lineas = f.readlines()
f.close()

# una cadena de caracteres con las letras del alfabeto
alfabeto = "abcdefghijklmnopqrstuvwxyz"

# creo un diccionario donde las llaves son las letras del alfabeto
# y los valores son los conteos de las letras

conteo = {}
for letra in alfabeto:
    conteo[letra] = 0

# paso linea por linea del texto
for linea in lineas:
    # luego caracter por caracter en cada linea
    for caracter in linea:
        # y luego recorro el alfabeto
        for letra in alfabeto:
            # y me pregunto si caracter==letra para contarlo
            if caracter==letra:
                conteo[letra] = conteo[letra] + 1

# ahora escribo lo que tengo dentro de conteo
f = open('conteo.csv', 'w')
n_lineas = len(alfabeto)
for k in conteo.keys():
    f.write('{},{}\n'.format(k, conteo[k]))
f.close()
