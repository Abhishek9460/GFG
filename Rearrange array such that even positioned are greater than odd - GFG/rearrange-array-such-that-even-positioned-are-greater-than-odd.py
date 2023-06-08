#User function Template for python3

class Solution:
    def assign (self, arr,  n) :
        #Complete the function
        arr.sort()

        for i in range(1, len(arr)):
            if (i + 1) % 2 == 0:
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
            else:
                if arr[i] > arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]

        return arr




#{ 
 # Driver Code Starts
#Initial Template for Python 3

  
def checkOrder(res):
    for i in range(1, len(res)):
        if(i%2 != 0):
            if(res[i] < res[i-1]):
                return False
        else:
            if(res[i] > res[i-1]):
                return False
    return True
for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.assign(arr, n)
    if(checkOrder(res)):
        print("Correct")
    else:
        print("Wrong Answer")



# } Driver Code Ends