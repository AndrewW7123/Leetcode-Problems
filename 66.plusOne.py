def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    if (len(digits) < 1):
        return []
    elif (len(digits) == 1):
        if ((digits[0] + 1) > 9):
            return [1,0]
    
    i = len(digits) - 2
    last = digits[len(digits)-1] + 1
    carry = False

    if (last > 9):
        digits[len(digits)-1] = 0
        carry = True
        while (i >= 0):
            if (carry == False):
                break
            if ((digits[i] + 1) > 9):
                digits[i] = 0
            else:
                digits[i] += 1
                carry = False
            i -= 1
        if (carry == True):
            digits.append(1)
            digits[0], digits[len(digits)-1] = digits[len(digits)-1], digits[0]

    else:
        digits[len(digits)-1] += 1

    return digits