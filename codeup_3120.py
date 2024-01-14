# Codeup_그리디_3120: 리모컨
# 리모컨 조작 최소 횟수를 물었으니까, BFS를 하자. 
from collections import deque
import sys
a,b = map(int, sys.stdin.readline().split())
def BFS(a,b):
    Q = deque()
    Q.append(a)
    check = [0]*100     # 온도를 전부 담고도 남는 적당히 큰 배열 하나 만든다.
    check[a] = 1
    Level = 0
    while Q:
        n = len(Q)
        for i in range(n):
            x = Q.popleft()
            if x==b:
                return Level
            for nx in [x-1, x+1, x-5, x+5, x-10, x+10]:
                if nx>=0 and nx<=40 and check[nx]==0:
                    Q.append(nx)
                    check[nx]=1
        Level += 1
print(BFS(a,b))
