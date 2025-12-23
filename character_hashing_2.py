s = "azyxyyzaaaa"
q = ["d","a","y","x"]
d = {}
for char in s:
    if char not in d:
        d[char]=1
    else:
        d[char]+=1
for c in q:
    if c in d:
        print(c, d.get(c))
    else:
        print(c,"doesn't exists")