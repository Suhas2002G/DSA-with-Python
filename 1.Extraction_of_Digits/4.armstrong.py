
def check_armstrong(num: int) -> bool:
    n = num
    length = 0
    while n > 0:
        length += 1
        n = n // 10

    n = num
    result = 0
    while n > 0:
        digit = n % 10
        result += digit ** length
        n = n // 10

    return result == num



print(check_armstrong(153))
print(check_armstrong(1634))