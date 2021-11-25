A=[43,12,76,1,3,89,21,32]
print("Array before Sorting :")
print(A)

def InsertionSort(A):
    for i in range(1,len(A)):
        
        key=A[i]
        j=i-1
        while (j>=0 and A[j]>key):
            A[j+1]=A[j]
            j=j-1
            A[j+1]=key
    return A

print("After sorting : ")
print(InsertionSort(A))