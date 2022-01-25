def square():
    sum_squares = 0
    squares_sum = 0
    for number in range(1,101):
        sum_squares += number ** 2
        squares_sum += number
    return (squares_sum ** 2) - sum_squares 
    
print(square())