# Codeup_Python 기초5-3.2차원배열_1460: 2차원 배열 순서대로 채우기 1-1

n = int(input())
arr = [[0] * n for _ in range(n)]
a = 1
for j in range(n):
    for i in range(n):
        arr[j][i] = a
        a += 1
for i in arr:
    print(*i)

# 아래처럼 간결하게 쓸 수도 있다. 
n = int(input())
for i in range(n):
    print(*range(i * n + 1, (i + 1) * n + 1))