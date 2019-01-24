def lengthOfLongestSubstring():
    s = raw_input()
    """
    :type s: str
    :rtype: int
    """
    sList = []
    lengths = []
    previous = []
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    for i in s:
        sList.append(i)
    for j in sList:
        index = 1
        length = 1
        x = s.index(j)
        if x + index < len(s) and s[x+index] != j:
            if j in previous:
                previous = []
                lengths.append(length)
                length = 1
                index = 1
            else:
                index += 1
                length += 1
                previous.append(j)
        lengths.append(length)
    print max(lengths)
