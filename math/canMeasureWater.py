def canMeasureWater(x, y, z):
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """
    if z>x+y:
        return False
    if z==0:
        return True
    a={0}
    if x>0:
        a.add(x-y%x)
    if y>0:
        a.add(y-x%y)
    if x>0 and y>0:
        a.add(x%y)
        a.add(y%x)
    print(a)
    for i in a:
        if i!=0:
            if z%i in a or z%i==0:
                return True
    return False

print(canMeasureWater(13,11,1))