from collections import Counter
def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    if not t or not s:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    l, r = 0, 0

    formed = 0

    window_counts = {}

    ans = float("inf"), None, None

    while r < len(s):

        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1
        print(window_counts)

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        while l <= r and formed == required:
            character = s[l]

            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
                print(ans)

            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            l += 1    

        r += 1    
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


def minWindow(s, t):
    if not t or not s:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))

    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1

        if window_counts[character] == dict_t[character]:
            formed += 1

        while l <= r and formed == required:
            character = filtered_s[l][1]

            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1    

        r += 1    
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

s='ABAACBAB'
t='ABC'
print(minWindow(s,t))

def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if len(s) < len(t):
        return ""
    
    hashmap = collections.Counter(t)
    counter = len(t)
    min_window = ""
    start, end = 0, 0
    
    
    for end in range(len(s)):
        if hashmap[s[end]] > 0:
            counter -= 1
        hashmap[s[end]] -= 1
        
        while counter == 0:
            length = end - start + 1
            
            if not min_window or len(min_window) > length:
                min_window = s[start:end+1]
            
            hashmap[s[start]] += 1

            if hashmap[s[start]] > 0:
                counter += 1
            
            start += 1
    return min_window