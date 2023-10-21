'''
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
'''

# Definimos la funcion para detectar si es un heterograma (no tiene ninguna letra repetida)

def heterogram(text):

    # recorremos el texto letra a letra, añadiendolas a una lista, comprobando antes que no esten ya en esta, si esta, es porque esta repetida, entonces
    # devolvemos false, si terminamos de recorrer la palabra es porque ninguna letra estaba repetida, y devlvemos true

    used_letters = []
    for letter in text:
        if letter in used_letters:
            return False
        else:
            used_letters.append(letter)
    return True


# Definimos la funcion para detectar si es un isograma (todas las letras estan el mismo numero de veces)

def isogram(text):

    # creamos el abecedario para hacer un diccionario, donde las letras sean la clave y todas tengan valor 0, despues recorremos el texto, sumamos uno al valor
    # de la letra y añadimos la letra a una lista de letras usadas si es que no estaba ya

    abc = "abcdefghijklmnñopqrstuvwxyz"
    used_letters = []
    num_used_letters = {letter: 0 for letter in abc}
    for letter in text:
        num_used_letters[letter] += 1
        if letter not in used_letters:
            used_letters.append(letter)

    # definimos una variable que sea igual a el numero de veces que aparece la primera letra de la lista donde hemos ido poniendo las letras que recorriamos
    # recorremos esa lista, comprobando que los valores de esas letras en el diccionario sea igual que la variable que hemos definido, devolviendo false
    # si en algun caso no es igual, y true si termina el for exitosamente

    num_times_used = num_used_letters[used_letters[0]]
    for letter in used_letters:
        if num_used_letters[letter] != num_times_used:
            return False
    return True


# Definimos la funcion para detectar si es un pangrama (tiene todas las letras del abecedario)

def pangram(text):

    # creamos una lista con el abecedario, recorremos las letras del texto, y vamos eliminando de la lista las letras que hay en el texto, si al terminar de
    # recorrer el texto la longitud de la lista es 0, es que estaban todas las letras del abecedario en el texto, si no es 0, es que alguna letra no estaba

    unused_letters = list("abcdefghijklmnñopqrstuvwxyz")
    for letter in text:
        if letter in unused_letters:
            unused_letters.remove(letter)
    if len(unused_letters) == 0:
        return True
    else:
        return False


# Definimos la funcion principal

def heterogram_isogram_pangram():

    # solicitamos el texto e imprimimos la primera parte de la respuesta del programa

    text = input("Itroduce un texto: ")
    print("El texto introducido ", end = "")

    # pasamos el texto a las funciones anteriormente creadas y imprimimos en funcion de lo que haya devuelto

    if heterogram(text):
        print("es un heterograma, ", end = "")
    else:
        print("no es un heterograma, ", end = "")
    if isogram(text):
        print("es un isograma, ", end = "")
    else:
        print("no es un isograma, ", end = "")
    if pangram(text):
        print("y es un pangrama.")
    else:
        print("y no es un pangrama.")

heterogram_isogram_pangram()