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
    letras_fila = {"A":0, "B":1, "C":2, "D":3,"E":4,"F":5, "G":6, "H":7, "I":8, "J":9,}

    #Comprobamos si la letra introducida es válida
    if fila_letra.upper() not in letras_fila:
        return False # --> si el usuario introduce un numero fuera de A-J no le devolvemos nada
    
    #creamos estas siguientes varibales para que no tengamos que escribir "letras_fila[fila.upper()]" todo el rato
    f = letras_fila[fila.upper()]
    c = columna_num

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

    
