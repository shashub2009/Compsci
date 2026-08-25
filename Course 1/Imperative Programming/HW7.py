found = False
n=1
while not found:
    if (n**3 - 16)%47 == 0:
        found = True
    else:
        n += 1
print(n)