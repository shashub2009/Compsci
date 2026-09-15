ssn = str(input('Enter ssn: '))
def date_of_birth(ssn):
    if ssn[6] == '+':
        a = '18'
    elif ssn[6] == '-':
        a = '19'
    elif ssn[6] == 'A':
        a = '20'    
    y = (a+str(ssn[4:6]))
    m = (ssn[2:4])
    d = (ssn[:2])
    return (y,m,d)
a = ''



print(date_of_birth(ssn))