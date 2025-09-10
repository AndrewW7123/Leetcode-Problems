def maximum69Number (num):
    """
    :type num: int
    :rtype: int
    """
    sNum = str(num)
    lNum = []
    for i in sNum:
        lNum += i
    lLen = len(lNum)
    maxNum = ""

    for i in range(lLen):
        if (lNum[i] == "6"):
            lNum[i] = "9"
            for j in lNum:
                maxNum += j
            return int(maxNum)

    return num