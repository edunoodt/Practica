from os import system       # Se importa sysytem para borrar la pantalla
import random as rn         # Libreria de funciones random    
import statistics as stt    # LIbreria de funciones estadísticas
system ('cls')              # Borrado de pantalla

# Inicialización de dos listas
listaMedia = []
listado =[]


for ciclos in range (50):       # Ciclo mayos para calcular 50 veces el promedio de una lista random de 50 elementos
    for indice in range (20):   # Ciclo menor para generar una lista de 50 numeros random
        x = rn.randint(0,50)    # Se genera un numero random entre 0 y 50
        listado.append(x)       # Se lo almacena en la lista "Listado"

    media=stt.median(listado)   # Calculamos el promedio de la lista "Listado"
    listaMedia.append(media)    # Almacenamos el promedio calculado en "listaMedia"
print(listaMedia)               # Imprimimos la lista de promedios
contador = {}                   # Inicializamos el diccionario "contador"

for puntero in listaMedia:      # ciclamos "listaMedia para introducir los valores en el diccionario"
    if puntero in contador:     # Verificamos si el valor de la lista ya está en el contador
        contador[puntero]+=1    # Si está, incrementamos la cantidad en uno
    else:
        contador[puntero]=1     # Si no está, iniciamos el valor en 1

print(contador)                 # Imprimimos el diccionario con los contadores

mayor = [ valor for valor in listaMedia if valor > 25] # Usando "list comprhension" creamos una lista con los promedios de mas de 25
print (mayor)                   # Imprimimos nueva lista


