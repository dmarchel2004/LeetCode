
def romanToInt():
    s = raw_input("")
    n = []
    mCount = 0
    hCount = 0
    tCount = 0
    oCount = 0
    """
    :type s: str
    :rtype: int
    #[1,2,3,4,5,6,7,8,9]
    """
    index = 0
    for i in s:
        if i == "M":
            mCount += 1
        elif i == "C" and s[index+1] == "M":
            mCount -= 1
            hCount += 9
        elif i == "C" and s[index+1] == "D":
            hCount -= 1
        elif i == "D":
            hCount += 5
        elif i == "C" and s[index+1] != "M":
            hCount += 1
        elif i == "X" and s[index+1] == "C":
            hCount -= 1
            tCount += 9
        elif i == "X" and s[index+1] == "L":
            tCount -= 1
        elif i == "L":
            tCount += 5
        elif i == "X":
            tCount += 1
        elif i == "I" and s[index+1] == "X":
            tCount -= 1
            oCount += 9
        elif i == "I" and s[index+1] == "V":
            oCount -= 1
        elif i == "V":
            oCount += 5
        elif i == "I":
            oCount += 1

    thousand = ["0","1","2","3","4","5","6","7","8","9"]
    hundred = ["0","1","2","3","4","5","6","7","8","9"]
    ten = ["0","1","2","3","4","5","6","7","8","9"]
    one = ["0","1","2","3","4","5","6","7","8","9"]
    s = thousand[mCount] + hundred[hCount] + ten[tCount] + one[oCount]
    isZero = True
    for j in s:
        n.append(j)
    while isZero:
        if n[0] == "0":
            n.pop(0)
        else:
            isZero = False
    final = ''
    for k in n:
        final += k
    print final
    return int(final)
romanToInt()
