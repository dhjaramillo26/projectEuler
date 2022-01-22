def fibonacci():
    number_top = 4000000
    number_one = 1
    number_two = 2
    result = 2
    while number_two < number_top:
        number_temp = number_one + number_two
        number_one = number_two
        number_two = number_temp
        if number_two % 2 == 0:
            result += number_two
    return result

print(fibonacci())