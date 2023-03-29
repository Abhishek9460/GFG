class Solution:
    def leftRotate(self, arr, k, n):
        k=k%len(arr)
        l1 = []
        l2 = []
        l1 = arr[:k]
        l2 = arr[k:]
        l2.extend(l1)
        for i in range(len(arr)):
            arr[i] = l2[i]
        # Your code goes here


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends