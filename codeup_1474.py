# Codeup_Python 기초5-3.2차원배열_1474: 2차원 배열 지그재그 채우기 2-7

a, b = map(int, input().split())
arr = [[0] * b for _ in range(a)]
c = 1

for i in range(b-1,-1,-1):
    if i % 2 == (b%2==0):
        for j in range(a-1,-1,-1):
            arr[j][i] = c 
            c+=1 
    else:
        for j in range(a):
            arr[j][i] = c 
            c+=1 
for i in arr:
    print(*i)


