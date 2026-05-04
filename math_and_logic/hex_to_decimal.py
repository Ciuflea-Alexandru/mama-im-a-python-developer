# Convert a string hexadecimal number into an integer decimal

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDec(hexNum):
    hexNum = hexNum.upper()

    decimalvalue = 0
    
    reversedhex = hexNum[::-1]
    
    for i in range(len(reversedhex)):
        char = reversedhex[i]
        
        if char not in hexNumbers:
            return None
            
        decimalvalue += hexNumbers[char] * (16 ** i)
        
    return decimalvalue

number = 'A2'
print(hexToDec(number))