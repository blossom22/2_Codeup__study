# Codeup_스택_3117: 0은 빼!

import sys
k = int(sys.stdin.readline())
stack = []
for i in range(k):
    n = int(sys.stdin.readline())
    if n!=0:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))