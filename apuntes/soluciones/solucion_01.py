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
