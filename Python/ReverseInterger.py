def zero(l, j):
    right = 0
    left = 0
    jef = l.index(j)
    print 'jef', jef
    while True:
        print right
        print left
        # print l[jef+right]
        # print l[jef-left]
        if l[jef+right] != '0' and l[jef-left] != '0':
            print 'o'
            return True
        elif l[jef+right] == '0' and jef + right + 1!= len(l):
            right +=1
            print 'f'
        elif l[jef - left] == '0' and jef - left != 0:
            left += 1
            print 'of'
        elif (l[jef+right] == '0' and jef + right + 1 == len(l)) or (l[jef - left] == '0' and jef - left == 0):
            print 'oof'
            return False

def reverse():
    x = raw_input("ppf")
    final =''
    zerolist = []
    removals = []
    if x == '0' or int(x) > 2147483647:
        return 0
    for s in x:
        zerolist.append(s)
    for i in zerolist:
        print 'i', i
        print i, zerolist.index(i)
        if i == '-':
            final += '-'
            zerolist.remove(i)
        elif i == '0':
            if zero(zerolist, i) == False:
                removals.append(i)
            else:
                removals.append('')
    place = 0
    for i in zerolist:
        if i == removals[0]:
            zerolist.remove(i)
    zerolist = zerolist[::-1]
    for c in zerolist:
        final += c
    print final
reverse()
