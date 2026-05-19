# Find out if all the characters in a string are unique

def has_unique_characters(s):
    r = set(s)
    return len(r) == len(s)

s = "sample"
print(has_unique_characters(s))