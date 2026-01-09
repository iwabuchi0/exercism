def square(number):
    if number <1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    contador = 2
    grao = 0
    while contador < 65:
        grao += 2**(contador-1)
        contador += 1
    return grao + 1