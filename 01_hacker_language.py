'''
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''

# Definimos la funcion
def hacker_language():
    
    # Creamos un diccionario con la traduccion de cada letra
    dict = {    
        'A': '4',
        'B': '|3',
        'C': '[',
        'D': ')',
        'E': '3',
        'F': '|=',
        'G': '&',
        'H': '#',
        'I': '1',
        'J': ',_|',
        'K': '>|',
        'L': '1',
        'M': '|\/|',
        'N': '^/',
        'O': '0',
        'P': '|*',
        'Q': '(_,)',
        'R': '|2',
        'S': '5',
        'T': '7',
        'U': '(_)',
        'V': '\/',
        'W': '\/\/',
        'X': '><',
        'Y': 'j',
        'Z': '2'}
    
    # Solicitamos un texto a traducir y creamos una variable para el texto traducido
    input_text = input("Introduce el texto a traducir: ")
    output_text = ""

    # Hacemos un for para traducir letra a letra y las vamos añadiendo a la variable del texto traducido
    for letter in input_text.upper():
        if letter in dict:
            output_text += dict[letter]
        else:
            output_text += letter

    # imprimimos el texto traducido
    print(output_text)

# Llamamos a la funcion
hacker_language()