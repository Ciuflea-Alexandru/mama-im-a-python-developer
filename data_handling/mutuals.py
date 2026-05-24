# Given two list select the variables that can be found in both of them

def find_mutual_friends(set1, set2):
    return set1.intersection(set2)

set1 = {"John", "Alice", "Bob"}
set2 = {"Alice", "Bob", "Charlie"}

print(find_mutual_friends(set1, set2))