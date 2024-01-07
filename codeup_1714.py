# Codeup_스택_1714: 숫자 거꾸로 출력하기

import sys
n = list(sys.stdin.readline().strip())
stack = []
for i in range(len(n)):
    stack.append(n.pop())
print(''.join(stack))