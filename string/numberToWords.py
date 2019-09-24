def numberToWords(num):
    lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    thousands = ["","Thousand","Million","Billion"]
    res=[]
    n=0
    count=0
    while num:
    	value=num%100
    	if count==3:
    		res=['Thousand']+res
    	if count==6:
    		if res[0]=="":
    			res.remove('Thousand')
    		res=['Million']+res
    	if count==9:
    		if res[0]=="":
    			res.remove('Million')
    		res=['Billion']+res
    	if n<2:
    		if value>=20:
    			res=[tens[value//10]]+[lessThan20[value%10]]+res
    		else:
    			res=[lessThan20[value]]+res
    		n=n+2
    		num=num//100
    		count=count+2
    	elif n==2:
    		if value%10:
    			res=[lessThan20[value%10]]+['Hundred']+res
    		n=0
    		num=num//10
    		count=count+1
    res=" ".join(res)
    print(" ".join(res.split()))

numberToWords(1010010)



