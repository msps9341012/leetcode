import heapq
from collections import Counter
def topKFrequent(nums, k):
    res = []
    dic = Counter(nums)
    max_heap = [(-val, key) for key, val in dic.items()]
    heapq.heapify(max_heap)
    print(max_heap)
    for i in range(k):
        res.append(heapq.heappop(max_heap)[1])
    return res   

#bucket sort
def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    freq, result = Counter(nums), []
    inverse_freq = defaultdict(list)
    for k1,v1 in freq.items():
        inverse_freq[v1].append(k1)
    for x in range(len(nums), 0, -1):
        if x in inverse_freq:
            result.extend(inverse_freq[x])
            if len(result) >= k:
                break
    return result[:k]
