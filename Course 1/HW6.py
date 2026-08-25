w = float(input('enter weight: '))
if w<=2:
    p = 3
elif 2<w<=5:
    p = 3+2*(w-2)
elif w>5:
    p = 3+2*(5-2)+3*(w-5)

print(p)