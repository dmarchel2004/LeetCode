def zero(l, j):
    right = 0
    left = 0
    jef = l.index(j)
    for j in range(len(l)-jef):
        if l.index(l[jef+right]) == max(l):
            return False
        elif l[jef+right] != '0':
            return True
        else:
            right += 1
    for k in range(l.index(j)):
        if l.index(l[jef-left]) == min(l):
            return False
        elif l[jef-left] != '0':
            return True
        else:
            left += 1


def main():
    x = raw_input("jef")
    final =''
    x = str(x)
    if x == '0' or int(x) > 2147483647:
        return int(x)
    for i in x:
        if i == '-':
            final += '-'
        elif i == '0':
            if zero(x, i) == False:
                x.pop(i)
    x = x.replace("-","")
    x = x[::-1]
    final += x
    print final
    return int(final)
main()
