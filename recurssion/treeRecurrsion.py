def fun(n):
    if n>0:
        print(n,end=" ")
        fun(n-1)
        fun(n-1)

fun(3)