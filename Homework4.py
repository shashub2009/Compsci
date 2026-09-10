a = int(input('Enter a positive integer: '))
b = int(input('Enter another positive integer: '))
t = 1
while t%a != 0 or t%b != 0:
    t +=1

print(t)