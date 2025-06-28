
def is_pallindrome(s:str)->bool:
    start=0
    end=len(s)-1

    while start<end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True


print(is_pallindrome(s='suhas'))
print(is_pallindrome(s='nitin'))