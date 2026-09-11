def alternate(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(lst[i])
        new_lst.append(lst[len(lst)-i-1])
    return new_lst

print(alternate([1,2,3,4,5,6,7,8,9]))