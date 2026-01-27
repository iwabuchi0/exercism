import math

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range (5, math.isqrt(number) + 1, 6):
        if number % i == 0 or number % (i+2) == 0:
            return False
    return True 
        
def aliquot_sum(number):
    if number == 1:
        return 0
    if is_prime(number):
        return 1
    soma = 1
    root = math.isqrt(number)

    for i in range(2, root + 1):
        if number % i == 0:
            soma += i 
            par = number // i
            if par != i:
                soma += par
    return soma
    

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0: 
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"
    
    result_some = aliquot_sum(number)

    if is_prime(number):
        return "deficient"
    if result_some == number:
        return "perfect"
    if result_some > number:
        return "abundant" 
    else: 
        return "deficient"
