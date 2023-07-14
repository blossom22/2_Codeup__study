# Codeup_Python 기초5-3.2차원배열_1480: 2차원 배열 빗금 채우기 3-5

n,m = map(int, input().split())
matrix = [[0]*m for _ in range(n)]

a = n*m
for i in range(n+m-1,-1,-1):
    start = max(0, i-(m-1))   
    end = min(i, n-1)
    for j in range(start, end+1):
        k = i - j
        matrix[n-1-j][m-1-k] = a    # 1476번과 빗금이 그어지는 방향은 똑같은데 숫자만 역순이니까, 초기값을 n*m으로 해서 a를 빼면서 matrix를 업데이트하면 된다
        a -= 1

for i in matrix:
    print(*i)