from os import system

system('cls')


asado = {'raul':'carne','jorge':'pan','daniel':'carbon','fernando':'ensalada','sandra':'postre','marita':'cafe'}

print (asado)

claves = list(asado.keys())
print (claves)
valores = list(asado.values())
print (valores)

for puntero in asado:
    print(puntero,end=', ')
    print(asado[puntero])
