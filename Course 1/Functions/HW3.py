def read_ints():
    lst = []
    while a := input('Int input: ') != '':
        lst.append(a)
    return lst
print(read_ints())