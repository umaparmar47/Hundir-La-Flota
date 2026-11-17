import random
from funciones import *
def CrearTableroJugador(nivel):
    tablero = crearTableroVacio(10,10, "-")
    lancha = "L"
    buque = "B"
    acorazado = "Z"
    portaaviones = "P"
    if nivel == 1:
        listaBarcos = [portaaviones, acorazado, buque, buque, buque, lancha, lancha, lancha, lancha, lancha]
        for i in range(len(listaBarcos)):
            tamano = 0
            colocado = False
            while colocado == False:
                fila = random.randint(0,9)
                columna = random.randint(0,9)
                if listaBarcos[i] == portaaviones:
                    tamano = 5
                elif listaBarcos[i] == acorazado:
                    tamano = 4
                elif listaBarcos[i] == buque:
                    tamano = 3
                elif listaBarcos[i] == lancha:
                    tamano = 1

                if columna + tamano <= 10:
                    huecolibre = True
                    for j in range(tamano):
                        if tablero[fila][columna + j] != "-":
                            huecolibre = False
                    if huecolibre:
                        for j in range(tamano):
                            tablero[fila][columna + j] = listaBarcos[i]
                        colocado = True
    if nivel == 2:
        listaBarcos = [portaaviones, acorazado, buque, lancha, lancha]
        for i in range(len(listaBarcos)):
            tamano = 0
            colocado = False
            while colocado == False:
                fila = random.randint(0,9)
                columna = random.randint(0,9)
                if listaBarcos[i] == portaaviones:
                    tamano = 5
                elif listaBarcos[i] == acorazado:
                    tamano = 4
                elif listaBarcos[i] == buque:
                    tamano = 3
                elif listaBarcos[i] == lancha:
                    tamano = 1

                if columna + tamano <= 10:
                    huecolibre = True
                    for j in range(tamano):
                        if tablero[fila][columna + j] != "-":
                            huecolibre = False
                    if huecolibre:
                        for j in range(tamano):
                            tablero[fila][columna + j] = listaBarcos[i]
                        colocado = True
    if nivel == 3:
        listaBarcos = [buque, lancha]
        for i in range(len(listaBarcos)):
            tamano = 0
            colocado = False
            while colocado == False:
                fila = random.randint(0,9)
                columna = random.randint(0,9)
                if listaBarcos[i] == buque:
                    tamano = 3
                elif listaBarcos[i] == lancha:
                    tamano = 1

                if columna + tamano <= 10:
                    huecolibre = True
                    for j in range(tamano):
                        if tablero[fila][columna + j] != "-":
                            huecolibre = False
                    if huecolibre:
                        for j in range(tamano):
                            tablero[fila][columna + j] = listaBarcos[i]
                        colocado = True
    return tablero

