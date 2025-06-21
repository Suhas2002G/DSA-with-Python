# Reverse a number
def reverse_number(n: int) -> int:
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

print(reverse_number(1234))


# Time Complexity:
# O(log₁₀N) → because the number of digits is log₁₀N, and we process each digit once.

# Space Complexity:
# O(1) → only a few variables used.