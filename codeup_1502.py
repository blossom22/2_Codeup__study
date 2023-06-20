# Codeup_Python 기초5-3.2차원배열_1502: 2차원 배열 채우기 2

n = int(input())
array = [[0] * n for _ in range(n)]  # 크기가 n인 2차원 배열 초기화
num = 1
for j in range(n):
    for i in range(n):
        array[i][j] = num
        num += 1
for i in array:
    print(*i)