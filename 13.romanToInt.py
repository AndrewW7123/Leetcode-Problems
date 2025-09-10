def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    result = 0
    prev = ""

    for i in s:
        if (i == "M"):
            if (prev == "C"):
                result += 800
            else:
                result += 1000
        if (i == "D"):
            if (prev == "C"):
                result += 300
            else:
                result += 500
        if (i == "C"):
            if (prev == "X"):
                result += 80
            else:
                result += 100
        if (i == "L"):
            if (prev == "X"):
                result += 30
            else:
                result += 50
        if (i == "X"):
            if (prev == "I"):
                result += 8
            else:
                result += 10
        if (i == "V"):
            if (prev == "I"):
                result += 3
            else:
                result += 5
        if (i == "I"):
            result += 1
        prev = i
    
    return result