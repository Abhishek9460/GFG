#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        psList=[]
        ngList=[]
        for i in range(len(arr)):
            if arr[i]>=0:
                psList.append(arr[i])
            else:
                ngList.append(arr[i])
        p=0
        n=0
        for i in range(len(arr)):
            if n == len(ngList):
                arr[i]=psList[p]
                p+=1
            elif p ==len(psList):
                arr[i]=ngList[n]
                n+=1
                
            elif i%2==0:
                arr[i]=psList[p]
                p+=1
            else:
                arr[i]=ngList[n]
                n+=1
        
    
                
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends