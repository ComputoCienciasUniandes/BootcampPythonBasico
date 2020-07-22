def lee_notas(archivo): 
    """
    Entrada:
    archivo: cadena de caracteres con el nombre del archivo.
             Las notas estan escritas en una columna con una nota por linea.
    Salida:
    notas: lista con floats como elementos. 
           Corresponde a las notas que se encuentran dentro de archivo.
           Si el archivo esta vacio, entonces notas es una lista vacia.
          
    """   
    f = open(archivo, "r")
    lineas = f.readlines()
    f.close()

    notas = []    
    for l in lineas:
        notas.append(float(l))
    return notas

def separa_notas(notas):
    """
    Entrada: 
    notas: lista de floats.

    Salida:
    pasan: lista de floats, solamente incluye los valores dentro de notas 
           que son mayores o iguales a tres.
    pierden: lista de floats, solamente incluye los valores dentro de notas
           que son menores a tres.
    """
    
    pasan = []
    pierden = []
    
    for n in notas:
        if n<3.0:
            pierden.append(n)
        else:
            pasan.append(n)
    return pasan, pierden

def escribe_notas(notas, archivo):
    """
    Entrada:
    notas: lista de floats.
    archivo: cadenda de caracteres que representa el archivo donde se va a escribir,
    Salida:
    La funcion no devuelve nada. 
    Si notas es una lista vacia entonces el archivo se abre y cierra de todas maneras.
    """
    f = open(archivo, "w")    
    try:
        for n in notas:
            f.write("{}\n".format(n))
    except:
        print("La lista esta vacia, nada que escribir")
    f.close()
    return 

notas = lee_notas("notas_completas.txt")
pasa, pierde = separa_notas(notas)
escribe_notas(pasa, "notas_pasan.txt")
escribe_notas(pierde, "notas_pierden.txt")


            

