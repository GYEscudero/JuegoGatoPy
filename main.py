###########################################################
###########################################################
##                                                       ## 
##  Autor: Gerson Yaser Escudero Bejarano                ##
##  Fecha: 31 de Mayo de 2023                            ##
##                                                       ## 
##  Programa que simula el Jueggo del gato mediante      ##
##  la creacion de funciones, usando metodos y setencias ##
##  de control en Python (No utiliza ninguna             ##
##  inteligencia artificial)                             ##
##                                                       ##
###########################################################
###########################################################

#protocolos de la funcion creadas
from muestraTablero import muestra_tablero
from escogeVolado import escoge_volado
from volado import volado_lanzado
from tiro import tiro_gato
from movimientoComputador import movimiento_computador
from movimientoUsuario import movimiento_usuario
from ingresaCasillero import ingresa_casillero 
from ganador import ganador_juego

#protocolos de la funcion Python
import numpy as np

#----------------------------------------------------------
#---------Inicio del programa la Funcion principal "main"--
#----------------------------------------------------------
def main():

  #Variables 
  tablero = [] #Lista para crear tablero del gato
  bucle = 1
  contador = 0

  #------- Llamado a la función "muestra_tablero"----------
  # --------------del modulo "muestraTablero" -------------
  #---Funcion que crea las casillas del juego del gato-----
  #----------llenado las casillas del 1 al 9.--------------
  gato_tabla = muestra_tablero(tablero)
  print('Empieza ...\n')
  #print(np.array(gato_tabla)) #Devuelve la impresión del 
                               #tablero del gato

  #------- Llamado a la función "escoge_volado"------------
  #------------del modulo "escogeVolado"------------------- 
  #-----Funcion que da a escoger al usuario que lado-------
  #---de la moneda quiere tomar para realizar el volado----
  cara_escogida = escoge_volado()

  #------- Llamado a la función "volado"-------------------
  #--------------del modulo "volado"----------------------- 
  #---Funcion donde al azar se da un lado de la------------ 
  #--------cara para que empiece el juego------------------
  print('\nEmpezara el Volado...\n')
  participante = volado_lanzado(cara_escogida)
  print('Empieza el', participante, '\n' )

  #------- Llamado a la función "tiro_gato" ---------------
  #---------------del modulo "tiro"------------------------
  #---Función donde se le asigna una "X" para el turno-----
  #---del computador y una "O" para el tiro del humano-----
  jugador_tiro = tiro_gato(participante)  

  while bucle: #Bucle donde se realiza los movimientos del
               #juego

    if jugador_tiro == 'X': #Computador
    
    #-----Llamado a la función "movimiento_computador"-----
    #---------- del modulo "movimientoComputador" --------- 
    #--Aleatoriamente escoge una casilla del 1 al 9--------
      print('\nTurno del Computador.')
      casilla = movimiento_computador()
      
    else: #Usuario

    #-----Llamado a la función "movimiento_usuario"--------
    #----------- del modulo "movimientoUsuario"------------
    #----mediante el teclado se asigna un numero de la-----
    #----------------------casilla-------------------------
      print('\nTurno del usuario.')
      casilla = movimiento_usuario()

    #------- Llamado a la funcion ingresa_casillero--------
    #------------ del modulo "ingresaCasillero" ----------- 
    #-Para el Computador-----------------------------------
    #--Si esta ocupada escoge automticamente otra hasta----
    #----------------encontrar una vacia-------------------
    #-Para el Usuario--------------------------------------
    #------------Si el valor es un caracter,---------------
    #--------esta fuera de rango o ya esta ocupado---------
    #------se pide al usuario que ingrese otro valor-------
    gato_tabloide = ingresa_casillero(gato_tabla,
                                      jugador_tiro,
                                      casilla)
    print()
    print(np.array(gato_tabloide))
    
    if jugador_tiro == 'X': #Si el turno del Computador
                            #termino se cambia a Usuario
      
      jugador_tiro = 'O'
      
    else: #Si el turno del Usuario termino se cambia a 
          #Computador
      jugador_tiro = 'X'
      
    #------- Llamado a la funcion "ganador_juego"--------
    #--------------del modulo "ganador"------------------
    #----Verifica las celdas ocupadas y da un ganador----
    vencedor = ganador_juego(gato_tabloide)

    contador += 1

    if vencedor == None: # Aun no hay un ganador
      bucle = 1
      if contador == 9: #El juego finalizo y hay un 
                        #empate
        print('\nEmpate...')
        bucle = 0
    else: #Existe un ganador
      print('\nEl ganador es "', vencedor, '"...!!!!')
      bucle = 0  
  
if __name__ == '__main__':

  main()

