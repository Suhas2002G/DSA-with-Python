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


# NOTE : in method-2 : if n == 0 then log10(n)-->raise errror, that why add error-handling
# n1=0
# print(int(log10(n1)+1))     Math Domain Error


# final code for method-2 
from math import log10
n=0
if n == 0:
    print(1)
else:
    print(int(log10(n)+1))   #1