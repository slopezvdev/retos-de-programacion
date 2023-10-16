'''
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos. 
'''

# Definimos la funcion
def tennis_match():

    # Establecemos las variables y el diccionario de la puntuacion
    counter1 = 0
    counter2 = 0
    deuce = False
    points_table = {0:"Love", 1:"15", 2:"30", 3:"40", 4:"Ventaja"}

    print("Comienza el partido")
    
    # Creamos todo el sistema de peticion de datos, funcionara mientras ninguno de los dos jugadores lleguen a sumar 5 puntos, ya que en ese momento ganaria
    # ese jugador. Si la puntuacion de ambos jugadores es 3, no imprimira el contador ya que en su lugar imprimira "Deuce". Cuando imprime "Deuce" tambien
    # seteamos en True un booleano, para luego poder gestionar las ventajas, ya que solo hay ventaja si antes ha habido "Deuce"
    while counter1 < 5 and counter2 < 5:
        if counter1 != 3 or counter2 != 3:
            print(points_table[counter1], " - ", points_table[counter2])
        else:
            print("Deuce")
            deuce = True
        
        # Condicionamos la entrada a 1, P1, 2 o P2, sin importar mayusculas o minusculas, repitiendo la pregunta despues de mostrar un print de error
        # en caso de que la respuesta no sea valida. Si la respuesta es valida rompemos el while(True)
        while (True):
            point = input("Que jugador a puntuado?: ")
            if point == "1" or point.upper == "P1":
                counter1 += 1
                break
            elif point == "2" or point.upper == "P2":
                counter2 += 1
                break
            else:
                print("Entrada no valida")
            
        # Si no ha habido empate, no hay ventaja, por lo que si un jugador marca 4 veces, habra ganado. Le sumamos un punto para que al tener 5 el programa
        # lo de por ganador
        if deuce == False:
            if counter1 == 4:
                counter1 += 1
                break
            elif counter2 == 4:
                counter2 += 1
                break
            else:
                print("Ups, algo ha fallado :(")
                return 1

        # Si los jugadores empatan a 4, significa que un jugador a obtenido ventaja, y despues ha puntuado el otro jugador, por lo que el primero pierde la
        # ventaja, y vuelven a la posicion de "Deuce". Para ello se le quita un punto a cada jugador
        if counter1 == 4 and counter2 == 4:
            counter1 -= 1
            counter2 -= 1
            
    # Si un jugador llega a 5, ha ganado el juego, imprimimos el ganador
    if counter1 == 5:
        print("P1 ha ganado el juego")
    elif counter2 == 5:
        print("P2 ha ganado el juego")
    else:
        print("Ups, algo a fallado :(")
        return 1

# Llamamos a la funcion
tennis_match()