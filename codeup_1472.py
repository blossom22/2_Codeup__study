# Codeup_Python 기초5-3.2차원배열_1472: 2차원 배열 지그재그 채우기 2-5

a,b = map(int, input().split())
arr = [[0]*b for _ in range(a)]
c = 1
for j in range(a-1,-1,-1):
    if a%2 == 0:
        if j%2==1:
            for i in range(b-1,-1,-1):
                arr[j][i] = c
                c+=1
        else:
            for i in range(b):
                arr[j][i] = c
                c+=1
    else:
        if j%2==0:
            for i in range(b-1,-1,-1):
                arr[j][i] = c
                c+=1
        else:
            for i in range(b):
                arr[j][i] = c
                c+=1
for i in arr:
    print(*i)



# 아래처럼 간결하게 표현할 수 있다. 
a, b = map(int, input().split())
arr = [[0] * b for _ in range(a)]
c = 1
for j in range(a - 1, -1, -1):
    if j % 2 == (a % 2 == 0):           # a가 짝수라면 True(1), 홀수라면 False(0)를 반환
        for i in range(b - 1, -1, -1):
            arr[j][i] = c
            c += 1
    else:
        for i in range(b):
            arr[j][i] = c
            c += 1
for row in arr:
    print(*row)