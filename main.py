#Archivo principal del juego
#Autores: Marcos Cobarro Torres, Umang Sanjaykumar Parmar y Álvaro Barceló López
#Grupo: 1ºDAW
print("********************************************")
print("--------BIENVENIDO A HUNDIR LA FLOTA--------")
print("********************************************")
from funciones import *
from umang import *


#Pedir dificultad
dificultad = menuDificultad()

#Tableros
tablero_Jugador = CrearTableroJugador()
tablero_Ordenador = CrearTableroOrdenador()
tablero_Disparo = crearTableroVacio()

#Imprimimos los tableros
print("########## TU TABLERO ##########")
Imprime_Tablero(tablero_Jugador)

print("########## TABLERO DE DISPAROS##########")
Imprime_Tablero(tablero_Disparo)

#Bucle principal que se repite hasta que ambos tengan barcos 
while QuedanBarcos(tablero_Jugador) and QuedanBarcos(tablero_Ordenador):

    #Tablero Jugador 