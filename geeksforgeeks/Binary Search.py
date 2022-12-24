"""
Given a sorted array of size N and an integer K, find the position at which K is present in the array using binary search.

Example 1:

Input:
N = 5
arr[] = {1 2 3 4 5} 
K = 4
Output: 3
Explanation: 4 appears at index 3.

Example 2:

Input:
N = 5
arr[] = {11 22 33 44 55} 
K = 445
Output: -1
Explanation: 445 is not present.

Your Task:  
You dont need to read input or print anything. Complete the function binarysearch() which takes arr[], N and K as input parameters and returns the index of K in the array. If K is not present in the array, return -1.


Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(LogN) if solving recursively and O(1) otherwise.


Constraints:

1 <= N <= 105
1 <= arr[i] <= 106
1 <= K <= 106
"""

#User function template for Python
#..........................................................................................
class Solution:	
	def binarysearch(self, arr, n, k):
		low=0
		high=n-1
		mid=(low+high)//2
		
		if k not in arr:
		    return -1
		else:
    		if k == arr[mid]:
    		    return mid
    		else:
    		    if k > arr[mid]:
    		        return (mid+1) + self.binarysearch(arr[mid+1:],n//2,k)
    		    else:
    		        return self.binarysearch(arr[:mid],n//2,k)
#..........................................................................................


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends
