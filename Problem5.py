def multiples():
    is_multiple = False
    number = 1
    while not is_multiple:  
        for i in range(1,21):
            if number % i != 0:
                is_multiple = False 
                number += 1
                break
            else:
                is_multiple = True 
    return number

print(multiples())


