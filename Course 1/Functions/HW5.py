def REMOVE(ORIG, X, OUT):
    while X in ORIG:
        ORIG.remove(X)
        ORIG.append(0)
    OUT = ORIG
    return OUT

print(REMOVE([1,2,3,4,4,5,6,7,8,9], 4, [6,6,6,6,6,6,6,6,6,6]))
            