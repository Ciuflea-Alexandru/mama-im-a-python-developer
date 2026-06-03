# read a list of names and sort them alphabetically

def process_names(name_list):
    sorted_names = sorted(name_list)
    
    print("Sorted Names:")
    for name in sorted_names:
        print(f"- {name}")

if __name__ == "__main__":
    my_names = ["Zoe", "Alice", "Charlie", "Bob", "David"]
    
    process_names(my_names)