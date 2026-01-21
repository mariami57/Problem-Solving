def fizz_buzz_lucky(n: int):
    LUCKY_N = '3'
    result = []
    for num in range(1, n + 1):

        if LUCKY_N in str(num):
            result.append('Lucky')

        elif num % 3 == 0 and num % 5 == 0:
            result.append('FizzBuzz')

        elif num % 3 == 0:
            result.append('Fizz')

        elif num % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(num))

    return '\n'.join(result)


print(fizz_buzz_lucky(10))
