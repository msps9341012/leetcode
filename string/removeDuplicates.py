def removeDuplicates(s, k):
    stack = [['#', 0]]
    for c in s:
        if stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([c, 1])
    return ''.join(c * k for c, k in stack)


s='deeedbdd'
k=2

print(removeDuplicates(s,3))