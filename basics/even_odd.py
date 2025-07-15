
n = 101 
print('even' if n % 2 == 0 else 'odd')


def check_even_odd(n:int)->str:
    return 'even' if n%2==0 else 'odd'

result = check_even_odd(2002)
print(result)

result = check_even_odd(20029)
print(result)