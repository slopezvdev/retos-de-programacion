'''
* Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 '''

# Definimos las tres funciones que usaremos en la funcion principal
def is_prime(number):
    if number > 1:
        for n in range(2, number):
            if number % n == 0:
                return ("no es primo")
        return("es primo")
    else:
        return("no es primo")

def is_fibonacci(number):
    a, b, c = 0, 1, 0
    while c <= number:
        if c == number:
            return("es fibonacci")
        a = b
        b = c
        c = a + b
    return("no es fibonacci")

def is_even(number):
    if number % 2 == 0:
        return("es par")
    else:
        return("es impar")
    
# Definimos y desarrollamos la funcion principal
def prime_fibonacci_even():
    number = int(input("Introduce un numero: "))

    # Imprimimos el resultado
    print(f"El numero {number} {is_prime(number)}, {is_fibonacci(number)} y {is_even(number)}")



# Llamamos la funcion
prime_fibonacci_even()