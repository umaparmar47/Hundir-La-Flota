#Archivo principal del juego
#Autores: Marcos Cobarro Torres, Umang Sanjaykumar Parmar y Álvaro Barceló López
#Grupo: 1ºDAW
print("********************************************")
print("--------BIENVENIDO A HUNDIR LA FLOTA--------")
print("********************************************")
from funciones import *
from umang import *
from cobarro import *


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

print("########## TABLERO DE DISPAROS##########")
imprimirTablero(tablero_Disparo)

#Bucle principal que se repite hasta que ambos tengan barcos 
#while QuedanBarcos(tablero_Jugador) and QuedanBarcos(tablero_Ordenador):

    #Tablero Jugador 