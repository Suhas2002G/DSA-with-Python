# Reverse a number

# Method-1
def reverse_number(n:int)->int:
    rev = 0
    while n>0:
        rev = rev*10 + n%10
        n = n//10
    return rev

print(reverse_number(10))

# Time Complexity:
# O(log₁₀N) → because the number of digits is log₁₀N, and we process each digit once.

# Space Complexity:
# O(1) → only a few variables used.



# Method-2 : If we want to keep leading zeros (as a string), use this version
def reverse_number_str(n: int) -> str:
    return str(n)[::-1]

print(reverse_number_str(10))  # Output: '01'

# Time Complexity
# str(n) → Converts integer to string → O(log₁₀N)
# (because the number of digits in n is proportional to log₁₀N)
# [::-1] → Reverses the string → O(D), where D = number of digits → again O(log₁₀N)
# Overall Time Complexity: O(log₁₀N)

# Space Complexity
# str(n) → Creates a string of size D → O(log₁₀N)
# [::-1] → Creates a reversed copy → O(log₁₀N)
# Overall Space Complexity: O(log₁₀N)
