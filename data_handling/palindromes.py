# Determine if a list is a palindrome

def is_palindrome(teststr):
    teststr = teststr.lower()

    newstr = ''
    for s in teststr:
        if s.isalpha():
            newstr += s

    reversestr = newstr[::-1]

    return newstr == reversestr

test_word_1 = "Anna"
test_word_2 = "Alex"

palindrome = is_palindrome(test_word_1)
not_palindrome = is_palindrome(test_word_2)

print(palindrome)
print(not_palindrome)