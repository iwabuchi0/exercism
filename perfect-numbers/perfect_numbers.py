import math

def is_prime(number)
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range (5, math.isqrt(number) + 1, 6):
        if number % i == 0 or number % (i+2) == 0:
            return False

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 3 OR :
        return "deficient"
    if number <= 0: 
        raise ValueError("Classification is only possible for positive integers.")
    if number 
