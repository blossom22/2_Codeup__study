# Codeup_Python 재귀함수_1929:  (재귀함수) 우박수 (3n+1) (reverse)

import sys
n = int(sys.stdin.readline())
def DFS(n):
    if n==1:
        return
    else:
        if n%2==1:
            n = (3*n+1)
            DFS(n)
            print(n)
        else:
            n = n//2
            DFS(n)
            print(n)
DFS(n)
print(n)