def insert(intervals, newInterval):
	for i in range(len(intervals)):
		if intervals[i][0]>newInterval[0]:
			break
	if intervals[i][0]>newInterval[0]:
		intervals=intervals[:i]+[newInterval]+intervals[i:]
	else:
		intervals=intervals+[newInterval]
	merged = []
	for interval in intervals:
		if not merged or merged[-1][1] < interval[0]:
			merged.append(interval)
		else:
			merged[-1][1] = max(merged[-1][1], interval[1])
	return merged



intervals = [[1,5]]
newInterval = [2,3]
print(insert(intervals, newInterval))