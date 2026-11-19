#Archivo de funciones 
#Autores: Marcos Cobarro Torres, Umang Sanjaykumar Parmar y Álvaro Barceló López
#Grupo: 1ºDAW
import random

def crearTableroVacio(totalFilas, totalCol, valor):
    matriz = []#list()
    for fila in range(totalFilas):
        matriz.append([])
        for col in range(totalCol):
            matriz[fila].append(valor)
    return matriz
def imprimirTablero(tablero):
    for fila in tablero:
        for celda in fila:
            print(celda, end= " | ")#reemplazo el salto de linea por|
            #print(celda)#salto de linea al final
        print()#Salto linea al final de fila
        
#UMANG
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



def CompruebaCoordenadas(tablero, fila, columna): #Comprueba el tablero, la fila (Letra), la columna (número).
    #Comprobamos si está dentro de los límites del array y si no se ha disparado antes.
    #Devolvera True si es válida o False en caso contrario
    
    #Creamos un diccionario con letras para las filas y numeros para indentificar la posicion de cada letras (0 a 9)
    letras_fila = {"A":0, "B":1, "C":2, "D":3,"E":4,"F":5, "G":6, "H":7, "I":8, "J":9}

    if isinstance(fila, int):
        inversor_letra = {0: "A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G" , 7:"HH" , 8:"I" , 9:"J"}
        fila = inversor_letra[fila]
    #Comprobamos si la letra introducida es válida
    if fila.upper() not in letras_fila:
        return False # --> si el usuario introduce un numero fuera de A-J no le devolvemos nada
    
    #creamos estas siguientes varibales para que no tengamos que escribir "letras_fila[fila.upper()]" todo el rato
    f = letras_fila[fila.upper()]
    c = columna

    #Primero de todo comprobamos si el tablero esta dentro de Array [10x10]
    #len(tablero) --> nos dara las filas y len(tablero[0]) --> las columnas
    if f < 0 or f >= len(tablero) or c < 0 or c >= len(tablero[0]): #Asi si el usuario introduce valores fuera de limite del tablero le devolveremos FALSE
        return False

    #Comprobamos lo que hay en esa celda especifica, para no volver a disparar en el mismo lugar 2 veces
    # Por ejemplo si hay una "X" (ya tocado) o "A" (Agua), significa que ya se había disparado ahi antes
    if tablero[f][c] == "X" or tablero[f][c] == "A":
         return False

        
    # Si pasa todas las comprobaciones e la posición de array es libre y valida entonces:
    return True


#COBARRO
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

def CrearTableroOrdenador(nivel):
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

def PideCoordenadas(tablero):
    
    validez_coordenada = False
    while not validez_coordenada:
        fila_validez = False
        columna_validez = False
        while not fila_validez:
            fila = input("Introduce una fila: ").upper()
            if fila in "ABCDEFGHIJ":
                fila_validez = True
        while not columna_validez:
            columna = input("Introduce una columna: ")
            if columna.isdigit() == True:
                columna = int(columna)
                if 0 <= columna <= 9:
                    columna_validez = True
        if CompruebaCoordenadas(tablero, fila, columna) == True:
            validez_coordenada = True

    return fila, columna

#ALVARO
def RealizarDisparo(tableroObjetivo, tableroVisible, fila, columna):
    CompruebaCoordenadas(tableroObjetivo,fila,columna) #Llamamos a la funcion CompruebaCordenadas y le pasamos los parametros para ver si la coordenada está o no
    if isinstance(fila, str):
        letras_fila = {"A":0, "B":1, "C":2, "D":3,"E":4,"F":5, "G":6, "H":7, "I":8, "J":9}
        fila = letras_fila[fila.upper()]
    if tableroObjetivo[fila][columna] == "-": #<---Si es "-"(esta vacio), es agua
        print("¡AGUA! has fallado")
        tableroObjetivo[fila][columna]= "A" #Si es agua pintamos la coordenada como A
        tableroVisible[fila][columna]= "A"
        return False
    else: #<---Si no es "-", no será agua; Por lo tanto le hemos dado a algo
        print("¡¡¡TOCADO!!!")
        tableroObjetivo[fila][columna]= "X" #Si no es agua pintamos la coordenada como X
        tableroVisible[fila][columna]= "X"
        return True

def QuedanBarcos(tablero):
    contador = 0
    barcos = ["L", "B", "Z", "P"] #Lista de los distintos barcos posibles
    for fila in range(len(tablero)):
        for col in range(len(tablero[fila])):
            if tablero[fila][col] in(barcos): #Si el valor de la casilla coincide con alguno de los de la lista, suma 1
                contador+=1
    if contador == 0: #Si el contador está a 0, significa que no se ha encontrado ningún barco en el tablero
        return False
    else: #Si el valor del contador no es 0, habra encontrado algún barco
        return True