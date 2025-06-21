# Count the digits present in a number 

# way-1
n = 1235345
count = 0
while n > 0:
    count += 1 
    n = n // 10
print(count)


# way-2 
# Trick : find log10(n), then add +1, then convert into 'int'

from math import log10

n=123432
print(int(log10(n)+1))   #6

n1=12
print(int(log10(n1)+1))     #2

