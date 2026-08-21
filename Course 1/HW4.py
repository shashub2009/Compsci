a = int(input('enter total: '))
if a > 21:
    b = 'bust'
elif 17 <= a < 21:
    b = 'stay'
else:
    b = 'hit'
print(b)