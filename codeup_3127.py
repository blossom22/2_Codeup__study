# Codeup_스택_3127: 수식 계산 1

from collections import deque
n =deque(input().split())
stack = deque()
for i in n:
    if i=='*':
        a = int(stack.pop())
        b = int(stack.pop())
        stack.append(b*a)
    elif i=='+':
        a = int(stack.pop())
        b = int(stack.pop())
        stack.append(b+a)
    elif i=='-':
        a = int(stack.pop())
        b = int(stack.pop())
        stack.append(b-a)
    else:
        stack.append(int(i))
print(*stack)