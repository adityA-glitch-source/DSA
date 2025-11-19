def is_palindrome(s):
    s = s.replace(" ",'').lower()
    rev = ''
    for i in range(len(s)-1,-1,-1):
        rev+=s[i]
    if s==rev:
        return True
    else:
        return False
print(is_palindrome('Malayalam'))

