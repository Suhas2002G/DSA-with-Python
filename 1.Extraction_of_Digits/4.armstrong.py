

def check_armstrong(num:int)->bool:
    n=num 
    len=0
    while n>0:
        len+=1
        n=n//10

    n=num
    result=0
    while n>0:
        result=result+n%10**len 
        n=n//10 

    return result == num 


print(check_armstrong(153))