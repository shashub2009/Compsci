a = int(input("Enter a year: "))
b = False
if a%4 == 0:
    b = True
    if a%100 == 0:
        b = False
        if a%400 == 0:
            b = True

print(b)

