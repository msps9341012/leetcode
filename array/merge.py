def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    if not intervals:
        return []
    intervals.sort()

    merged = []
    for interval in intervals:
        # if the list of merged intervals is empty or if the current
        # interval does not overlap with the previous, simply append it.
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
        # otherwise, there is overlap, so we merge the current and previous
        # intervals.
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    if not intervals:
        return []
    intervals.sort()

    i = 1
    while i<len(intervals):
        deleted = False
        if intervals[i][0] <= intervals[i-1][1]  :
            intervals[i-1][1] =  max(intervals[i-1][1],intervals[i][1])
            del intervals[i]
            deleted = True
        if not deleted:
            i = i+1        
    return intervals