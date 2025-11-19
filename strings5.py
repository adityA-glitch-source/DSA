# Removes duplicates in a string
def remove_duplicates(s):
    k = ''
    for i in s:
        if i not in k:
            k+=i
    return k
print(remove_duplicates('programming'))
