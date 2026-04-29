#Count the longest string in a list

def find_largest(test_strings):
    result = 0
    for word in test_strings:
        if len(word) > result:
            result = len(word)
    return result

test_strings = [
    "Hello World!",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it.",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
]

largest_string = find_largest(test_strings)
print(f'Longest string is: {largest_string}')