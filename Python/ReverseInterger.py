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
            jef = x.index(i)
            for j in range(len(x)-jef):
                if x.index(x[jef+right]) == max(x):
                    x.remove('0')
                elif x[jef+right] != '0':
                    break
                else:
                    right += 1
            for k in range(x.index(i)):
                if x.index(x[jef-left]) == min(x):
                    x.remove('0')
                elif x[jef-left] != '0':
                    break
                else:
                    left += 1
    x = x.replace("-","")
    x = x[::-1]
    final += x
    print final
    return int(final)
main()
