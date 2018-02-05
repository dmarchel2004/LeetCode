def zero(l, j):
    jef = l.index(j)
    for j in range(len(l)-jef):
        if l.index(l[jef+right]) == max(l):
            l.pop(j)
        elif l[jef+right] != '0':
            break
        else:
            right += 1
    for k in range(l.index(j)):
        if l.index(l[jef-left]) == min(l):
            l.pop(j)
        elif l[jef-left] != '0':
            break
        else:
            left += 1


def main():
    x = raw_input("jef")
    final =''
    right = 0
    left = 0
    x = str(x)
    if x == '0':
        return int(x)
    for i in x:
        if i == '-':
            final += '-'
        elif i == '0':
            zero(x, i)
    x = x.replace("-","")
    x = x[::-1]
    final += x
    print final
    return int(final)
main()
