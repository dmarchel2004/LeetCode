def zero(l, j):
    right = 0
    left = 0
    jef = l.index(j)
    good = 0
    print "hi"
    for m in range(len(l)-jef):
        print"hj"
        if l[jef+right] == max(l):
            return False
        elif l[jef+right] != '0':
            good = 1
        else:
            right += 1
    for k in range(l.index(j)):
        if l[jef-left] == min(l):
            return False
        elif l[jef-left] != '0':
            good = 2
        else:
            left += 1
        if good == 2:
            return True



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
                x.replace(i,'')
    x = x.replace("-","")
    x = x[::-1]
    final += x
    print final
    return int(final)
main()
