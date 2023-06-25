# Codeup_Python 기초5-3.2차원배열_1461: 2차원 배열 순서대로 채우기 1-2

n = int(input())
arr = [[0] * n for _ in range(n)]
a = 1
for i in range(n):
    for j in range(n-1,-1,-1):
        arr[i][j] = a
        a += 1
for i in arr:
    print(*i)
