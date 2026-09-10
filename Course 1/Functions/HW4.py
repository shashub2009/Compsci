def share(a,b):
    m = False
    for i in range(len(a)):
        if a[i] in b:
            m = True
        else:
            m = False
    return m

a = [1,2,3,4]
b = [4,5,6,7]

print(share(a,b))