neg = []
pos = []

while a:=(int(input("Enter a number (0 to stop): "))):
    if a < 0:
        neg.append(a)
    else:
        pos.append(a)

print("Negative numbers:", neg)
print("Positive numbers:", pos)