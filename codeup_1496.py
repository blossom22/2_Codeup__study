# Codeup_Python 기초5-3.2차원배열_1496: 두 개씩 묶어 작은 값 골라 배열 만들기 5-5

import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = []
for i in range(0,n,2):
    b.append(min(a[i:i+2]))
print(*b)