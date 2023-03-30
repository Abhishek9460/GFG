#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        sum=0
        maxsum=0
        i,j=0,0
        for j in range(len(arr)):
            sum+=arr[j]
            while sum < 0:
                sum-=arr[i]
                i+=1
            maxsum = max(sum,maxsum)
        if maxsum==0:
            return(max(arr))
        else:
            return(maxsum)
            
        
        ##Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends