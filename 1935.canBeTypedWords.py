def canBeTypedWords(text, brokenLetters):
    """
    :type text: str
    :type brokenLetters: str
    :rtype: int
    """
    validWords = 0
    isValid = True

    for i in range(len(text)):
        if (text[i] in brokenLetters):
            isValid = False
        if ((text[i] == " ") or (i == len(text) - 1)):
            if (isValid):
                validWords += 1
            isValid = True
    return validWords