def transpose(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a))]

b = [[1,2,3],[4,5,6]]
print(transpose(b))