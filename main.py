#Archivo principal del juego
#Autores: Marcos Cobarro Torres, Umang Sanjaykumar Parmar y Álvaro Barceló López
#Grupo: 1ºDAW
from funciones import *


print("###############################")
print("--------HUNDIR LA FLOTA--------")
print("###############################")
while True:
    try:
        opcion = int(input("Por favor, selecciona el nivel de dificultad: "))
        if opcion == 1:
            tablero = crearTableroVacio(10,10,"-")
            imprimirTablero(tablero)
        elif opcion == 2:
            tablero = crearTableroVacio(10,10,"-")
            imprimirTablero(tablero)
        else:
            tablero = crearTableroVacio(10,10,"-")
            imprimirTablero(tablero)

    except Exception as errorNumero:
        print("Por favor introduce un número válido: 1, 2 ó 3")

