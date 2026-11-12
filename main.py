#Archivo principal del juego
#Autores: Marcos Cobarro Torres, Umang Sanjaykumar Parmar y Álvaro Barceló López
#Grupo: 1ºDAW
from funciones import *
from umang import *

print("********************************************")
print("--------BIENVENIDO A HUNDIR LA FLOTA--------")
print("********************************************")

def menuDificultad(): #Para que pide una opcion válida al usuario y que no pare hasta que el usuario introduzca un numero valido
    while True:
        try:
            opcion = int(input("Por favor, selecciona el nivel de dificultad (1, 2 ó 3): "))
            if opcion in [1,2,3]:
                return opcion
            else:
                print("Por favor, introduce un número válido: 1, 2 ó 3")

        except Exception as errorNumero:
            print("Ups... Debes de introducir un número entero: 1, 2 ó 3")

dificultad_elegida = menuDificultad()
print(dificultad_elegida)

