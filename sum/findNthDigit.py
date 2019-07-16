def findNthDigit(n):

    count=0
    i=1
    while count<=n:
        bound=i*9*(10**(i-1)) 
        count=count+bound
        print(bound)
        if count>=n:
            break
        i=i+1
    move=bound-(count-n)
    print(move,i)
    ans=(1*10**(i-1))+(move-i)//i
    print(ans)
    if move%i:
        ans=ans+1
        return str(ans)[move%i-1]
    return str(ans)[-1]
    #print(''.join(list(map(str,range(start,start+move//i+1))))[move-1])
    
    #print(str(start)[::-1][move])
print(findNthDigit(10))
