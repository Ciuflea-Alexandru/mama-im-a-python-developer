def is_valid_parentheses(s):
    """
    Determines if the input string of brackets is valid using a stack.
    """
    stack = []
    # Mapping of closing brackets to their corresponding opening brackets
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            # Pop the top element from stack if it's not empty, else use a placeholder
            top_element = stack.pop() if stack else '#'
            
            # If the mapping doesn't match the stack's top element, it's invalid
            if mapping[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it onto the stack
            stack.append(char)
            
    # If the stack is empty, all opening brackets were properly closed
    return not stack

# Example Usage
if __name__ == "__main__":
    valid_str = "({[]})"
    invalid_str = "([)]"
    
    print(f"Is '{valid_str}' valid? {is_valid_parentheses(valid_str)}")
    print(f"Is '{invalid_str}' valid? {is_valid_parentheses(invalid_str)}")