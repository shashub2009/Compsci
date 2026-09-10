x = int(input('x: '))
y = int(input('input exponent number y: '))
result = 1
while y>0:
    if y%2 == 0:
        y = y/2
        x *= x
    else:
        result *= x
        y -= 1
print(result)