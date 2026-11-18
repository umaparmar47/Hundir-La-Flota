def RealizarDisparo(tableroObjetivo,tablero,fila,columna):
    CompruebaCordenadas(tablero,fila,columna) #Llamamos a la funcion CompruebaCordenadas y le pasamos los parametros para ver si la coordenada está o no
    if tablero[fila][columna] == "-": #<---Si es "-"(esta vacio), es agua
        print("¡AGUA! has fallado")
        tablero[fila][columna]= "A" #Si es agua pintamos la coordenada como A
        return False
    else: #<---Si no es "-", no será agua; Por lo tanto le hemos dado a algo
        print("¡¡¡TOCADO!!!")
        tablero[fila][columna]= "X" #Si no es agua pintamos la coordenada como X
        return True

def QuedanBarcos(tablero):
    contador=0
    barcos=["L", "B", "Z", "P"] #Lista de los distintos barcos posibles
    for fila in range(len(tablero)):
        for col in range(len(tablero[fila])):
            if tablero[fila][col] in(barcos): #Si el valor de la casilla coincide con alguno de los de la lista, suma 1
                contador+=1
        if contador == 0: #Si el contador está a 0, significa que no se ha encon trado ningún barco en el tablero
            return False
        else: #Si el valor del contador no es 0, habra encontrado algún barco
            return True