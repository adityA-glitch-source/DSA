# Equal Strings
def equal_strings(s,t):
    if len(s)!=len(t):
        return False
    for i in range(len(s)):
       if s[i]!=t[i]:
           return False
    return True

print(equal_strings('hello','world'))
