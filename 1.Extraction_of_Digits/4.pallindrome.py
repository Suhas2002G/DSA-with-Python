# Check number is pallindrome or not
# NOTE : pallindrome mean from R-->L and from L-->R same, i.e 121 is pallindrome

def check_pallindrome(n):
    num = n
    rev=0
    while n>0:
        rev=rev*10+n%10
        n=n//10
    return rev == num           # T or F
     

num = 188
print(check_pallindrome(num))   #False    T.C.-->O(log N)

num = 181
print(check_pallindrome(num))   #True

'''
Time Complexity:
The while loop runs once for each digit in the number `n`.
In each iteration, we divide `n` by 10 (i.e., n = n // 10), so the number of iterations
is equal to the number of digits in `n`, which is approximately log₁₀(n).
Therefore, the time complexity is O(log n).

Space Complexity:
We use only a constant amount of space (a few integer variables: num, rev, n),
so the space complexity is O(1).
 '''


# check String is pallindome or not
def str_pallindrome(str):
    if str == str[::-1]:
        print(1)
    else:
        print(0)

str_pallindrome('nitin')