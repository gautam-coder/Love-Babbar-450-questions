#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        z=arr.count(0)
        t=arr.count(1)
        p=arr.count(2)
        for i in range(n):
            if z>0:
                arr[i]=0
                z-=1
            elif t>0:
                arr[i]=1
                t-=1
            elif p>0:
                arr[i]=2
                p-=1
            

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
