def isHappy(n):
    """
    會end up to a loop (4)

    """
    def recursive(n):
        if n**2<10 or n==4:
            return n%10
        res=0
        while n:
            res=res+(n%10)**2
            n=n//10
        return recursive(res)

    return recursive(n)==1


def isHappy2(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum([int(x) **2 for x in str(n)])
    return n==1
isHappy2(2)


#O(1)
int digitSquareSum(int n) {
    int sum = 0, tmp;
    while (n) {
        tmp = n % 10;
        sum += tmp * tmp;
        n /= 10;
    }
    return sum;
}

bool isHappy(int n) {
    int slow, fast;
    slow = fast = n;
    do {
        slow = digitSquareSum(slow);
        fast = digitSquareSum(fast);
        fast = digitSquareSum(fast);
        if(fast == 1) return 1;
    } while(slow != fast);
     return 0;
}