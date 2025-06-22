# Check number is pallindrome or not
# NOTE : pallindrome mean from R-->L and from L-->R same, i.e 121 is pallindrome

def check_pallindrome(n):
    num = n
    rev=0
    while n>0:
        rev=rev*10+n%10
        n=n//10
    if rev == num:
        return True
    else:
        return False

num = 188
print(check_pallindrome(num))   #False    T.C.-->O(log N)

num = 181
print(check_pallindrome(num))   #True

'''
Time Complexity
The time complexity of an algorithm describes how the execution time grows as the input size increases.

Understanding the Loop: The core of the check_pallindrome function is the while n > 0: loop.
Operations Inside the Loop:
rev = rev * 10 + n % 10: These are constant-time arithmetic operations (multiplication, addition, modulo).
n = n // 10: This is also a constant-time arithmetic operation (integer division).
Number of Iterations: The loop continues as long as n is greater than 0. In each iteration, n is effectively divided by 10. This means the number of iterations is proportional to the number of digits in the input number n.
Logarithmic Relationship: If a number n has d digits, then d is approximately log 10(n). 

For example:
If n = 10, d = 2.
If n = 100, d = 3.
If n = 1000, d = 4. The loop runs d times.
Therefore, the time complexity is O(log N), where N is the value of the input number.

Explanation:

Each iteration of the loop reduces the number of digits in n by one. The number of iterations required to reduce n to 0 is directly proportional to the number of digits in n. Since the number of digits in n is roughly log 10(n), the time complexity is logarithmic.
 '''


# check String is pallindome or not
def str_pallindrome(str):
    if str == str[::-1]:
        print(1)
    else:
        print(0)

str_pallindrome('nitin')