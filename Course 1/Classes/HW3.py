def dashify_substring(s,sub):
    if s.find(sub) >= 0:
        m = s.find(sub)
    a = s.replace(sub, '-'+sub+'-')
    return a

print(dashify_substring('hello', 'e'))

