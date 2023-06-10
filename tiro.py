#Modulo que muestra la función para asignarle simbolo
#de tiro al jugador en turno


def tiro_gato(jugador):

    if jugador == 'Computador.':
        tiro = 'X'
        #print('\nX')
        #print(tablero)
        return tiro
    
    else:
        tiro = 'O'
        #print('\nO')
        #print(tablero)
        return tiro
    
#if __name__ == '__main__':

    #jugador = 'Usuario.'
    #simbolo_tiro = tiro_gato(jugador)
    #print(simbolo_tiro)