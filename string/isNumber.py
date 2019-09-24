def isNumber(self, s):
    """
    :type s: str
    :rtype: bool
    """

    s = s.strip()
    met_dot = met_e = met_digit = False
    for i, char in enumerate(s):
        if char in ['+', '-']:
            if i > 0 and s[i-1] != 'e':
                return False
        elif char == '.':
            if met_dot or met_e: 
                return False
            met_dot = True
        elif char == 'e':
            if met_e or not met_digit:
                return False
            met_e, met_digit = True, False
        elif char.isdigit():
            met_digit = True #用來handle沒有數字的情況 '. -+'
        else:
            return False
    return met_digit


print(isNumber('+.8'))



'''
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
'''