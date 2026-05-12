# Count the words in a file

def count_words(file_path):
    r = 0
    file = open(file_path, 'r')
    for l in file:
        w = l.split()
        r += len(w)
    return r

file = "data_handling/count_words.py"

print(count_words(file))