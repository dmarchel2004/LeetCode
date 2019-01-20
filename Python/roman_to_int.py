class Solution(object):
    def romanToInt(self,s):
        final = 0
        """
        :type s: str
        :rtype: int
        #[1,2,3,4,5,6,7,8,9]
        """
        index = -1
        for i in s:
            if len(s) > 1 and index + 2 < len(s):
                index += 1
            if i == "M":
                final += 1000
            elif i == "C" and s[index+1] == "M":
                final -= 100
            elif i == "D":
                final += 500
            elif i == "C" and s[index+1] == "D":
                final -= 100
            elif i == "C":
                final += 100
            elif i == "X" and s[index+1] == "C":
                final -= 10
            elif i == "L":
                final += 50
            elif i == "X" and s[index+1] == "L":
                final -= 10
            elif i == "I" and s[index+1] == "X":
                final -= 1
            elif i == "X":
                final += 10
            elif i == "I" and s[index+1] == "V":
                final -= 1
            elif i == "V":
                final += 5
            elif i == "I":
                final += 1
        return int(final)
