def fun(n):
    if n>0:
        return fun(n-1)+n
    
    return 0
    
print(fun(5))