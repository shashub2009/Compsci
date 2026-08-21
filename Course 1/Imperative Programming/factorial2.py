n = int(input("Enter a positive integer: "))
if n > 0:
    b=1
    for i in range (2,n+1):
        b*=i
        
else:
    print("give a proper number next time")

print(b)