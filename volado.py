#Modulo con función que ayuda a escoger quien inicia el volado


import random


def volado_lanzado(cara_escogida):

    cara_moneda = random.randint(0,1)

    if cara_moneda == 0:
        cara_moneda = 'Cara'
    else:
        cara_moneda = 'Cruz'

    print('\nHa salido: ',cara_moneda, '\n')
   
    
    if cara_moneda == cara_escogida:
        return 'Usuario.'
    else:
        return 'Computador.'

#if __name__ == '__main__':

    #quien_empieza = volado_lanzado('Cara')
    #print(quien_empieza)
    