# Codeup_Python 기초5-3.2차원배열_1465: 2차원 배열 순서대로 채우기 1-6

a, b = map(int, input().split())
arr = [[0] * b for i in range(a)]
c = 1
for j in range(a-1,-1,-1):
    for i in range(b):
        arr[j][i] = c
        c += 1
for i in arr:
    print(*i)
