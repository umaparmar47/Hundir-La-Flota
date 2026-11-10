#Archivo principal del juego
#Autores: Marcos Cobarro Torres, Umang Sanjaykumar Parmar y Álvaro Barceló López
#Grupo: 1ºDAW
from funciones import *


print("###############################")
print("--------HUNDIR LA FLOTA--------")
print("###############################")
while True:
    try:
        comprobarcoordenadas = False
        opcion = int(input("Por favor, selecciona el nivel de dificultad: "))
        if opcion == 1:
            print("########## TU TABLERO ##########")
            tablero = crearTableroVacio(10,10,"-")
            imprimirTablero(tablero)
            pedirCoordenadas1 = (input("Introduce la fila (A - J): "))
            pedirCoordenadas2 = int(input("Introduce la columna (0 - 9): "))
            if pedirCoordenadas1 and pedirCoordenadas2 != coordenadasOrdenador:
                comprobarcoordenadas = False
                print("¡AGUA! Has fallado", comprobarcoordenadas)
            else:
                comprobarcoordenadas = True
                print("¡¡¡TOCADO!!!", comprobarcoordenadas)
        elif opcion == 2:
            print("########## TU TABLERO ##########")
            tablero = crearTableroVacio(10,10,"-")
            imprimirTablero(tablero)
            pedirCoordenadas1 = (input("Introduce la fila (A - J): "))
            pedirCoordenadas2 = int(input("Introduce la columna (0 - 9): "))
            if pedirCoordenadas1 and pedirCoordenadas2 != coordenadasOrdenador:
                comprobarcoordenadas = False
                print("¡AGUA! Has fallado", comprobarcoordenadas)
            else:
                comprobarcoordenadas = True
                print("¡¡¡TOCADO!!!", comprobarcoordenadas)
        else:
            print("########## TU TABLERO ##########")
            tablero = crearTableroVacio(10,10,"-")
            imprimirTablero(tablero)
            pedirCoordenadas1 = (input("Introduce la fila (A - J): "))
            pedirCoordenadas2 = int(input("Introduce la columna (0 - 9): "))
            if pedirCoordenadas1 and pedirCoordenadas2 != coordenadasOrdenador:
                comprobarcoordenadas = False
                print("¡AGUA! Has fallado", comprobarcoordenadas)
            else:
                comprobarcoordenadas = True
                print("¡¡¡TOCADO!!!", comprobarcoordenadas)

    except Exception as errorNumero:
        print("Por favor introduce un número válido: 1, 2 ó 3")

