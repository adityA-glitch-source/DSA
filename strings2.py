# Count a Vowel in a String
# input -> "Hello, World!"
# Output -> 3
def vowel_count(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in s:
        if i in vowels:
            count+=1
    return count

print(vowel_count('Hello, World!'))

