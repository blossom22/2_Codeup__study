# Codeup_Python 기초5-3.2차원배열_1497: 두 개씩 묶어 큰 값 골라 배열 만들기 5-6

import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = []
for i in range(0,n,2):
    b.append(max(a[i:i+2]))
print(*b)

# 리스트 컴프리헨션을 쓴 풀이
import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = [(max(a[i:i+2])) for i in range(0,n,2)]
print(*b)