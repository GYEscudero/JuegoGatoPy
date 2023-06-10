#Modulo con funcion para ingresar que cara de la moneda desea 
#el ususario

def escoge_volado():

    escoger_lado_moneda = input('Escriba "CARA" o "CRUZ" para iniciar el volado: ' )

    resultado = escoger_lado_moneda.upper() 
    #print(resultado)
    if resultado == 'CARA':
        print('\nHas escogido "Cara".')
        return resultado
    elif resultado == 'CRUZ':
        print('\nHas escogido "Cruz".')
        return resultado
    else:
        print('\nOpción incorrecta.\nVuelve a intentarlo...\n')
        return escoge_volado()
    
#if __name__ == '__main__':

    #escoge_volado() 

