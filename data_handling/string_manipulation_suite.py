def is_anagram(str1, str2):
    """Checks if two strings are anagrams of each other."""
    # Remove spaces and normalize case for accurate comparison
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

def reverse_words(sentence):
    """Reverses the order of words in a given sentence."""
    words = sentence.split()
    return " ".join(words[::-1])

def most_frequent_char(text):
    """Finds the most frequent character in a string using a dictionary."""
    counts = {}
    for char in text:
        if char != " ":
            counts[char] = counts.get(char, 0) + 1
    
    # Return the character with the maximum count
    return max(counts, key=counts.get)

if __name__ == "__main__":
    test_str = "listen silent"
    print(f"Is '{test_str}' an anagram? {is_anagram('listen', 'silent')}")
    
    sentence = "Hello world from Python"
    print(f"Reversed words: '{reverse_words(sentence)}'")
    
    char_str = "abracadabra"
    print(f"Most frequent char in '{char_str}': '{most_frequent_char(char_str)}'")