def subarraySum(nums, k):
    count,p,d = 0,0,{0:1}
    for i in nums:
        p+=i
        if p-k in d:
            count+=d[p-k]
        if p not in d:
            d[p] = 1
        else:
            d[p] +=1
    return count

print(subarraySum([1,1,1,2,1,3],4))

import heapq
def min_intervals_length_sum(nums, K):
    n = len(nums)
    d = dict() # key: prefix sum; value: index
    d[0] = -1
    cur_sum = 0
    heap=[]
    for i, num in enumerate(nums):
        cur_sum += num
        if cur_sum - K in d:
        	print(i, d[cur_sum - K])
        	heapq.heappush(heap,-(i - d[cur_sum - K]))
        if len(heap) > 2:
            heapq.heappop(heap)
        d[cur_sum] = i
    if len(heap) < 2:
        return -1
    else:
        total = 0
        print(heap)
        while len(heap) > 0:
        	total += abs(heapq.heappop(heap))
        return total

A=[5,1,2,2,3,4,1]
K=5

print(min_intervals_length_sum(A,K))