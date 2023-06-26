# Codeup_Python 기초5-3.2차원배열_1463: 2차원 배열 순서대로 채우기 1-4

n = int(input())
arr = [[0] * n for i in range(n)]
a = 1
for j in range(n):
    for i in range(n-1,-1,-1):
        arr[i][j] = a
        a += 1
for i in arr:
    print(*i)