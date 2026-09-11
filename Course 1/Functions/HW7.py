def iterate(f,x,n):
    lst = []
    for i in range(1,n+1):
        x = f(x)
        lst.append(x)
    return lst

def a(x):
    b = 0.5*(x+(2/x))
    return b

print(iterate(a,1,6))
