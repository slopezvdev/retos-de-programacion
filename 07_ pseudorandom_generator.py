'''
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
'''

# Definimos la funcion
def pseudorandom_generator():
    # solicitamos un numero semilla
    num = int(input("Introduce un numero: "))

    # conseguimos un numero pseudoaleatorio
    for _ in range(100):
        if num < 0:
            num = num ** num
        elif num > 100:
            num = num / 101
        else:
            num = num * num
    while num > 100:
        num = num / 101

    # imprimimos el numero
    print("Tu numero pseudoaleatorio es: ", int(num))

# Llamamos a la funcion
pseudorandom_generator()