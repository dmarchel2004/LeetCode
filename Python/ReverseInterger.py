def zero(l, j):
    right = 0
    left = 0
    jef = l.index(j)
    good = 0
    print "hi"
    print len(l)
    for m in range(len(l)-jef):
        print"hj"
        if l[jef+right] == max(l):
            print "hb"
            return False
        elif l[jef+right] != '0':
            print "hg"
            good = 1
        else:
            right += 1
            print "hc"
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
    zerolist = []
    if x == '0' or int(x) > 2147483647:
        return int(x)
    for s in x:
        zerolist.append(s)
        for i in zerolist:
            if i == '-':
                final += '-'
                zerolist.remove(i)
            elif i == '0':
                if zero(zerolist, i) == False:
                    zerolist.remove(i)
            print zerolist
    zerolist = zerolist[::-1]
    for c in zerolist:
        print final
        final += c
    print final
main()
