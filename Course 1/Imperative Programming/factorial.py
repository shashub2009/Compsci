n = int(input("Enter a positive integer: "))
if n > 0:
    b=1
    while n > 1:
        b *= n
        n-=1
        print(b)
else:
    print("give a proper number next time")

