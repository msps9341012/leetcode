def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    i=0
    final=''
    while i<len(str):
        if len(final)==0 and str[i]=='-':
            final=final+'-'
        elif len(final)==0 and str[i]=='+':
            final=final
        elif str[i].isdigit():
            final=final+str[i]
        elif len(final)>0 or str[i]!=' ':
            break
        i=i+1
    if final=='-' or len(final)==0:
        return 0
    final=int(final)
    final=min(2**31-1,final)
    final=max(-2**31,final)
    return final
print(myAtoi("33 ffe "))

def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = ''
        #remove left spaces
        str = str.lstrip(' ')
        
        # check empty string
        if (not str):
            return 0
        
        # check minus/plus signs
        if (str[0] == '-' or str[0] == '+'):
            num = str[0]
            str = str[1:]
            
        # check digits
        for ch in str:
            if (ch.isdigit()):
                num += ch
            else:
                break
                
        try: 
            value = int(num)
            #check overflow
            if (value.bit_length() >= 32):
                return (2**31-1) if value > 0 else -2**31
            return value
        except ValueError:
            return 0