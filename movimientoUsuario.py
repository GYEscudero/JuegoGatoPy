#Modulo que contiene la función que ayuda a 
#seleccionar una casilla pra el usuario

def movimiento_usuario():
    
    try:
        casilla = int(input('Selecciona una casilla: '))

    except ValueError:

        print('Casilla no admitida...')
        return movimiento_usuario()
    
    if casilla > 0 and casilla < 10:
        return casilla
    else:
        print('Casillero erroneo.')
        return movimiento_usuario()

if __name__ == '__main__':

    #mov_usu = movimiento_usuario()
    #print(mov_usu)
    movimiento_usuario()

