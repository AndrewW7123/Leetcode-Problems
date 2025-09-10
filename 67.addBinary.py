def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    i = len(a) - 1
    j = len(b) - 1
    newBinary = ""
    carry = False

    while (min(i,j) >= 0):
        indA = a[i]
        indB = b[j]

        if (indA == "1" and indB == "1"):
            if (carry == True):
                newBinary += "1"
            else:
                newBinary += "0"
                carry = True
        elif ((indA == "1" and indB == "0") or (indA == "0" and indB == "1")):
            if (carry == True):
                newBinary += "0"
            else:
                newBinary += "1"
                carry = False
        else:
            if (carry == True):
                newBinary += "1"
            else:
                newBinary += "0"
            carry = False
        i -= 1
        j -= 1
    
    if (len(a) != len(b)):
        if (i > j):
            k = a
            l = i
        elif (i < j):
            k = b
            l = j
        while (l >= 0):
            if (k[l] == "1"):
                if (carry == True):
                    newBinary += "0"
                else:
                    newBinary += "1"
            else:
                if (carry == True):
                    newBinary += "1"
                    carry = False
                else:
                    newBinary += "0"
            l -= 1

    if (carry == True):
        newBinary += "1"
    
    newBinary = newBinary[::-1]
    if ("1" not in newBinary):
        newBinary = "0"
    else:
        i = 0
        while (newBinary[i] != "1"):
            newBinary = newBinary[i+1:len(newBinary):]
            i += 1

    return newBinary