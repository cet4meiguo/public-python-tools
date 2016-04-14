def exchange(a,i,j):
    c = a[i]
    a[i] = a[j]
    a[j] = c 
    return a
def left(a):
    i=len(a)-1
    while i>=0:
        exchange(a,len(a)-1,i)
        i=i-1
        
a =[2,1,0,9,8,6,4,5,7,3]
i=0
while i<len(a):
    for n in range(0,len(a)):
        if a[n]==i:
            a = exchange(a,0,n)
            left(a)
            break
    i=i+1
print(a)
