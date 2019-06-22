def reverseWords(self, s):
    s = s + ' '
    ans = []
    pre = ' '
    for c in s:
        if c == ' ':
            if pre != ' ':
                ans.append(pre)
                pre = ' '
        else:
            if pre == ' ':
                pre = c
            else:
                pre = pre + c
    return ' '.join(ans[::-1])