def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if (x == 0):
        return 0
    if (x == 1):
        return 1

    dupe = x / 2
    while ((dupe * dupe) > x):
        dupe = dupe / 2
    while ((dupe * dupe) < x):
        dupe += 1
    
    if ((dupe * dupe) == x):
        return dupe
    
    return dupe - 1