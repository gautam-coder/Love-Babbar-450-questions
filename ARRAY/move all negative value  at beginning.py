#approach is two pointer approach
def moveAllNegative(a,n):
    l=0
    h=n-1
    while l<h:
        if a[l]>0 and a[h]<0:
            t=a[l]
            a[l]=a[h]
            a[h]=t
            l+=1
            h-=1
        elif a[l]<0:
            l+=1
        elif a[h]>=0:
            h-=1
    print(a)

n=int(input())
a=list(map(int,input().split()))
print(moveAllNegative(a,n))
            
