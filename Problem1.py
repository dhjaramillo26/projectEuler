def multiples(below):
    result = 0
    for number in range(below):
        if number % 3 == 0 or number % 5 == 0:
            result += number
    return result


print(multiples(1000))