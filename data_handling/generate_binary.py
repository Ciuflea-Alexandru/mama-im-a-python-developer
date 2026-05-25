# Generate n binary numbers in a list

from collections import deque

def generate_binary(n):
    r = []
    q = deque()
    q.append(1)
    for x in range(n):
        re = q.popleft()
        r.append(re)
        q.append(re * 10)
        q.append(re * 10 + 1)
    return r

n = 6

print(generate_binary(n))