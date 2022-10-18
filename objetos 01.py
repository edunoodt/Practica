from os import system
import random

system('cls')

class movil():
    def __init__(self,nombre):
        self.nombre = nombre
        self.__posicion = 0

    def avanza(self):
        self.__posicion += random.randint(1,4)

    def __str__(self):
        print (self.nombre,' - posicion: ',str(self.__posicion))


nombre1 = input ('ingrese el nombre del primer movil: ')
nombre2 = input ('ingrese el nombre del segundo movil: ')


movil01 = movil(nombre1)
movil02 = movil(nombre2)

for ciclos in range (10):
    print (movil01.__str__())
    print (movil02.__str__())
    movil01.avanza()
    movil02.avanza()


