a = int(input('enter value of s: '))
n = 1
found = False
while found == False:
    if (n*(n+1))/2 > a:
        print(n)
        found = True
    else:
        n += 1