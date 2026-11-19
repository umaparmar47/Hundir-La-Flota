#Archivo principal del juego
#Autores: Marcos Cobarro Torres, Umang Sanjaykumar Parmar y Álvaro Barceló López
#Grupo: 1ºDAW
print("********************************************")
print("--------BIENVENIDO A HUNDIR LA FLOTA--------")
print("********************************************")
import random
import math
from funciones import *



#Pedir dificultad

dificultad_elegida = menuDificultad()
print("Has elegido la dificultad: ",dificultad_elegida)

#Tableros
tablero_Jugador = CrearTableroJugador(dificultad_elegida)
tablero_Ordenador = CrearTableroOrdenador(dificultad_elegida)
tablero_Disparo = crearTableroVacio(10, 10, "-")

#Imprimimos los tableros
print("########## TU TABLERO ##########")
imprimirTablero(tablero_Jugador)

print("########## TABLERO DE DISPAROS ##########")
imprimirTablero(tablero_Disparo)

#Bucle principal que se repite hasta que ambos tengan barcos 
while QuedanBarcos(tablero_Jugador) and QuedanBarcos(tablero_Ordenador):
    #Tablero Jugador 
    print("===== Tu turno =====")
    #Pedimos las coordenadas al usuario
    fila, columna = PideCoordenadas(tablero_Disparo)
    #Comprobamos el disparo encima del tablero del ordenador, si hay alguna flota o agua (Si hay barco (X) y si no hay nada (A))
    RealizarDisparo(tablero_Ordenador, tablero_Disparo, fila, columna)

    #Imprimimos de nuevo el tablero de disparos
    imprimirTablero(tablero_Disparo)

    #SI tras el disparo al tablero del ordenador no le quedan barcos, terminamos el programa 
    if not QuedanBarcos(tablero_Ordenador):
        break

    #Turno del ordenador 
    print("===== Turno del ordenador =====")
    #Generamos coordenadas aleatorios para el disparo que va a relaizar el ordenador 
    fila_ordenador = random.randint(0,9) #randit devuele un número entero entre 0,9
    columna_ordenador = random.randint(0,9)
    letras_fila = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}

    print(f"El ordenador ha disparado en la posicion: {fila_ordenador}, {columna_ordenador}")

    #Comprobamos el disparo del ordenador sobre el tablero del jugador
    RealizarDisparo(tablero_Jugador,tablero_Jugador,fila_ordenador,columna_ordenador)
    #Imprimimos el tablero con los disparos realizados 
    print("########## TU TABLERO ##########")
    imprimirTablero(tablero_Jugador)

print("#############################")
print("##### FIN DE LA PARTIDA #####")
print("#############################")
if QuedanBarcos(tablero_Jugador):
    print("Felicidades has ganado")
else:
    print("Ohh ferran ohh ferran, has perdido que pena.")