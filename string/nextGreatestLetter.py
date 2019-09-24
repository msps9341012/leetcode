def nextGreatestLetter(letters, target):
    n = len(letters)
    if n == 0:
        return None
    
    low = 0
    high = n - 1
    # If it can not be found, must be the first element (wrap around)
    result = 0 
    
    while low <= high:
        mid = (low+high)// 2
        if letters[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return letters[low%len(letters)]

letters = ["a",'b']
target = "z"
print(nextGreatestLetter(letters,target))