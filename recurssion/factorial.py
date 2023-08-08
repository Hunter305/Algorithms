def fact(n):
    if n==0:
        return 1
    elif n>0:
        return fact(n-1)*n
    return 0
print(fact(5))

def fact1(n):
    if n==0:
        return 1
    elif n>0:
        i=1
        for z in range(1,n+1):
            i=i*z
        return i
print(fact1(5))