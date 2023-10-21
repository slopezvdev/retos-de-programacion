'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

# Definimos la funcion
def fizz_buzz():

    # Establecemos el rango para recorrer los numero dl 1 al 100
    for n in range(1,101):
        # Establecemos las condiciones para imprimir "fizz", "buzz" y "fizzbuzz", y en caso de no tener que imprimir ninguno de ellos imprimimos el numero
        if n%3 == 0:
            if n%5 == 0:
                print("fizzbuzz")
            else:
                print("fizz")
        elif n%5 == 0:
            print("buzz")
        else:
            print(n)

# Llamamos a la funcion
fizz_buzz()