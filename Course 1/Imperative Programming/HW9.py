def exp(t):
    return t*(t-20)*(t-100) + 120000


diff = 0
maxdiff = 0
time = 0
for t in range(2,101):
    diff = exp(t-1) - exp(t)
    if diff > maxdiff:
        maxdiff = diff
        time = t
    else:
        continue

print(time)

