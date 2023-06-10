#Crea una matriz de DE 3X3 y la llena con valores del 1 al 9

import numpy as np #Funcion para manipular matrices

def muestra_tablero(tablero_gato):
    columnas = 3
    filas = 3
    

    #Se crea la matriz para el gato
    tablero_gato = [[ 0 for i in range(columnas)] for j in range(filas) ]

    #print('Matriz del gato creada.')
    #print(np.array(tablero_gato))

    #Se llena con valores del 1 al 9 para el gato
    k = 1
    for  i in range (columnas):
        for j in range (filas):
            tablero_gato [i][j]= k
            k += 1
    
    return tablero_gato


#if __name__ == '__main__':

    #tablero = []
    #gato = muestra_tablero(tablero)
    #print(gato)
