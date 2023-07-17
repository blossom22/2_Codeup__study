# Codeup_Python 기초5-3.2차원배열_1498: 여러 개씩 묶어 작은 값 골라 배열 만들기 5-7

import sys
n,g = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = [(min(a[i:i+g])) for i in range(0,n,g)]
print(*b)