def palindrome():
    largest_palindrome = 0
    for number1 in range(999, 99, -1):
        for number2 in range(999, 99, -1):
            result = str(number1 * number2)
            reverse = result[::-1]
            if result == reverse and int(result) > int(largest_palindrome):
                largest_palindrome = result
                break
    return largest_palindrome

print(palindrome())