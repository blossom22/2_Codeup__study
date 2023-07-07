# Codeup_Python 기초5-3.2차원배열_1507: 4개의 직사각형 넓이

matrix = [[0]*100 for _ in range(100)]
a = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            matrix[x][y] = 1

for row in matrix:
    a += sum(row)       # 직사각형 있는 곳만 1이고, 나머지 칸은 0으로 채워져있다
print(a)