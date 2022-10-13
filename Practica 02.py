from os import system
import random as rn
import statistics as stt
system ('cls')
listaMedia = []
listado =[]
for ciclos in range (50):
    for indice in range (20):
        x = rn.randint(0,50)
        listado.append(x)


    media=stt.median(listado)
    listaMedia.append(media)
print(listaMedia)
contador = {}
for puntero in listaMedia:
    if puntero in contador:
        contador[puntero]+=1
    else:
        contador[puntero]=1
print(contador)
mayor = [ valor for valor in listaMedia if valor > 25]
print (mayor)

