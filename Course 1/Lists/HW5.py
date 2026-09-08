lst = []
while a:= int(input('Enter positive numbers: ')):
    if a < 0:
        break
    if a not in lst:
        lst.append(a)
print(lst)
