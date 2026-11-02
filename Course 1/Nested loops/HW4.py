lst = [1,2,3,4,5,6]
for m in range(len(lst)):
    for n in range(len(lst)):
        if not m == n:
            print(10*lst[m]+lst[n])

