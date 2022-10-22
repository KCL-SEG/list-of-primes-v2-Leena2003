"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def check_prime(number):
    num = int(number)
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, round(num / 2) + 1):
            if num % i == 0:
                return False
            elif num % i != 0:
                if i == round(num / 2):
                    return True
def primes(number_of_primes):
    list = []

    if number_of_primes < 1:
        raise ValueError('Enter number greater than 0')

    y = 1
    while len(list) < number_of_primes:
        y += 1
        if check_prime(y):
            list.append(y)

    return list
