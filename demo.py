# # extract digits
# n = 1234
# while n > 0:
#     digit = n % 10 
#     print(digit)
#     n = n//10


# # count digits
# n=1234
# count = 0
# while n > 0:
#     count += 1
#     n = n // 10

# print(f"Digit Count --> {count}")


# # reverse a number
# n=3456
# rev = 0
# while n>0:
#     rev = rev*10 + n%10
#     n=n//10

# print(f"reverse number --> {rev}")



def is_num_pallindrome(num:int)->bool:
    n = num 
    rev = 0 
    while n > 0 : 
        rev = rev * 10 + n % 10
        n = n // 10 

    return rev == num


print(is_num_pallindrome(1001))