
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        n = len(arr)
        left_max = [0] * n
        right_max = [0] * n
        water = 0

    # Calculate the maximum height to the left of each block
        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], arr[i])

    # Calculate the maximum height to the right of each block
        right_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])

    # Calculate the trapped water at each block
        for i in range(n):
            water += min(left_max[i], right_max[i]) - arr[i]

        return water





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends