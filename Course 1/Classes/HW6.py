def max_char_rep(s):
    count = 1
    max_count = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        if count > max_count:
            max_count = count
    return max_count

print(max_char_rep('abaaaababab'))
