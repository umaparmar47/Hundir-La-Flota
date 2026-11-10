#Archivo de funciones 
#Autores: Marcos Cobarro Torres, Umang Sanjaykumar Parmar y Álvaro Barceló López
#Grupo: 1ºDAW
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