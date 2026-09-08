import random
n = 10
b = []
list_of_lists = [random.sample(list(range(n)), n) for _ in range(5)]
for i in list_of_lists:
    for c in i:
        b.append(c)
print(b)