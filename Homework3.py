b = False
s = int(input('Enter a number: '))
a = 0
while b == False:
    value = a**3 - 10*(a**2)
    if value > s:
        print(a, value)
        b = True
    a += 1
