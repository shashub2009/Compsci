for i in range(10,38,3):
    print(i, end=' ')
print()
for i in range(998,899,-2):
    print(i, end=' ')
print()
a=-1
for i in range(1,21):
    if a == -1:
        a=1
    else:
        a=-1
    print(a,end=' ')
print()
for i in range(1,61):
    if i%3 == 0:
        print(9, end=' ')
    else:
        print(7, end=' ')