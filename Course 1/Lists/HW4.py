lst = []
while a := input("Enter a word (or '!' to finish): "):
    if a == "!":
        break
    lst.append(a)
print(lst)

while b := input("Enter more words (or '!' to finish): "):
    if b == "!":
        break
    if b in lst:
        print('hit')
    