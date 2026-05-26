# Determine if a string has matching parentheses

from collections import deque

def check_matching_parentheses(s):
    r = deque()
    for x in s:
        if x == '(':
            r.append(x)
        elif x == ')':
            if not r:
                return False
            r.pop()
    return len(r) == 0

s = "(incre)me(nt)"
print(check_matching_parentheses(s))