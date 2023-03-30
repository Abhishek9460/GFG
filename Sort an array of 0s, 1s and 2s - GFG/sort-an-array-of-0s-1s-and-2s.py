#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        i,j,k=0,0,len(arr)-1
        while j<len(arr):
            if arr[j]==0:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j+=1
            elif arr[j]==2 and j<k:
                arr[j],arr[k]=arr[k],arr[j]
                k-=1
            else:
                j+=1
            
                
            
        # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

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