#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        map={}
        for i in range(len(A)):
        
            if A[i] in map:
                map[A[i]]+=1
            else:
                map[A[i]]=1
        for x,y in map.items():
            if y > N//2:
                return(x)
        return(-1)  
                
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends