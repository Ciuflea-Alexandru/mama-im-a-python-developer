# Given a string convert all the letters into the next one in the alphabet

def caesar_cipher(text, shift):
    result = []
    
    for char in text:
        # Handle uppercase letters (ASCII 65 to 90)
        if char.isupper():
            # Align 'A' to 0, apply shift, wrap with % 26, then restore back to ASCII
            new_char = chr(((ord(char) - 65 + shift) % 26) + 65)
            result.append(new_char)
            
        # Handle lowercase letters (ASCII 97 to 122)
        elif char.islower():
            # Align 'a' to 0, apply shift, wrap with % 26, then restore back to ASCII
            new_char = chr(((ord(char) - 97 + shift) % 26) + 97)
            result.append(new_char)
            
        else:
            result.append(char)
            
    # Glue the list of characters back into a single string
    return "".join(result)

# Test the function
message = "Hello, World! XYZ"
print(caesar_cipher(message, 3))  # Output: Khoor, Zruog! ABC
