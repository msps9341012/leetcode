from heapq import *
def minMeetingRooms(intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    intervals.sort()
    pq=[]
    res=0
    for i in intervals:
        """
        pop meetings already end
        """
        while pq and pq[0]<=i[0]:
            heappop(pq)
        heappush(pq,i[1])
        res=max(res,len(pq))
    return res
print(minMeetingRooms([[1,5],[8,9],[8,9],[9,10]]))