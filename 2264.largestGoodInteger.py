def largestGoodInteger(num):
    """
    :type num: str
    :rtype: str
    """
    if (len(num) < 3):
        return ""
    
    count = 1
    prev = num[0]
    maxNum = ""
    
    for i in num[1::]:
        if (i == prev):
            count += 1
        else:
            count = 1
        
        if (count == 3):
            if (maxNum == ""):
                maxNum = prev + prev + prev
            else:
                if (int((prev + prev + prev)) > int(maxNum)):
                    maxNum = prev + prev + prev
        prev = i

    return maxNum