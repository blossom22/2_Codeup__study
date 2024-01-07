# Codeup_스택_2016: 천단위 구분기호

from collections import deque
import sys
n = int(sys.stdin.readline())
num = deque(sys.stdin.readline().strip())
ans = deque()
i = 1
while len(num)>0:
    if i%4!=0:
        ans.appendleft(num.pop())
        i+=1
    else:
        ans.appendleft(',')
        i+=1
print(''.join(ans))