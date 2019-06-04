nums=[3,4,-1,1]
n=len(nums)
for i in range(n):
    if nums[i] <= 0: 
    	nums[i] = len(nums)+1
for i in range(n):
    if abs(nums[i]) <= n: 
    	nums[abs(nums[i])-1]=-abs(nums[abs(nums[i])-1])
for i in range(n):
    if nums[i] > 0: 
    	print(i+1)
print(n+1)
print (nums)