def interleave(a,b):
    lst = []
    for (x, y) in zip(a,b):
        lst.append(x)
        lst.append(y)
    return lst

a = [1,2,3,4]
b = [5,6,7,8]
print(interleave(a,b))