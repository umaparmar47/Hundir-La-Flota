import random
from funciones import *
def CrearTableroJugador():
    tablero = crearTableroVacio(10,10, "-")
    lancha = "L"
    buque = "B"
    acorazado = "Z"
    portaaviones = "P"
    if nivel == 1:
        barcos = 10
        while barcos != 0:
            fila = random.randint(0,9)
            columna = random.randint(0,9)
            if columna + 5 < 10:
                for i in range(5):
                    tablero[fila][columna] = portaaviones
                    columna+=1
            elif columna + 4 < 10:
                for i in range(4):
                    tablero[fila][columna] = acorazado
                    columna+=1
            elif columna + 3 < 10:
                for i in range(3):
                    tablero[fila][columna] = buque
                    columna+=1
            else:
                    tablero[fila][columna] = lancha
            barcos -= 1
        imprimirTablero(tablero)
