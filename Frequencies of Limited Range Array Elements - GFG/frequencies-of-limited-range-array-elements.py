class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        map={}
        for i in range(len(arr)):
            if arr[i] in map:
                map[arr[i]]+=1
            else:
                map[arr[i]]=1
        for i in range(N):
            if (i+1) in map:
                arr[i]=map[(i+1)]
            else:
                arr[i]=0
                    
            
        # code here




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends