def fun(x):
    flag = True
    i = 2
    while flag and i < len(x):
        if x[i] - x[i-1] != x[i-1] - x[i-2]:
            flag = False
        else: 
            i+=1
    return flag

print(fun([2,4,6,8,10]))

#Checks if the numbers are in an AP or not





