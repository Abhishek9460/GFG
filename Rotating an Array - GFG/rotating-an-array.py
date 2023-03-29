#User function Template for python3

class Solution:
    def leftRotate(self, arr, n, d):
        l1 =[]
        l2 =[]
        l1 = arr[:d]
        l2 = arr[d:]
        l2.extend(l1)
        for i in range(len(arr)):
            arr[i] = l2[i]
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        d = int(input())
        ob = Solution()
        ob.leftRotate(arr, n, d)
        for xx in arr:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends