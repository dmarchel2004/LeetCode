class Solution(object):
    def zero(self, l):
        isZero = True
        while isZero:
            if l[0] == '0':
                l.pop(0)
            if l[len(l)-1] == '0':
                l.pop(len(l)-1)
            else:
                isZero = False
        return l


    def reverse(self, x):
        x = str(x)
        chars = []
        final = ''
        if x == '0':
            return 0
        for i in x:
            chars.append(i)
            if i == '-':
                final += i
                chars.remove(i)
        chars = self.zero(chars)
        chars = chars[::-1]
        for a in chars:
            final += a
        if abs(int(final))>2147483647:
            return 0
        return int(final)
