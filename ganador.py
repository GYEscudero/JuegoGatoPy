#Modulo que ayuda a determinar quien gano el juego

def ganador_juego(tablero):

#Computador-----------------------------------------------------------------------------

    if tablero [0][0] == 'X' and tablero [0][1] == 'X' and tablero [0][2] == 'X':
    
        return 'Ordenador.'
    
    if tablero [1][0] == 'X' and tablero [1][1] == 'X' and tablero [1][2] == 'X':

        return 'Ordenador.'
    
    if tablero [2][0] == 'X' and tablero [2][1] == 'X' and tablero [2][2] == 'X':

        return 'Ordenador.'
    
    if tablero [0][0] == 'X' and tablero [1][0] == 'X' and tablero [2][0] == 'X':

        return 'Ordenador.'
    
    if tablero [0][1] == 'X' and tablero [1][1] == 'X' and tablero [2][1] == 'X':

        return 'Ordenador.'
    
    if tablero [0][2] == 'X' and tablero [1][2] == 'X' and tablero [2][2] == 'X':

        return 'Ordenador.'
    
    if tablero [0][0] == 'X' and tablero [1][1] == 'X' and tablero [2][2] == 'X':

        return 'Ordenador.'
    
    if tablero [0][2] == 'X' and tablero [1][1] == 'X' and tablero [2][0] == 'X':

        return 'Ordenador.'
    
#Usuario-----------------------------------------------------------------------------------

    if tablero [0][0] == 'O' and tablero [0][1] == 'O' and tablero [0][2] == 'O':
    
        return 'Usuario.'
    
    if tablero [1][0] == 'O' and tablero [1][1] == 'O' and tablero [1][2] == 'O':

        return 'Usuario.'
    
    if tablero [2][0] == 'O' and tablero [2][1] == 'O' and tablero [2][2] == 'O':

        return 'Usuario.'
    
    if tablero [0][0] == 'O' and tablero [1][0] == 'O' and tablero [2][0] == 'O':

        return 'Usuario.'
    
    if tablero [0][1] == 'O' and tablero [1][1] == 'O' and tablero [2][1] == 'O':

        return 'Usuario.'
    
    if tablero [0][2] == 'O' and tablero [1][2] == 'O' and tablero [2][2] == 'O':

        return 'Usuario.'
    
    if tablero [0][0] == 'O' and tablero [1][1] == 'O' and tablero [2][2] == 'O':

        return 'Usuario.'
    
    if tablero [0][2] == 'O' and tablero [1][1] == 'O' and tablero [2][0] == 'O':

        return 'Usuario.'
    
    #Empate-----------------------------------------------------------------------------------
    
    else:

        return None
    
#if __name__ == '__main__':

    #tabla = (['X', 'X', 'X'],[4, 5, 6],[7, 8, 9])
    #gano = ganador_juego(tabla)
    #print('El ganador es', gano)
    
