
p=1
f=1
def e(x,n):
    global p,f    
    if(n==0):
        return 1
    r=e(x,n-1)
    p=p*x
    f=f*n
    return r+p/f

print(e(1,10))