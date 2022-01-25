def ordinal_prime_number(ordinal_number):
    counter = 0
    number = 2
    while counter < ordinal_number:
        if is_prime(number):
            counter += 1
        number += 1
    return number - 1

def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

print(ordinal_prime_number(10001))