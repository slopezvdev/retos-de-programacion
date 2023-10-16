'''
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
'''

# Definimos la funcion
def password_generator():
    # Importamos random para elegir los caracteres aleatoriamente
    import random

    # Creamos los diccionarios de los diferentes parametros asociados a numeros, y una lista donde pondremos en forma de numero los parametrosa utilizar
    dict_minus = {i: chr(97 + i) for i in range(26)}
    dict_mayus = {i: chr(65 + i) for i in range(26)}
    dict_symbols = {0: ' ', 1: '!', 2: '"', 3: '#', 4: '$', 5: '%', 6: '&', 7: "'", 8: '(', 9: ')',
                    10: '*', 11: '+', 12: ',', 13: '-', 14: '.', 15: '/', 16: ':', 17: ';', 18: '<', 19: '=',
                    20: '>', 21: '?', 22: '@', 23: '[', 24: '\\', 25: ']', 26: '^', 27: '_', 28: '`', 29: '{',
                    30: '|', 31: '}', 32: '~'}
    parameters = [0]

    # Creamos los parametros variables
    password = ""
    length = 0

    # Creamos las peticiones de los parametros
    while (1):
        i = input("Quieres que la contraseña sea larga?: (s/n)")
        if i.lower() == "s":
            length = 16
            break
        elif i.lower() == "n":
            length = 8
            break
        else:
            print("Entrada no valida")
    while (1):
        i = input("Quieres que la contraseña contenga mayusculas?: (s/n)")
        if i.lower() == "s":
            parameters.append(1)
            break
        elif i.lower() == "n":
            break
        else:
            print("Entrada no valida")
    while (1):
        i = input("Quieres que la contraseña contenga numeros?: (s/n)")
        if i.lower() == "s":
            parameters.append(2)
            break
        elif i.lower() == "n":
            break
        else:
            print("Entrada no valida")
    while (1):
        i = input("Quieres que la contraseña contenga simbolos?: (s/n)")
        if i.lower() == "s":
            parameters.append(3)
            break
        elif i.lower() == "n":
            break
        else:
            print("Entrada no valida")
    
    # Construimos la contraseña con randoms, rangos y los diccionarios, y la imprimimos
    while length > 0:
        j = random.choice(parameters)
        if j == 0:
            password += dict_minus[random.choice(range(26))]
        elif j == 1:
            password += dict_mayus[random.choice(range(26))]
        elif j == 2:
            password += str(random.randint(0, 9))
        elif j == 3:
            password += dict_symbols[random.choice(range(26))]
        else:
            print("Ups, ha habido un error :(")
            return 1
        length -= 1
    print("Contraseña: ", password)

# Llamamos a la funcion
password_generator()