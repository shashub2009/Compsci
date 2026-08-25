n = int(input('enter a positive integer: '))
a=1
for i in range(1, n+1):
    a *= 3

print(a)

b = int(input('enter an integer: '))
c = int(input('enter a positive integer: '))
value = b
for i in range(1, c):
    value *= b

print(value)
