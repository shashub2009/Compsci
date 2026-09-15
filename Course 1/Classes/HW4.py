def file_type(s):
    a = s[s.rfind('.')+1:]
    return a

s = input('Enter: ')
print(file_type(s))