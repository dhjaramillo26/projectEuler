def LargestPrimeFactor(number):
    divider = 2
    while number > 1:
        if number % divider == 0:
            number = number / divider
        else:
            divider += 1
    return divider

print(LargestPrimeFactor(600851475143))