def group_anagrams(strs):
    """
    Groups an array of strings into anagram clusters using a dictionary.
    """
    anagram_map = {}
    
    for s in strs:
        # Sort the string to create a consistent key (e.g., "eat" becomes "aet")
        sorted_key = "".join(sorted(s))
        
        if sorted_key not in anagram_map:
            anagram_map[sorted_key] = []
            
        anagram_map[sorted_key].append(s)
        
    return list(anagram_map.values())

# Example Usage
if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(words)
    print(f"Original words: {words}")
    print(f"Grouped anagrams: {result}")