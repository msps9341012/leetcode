def partition(arr,low,high): 
    i = low-1         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high):  
        if arr[j] <= pivot: 
        	i = i+1 
        	arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return i+1 
  

def quickSelect(arr,k): 
    pi = partition(arr,0,len(arr)-1) 
    print(pi)
    while pi!=len(arr)-k:
    	if pi>len(arr)-k:
    		pi=partition(arr,0,pi-1)
    	if pi<len(arr)-k:
    		pi=partition(arr,pi+1,len(arr)-1)
    return arr[pi]

import heapq

def findKthLargest(nums, k):
    nums = [-num for num in nums]
    heapq.heapify(nums)
    print(nums)
    res = float('inf')
    for _ in range(k):
        res = heapq.heappop(nums)
    return -res

arr = [10, 7, 8, 9, 1, 5] 
print(findKthLargest(arr,2))
