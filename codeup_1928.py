# Codeup_Python 재귀함수_1928:  (재귀함수) 우박수 (3n+1) (basic)

import sys
n = int(sys.stdin.readline())
def DFS(n):
    if n==1:
        return
    else:
        if n%2==1:
            print(3*n+1)
            n = (3*n+1)
            DFS(n)
        else:
            print(n//2)
            n = n//2
            DFS(n)
print(n)
DFS(n)