'''
Recursive Binary Search
'''

#Back-end complete function template for Python

class Solution:	
	def bin_search(self, arr, left, right, key):
		#check if left index is greater than right index
		#which means key is not found in the array
		if left > right:
			return -1
		
		#calculate the middle index
		mid = (left + right) // 2
		
		#check if the element at the middle index is equal to the key
		if arr[mid] == key:
			return mid
		
		#if the element is greater than the key, 
		#we search in the left half of the array
		elif arr[mid] > key:
			return self.bin_search (arr, left, mid - 1, key)
		
		#if the element is smaller than the key,
		#we search in the right half of the array
		else:
			return self.bin_search (arr, mid + 1, right, key)
	
	def binarysearch(self, arr, n, k):
		#call the recursive binary search function
		return self.bin_search(arr, 0, n-1, k)


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