#Modulo con función que determina el casillero a ocupar en el juego
#si llegase a estar ya ocupado uno realia la accion correspondiente
#para escoger un nuevo casillero.

#protocolos de funciones
from movimientoComputador import movimiento_computador
from movimientoUsuario import movimiento_usuario

def ingresa_casillero(gato_tablero, tiro_participante, casillero):

    if (casillero == 1):
        if gato_tablero [0][0] == 'X' or gato_tablero [0][0] == 'O':

            if tiro_participante == 'X':

                casillero = movimiento_computador() 
                return ingresa_casillero(gato_tablero, tiro_participante, casillero)
            
            else:

                print('Casilla ya ocupada, ingrese otra casilla a ocupar:')
                casillero_gato = movimiento_usuario()
                ingresa_casillero(gato_tablero, tiro_participante, casillero_gato)           
            
        else:

            gato_tablero [0][0] = tiro_participante
            

    if (casillero == 2):

        if gato_tablero [0][1] == 'X' or gato_tablero [0][1] == 'O':

            if tiro_participante == 'X':
                casillero = movimiento_computador() 
                return ingresa_casillero(gato_tablero, tiro_participante, casillero)
            else:
                print('Casilla ya ocupada, ingrese otra casilla a ocupar:')
                casillero_gato = movimiento_usuario()
                ingresa_casillero(gato_tablero, tiro_participante, casillero_gato)

        else:

            gato_tablero [0][1] = tiro_participante    
        
    if (casillero == 3):

        if gato_tablero [0][2] == 'X' or gato_tablero [0][2] == 'O':

            if tiro_participante == 'X':
                casillero = movimiento_computador() 
                return ingresa_casillero(gato_tablero, tiro_participante, casillero)
            else:
                print('Casilla ya ocupado, ingrese otra casilla a ocupar:')
                casillero_gato = movimiento_usuario()
                ingresa_casillero(gato_tablero, tiro_participante, casillero_gato)
            
        else:

            gato_tablero [0][2] = tiro_participante

    if (casillero == 4):

        if gato_tablero [1][0] == 'X' or gato_tablero [1][0] == 'O':

            if tiro_participante == 'X':

                casillero = movimiento_computador() 
                return ingresa_casillero(gato_tablero, tiro_participante, casillero)
            
            else:

                print('Casilla ya ocupado, ingrese otra casilla a ocupar:')
                casillero_gato = movimiento_usuario()
                ingresa_casillero(gato_tablero, tiro_participante, casillero_gato)
            
        else:

            gato_tablero [1][0] = tiro_participante
            
    if (casillero == 5):

        if gato_tablero [1][1] == 'X' or gato_tablero [1][1] == 'O':

            if tiro_participante == 'X':

                casillero = movimiento_computador() 
                return ingresa_casillero(gato_tablero, tiro_participante, casillero)
            else:

                print('Casilla ya ocupada, ingrese otra casilla a ocupar:')
                casillero_gato = movimiento_usuario()
                ingresa_casillero(gato_tablero, tiro_participante, casillero_gato)
            
        else:
            
            gato_tablero [1][1] = tiro_participante
            
    if (casillero == 6):

        if gato_tablero [1][2] == 'X' or gato_tablero [1][2] == 'O':

            if tiro_participante == 'X':

                casillero = movimiento_computador() 
                return ingresa_casillero(gato_tablero, tiro_participante, casillero)
            
            else:
                
                print('Casilla ya ocupada, ingrese otra casilla a ocupar:')
                casillero_gato = movimiento_usuario()
                ingresa_casillero(gato_tablero, tiro_participante, casillero_gato)

        else:

            gato_tablero [1][2] = tiro_participante  
            
    if (casillero == 7):

        if gato_tablero [2][0] == 'X' or gato_tablero [2][0] == 'O':

            if tiro_participante == 'X':

                casillero = movimiento_computador() 
                return ingresa_casillero(gato_tablero, tiro_participante, casillero)
            
            else:
                
                print('Casilla ya ocupada, ingrese otra casilla a ocupar:')
                casillero_gato = movimiento_usuario()
                ingresa_casillero(gato_tablero, tiro_participante, casillero_gato)

        else:

            gato_tablero [2][0] = tiro_participante
            
    if (casillero == 8):

        if gato_tablero [2][1] == 'X' or gato_tablero [2][1] == 'O':

            if tiro_participante == 'X':

                casillero = movimiento_computador() 
                return ingresa_casillero(gato_tablero, tiro_participante, casillero)
            
            else:

                print('Casilla ya ocupada, ingrese otra casilla a ocupar:')
                casillero_gato = movimiento_usuario()
                ingresa_casillero(gato_tablero, tiro_participante, casillero_gato)

        else:

            gato_tablero [2][1] = tiro_participante
            
    if (casillero == 9):

        if gato_tablero [2][2] == 'X' or gato_tablero [2][2] == 'O':

            if tiro_participante == 'X':

                casillero = movimiento_computador() 
                return ingresa_casillero(gato_tablero, tiro_participante, casillero)
            
            else:
                
                print('Casilla ya ocupada, ingrese otra casilla a ocupar:')
                casillero_gato = movimiento_usuario()
                ingresa_casillero(gato_tablero, tiro_participante, casillero_gato)
            
        else:

            gato_tablero [2][2] = tiro_participante
       
    #print(gato_tablero)
    return gato_tablero

#if __name__ == '__main__':

    #gato_tablero = ([1,2,3], [4,5,6], ['X',8,9])
    #tiro_participante = 'O'
    #casillero = int(input('Ingresa casillero: '))
    #ingresa_casillero(gato_tablero, tiro_participante, casillero)
    #print(gato_tablero)