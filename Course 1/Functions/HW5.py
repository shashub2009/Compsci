def REMOVE(ORIG, X, OUT):
    for i in range(len(ORIG)):
        print(i)
        if ORIG[9-i] == X:
            ORIG.remove(len(ORIG)-i)
            ORIG.append(0)
        else:
            continue
    OUT = ORIG
    return OUT

print(REMOVE([1,2,3,4,4,5,6,7,8,9], 4, [6,6,6,6,6,6,6,6,6,6]))
            