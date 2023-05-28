# Codeup_Python 기초100제_6097: 설탕과자 뽑기

data=[]
h, w = map(int, input("가로, 세로 크기를 입력하세요: ").split())
for i in range(h+1) :
    data.append([])
    for j in range(w+1) : 
        data[i].append(0)          # 일단 세로 h, 가로 w 크기의 0으로 채워진 판을 만든다. 

n = int(input("막대의 개수를 입력하세요: "))
for i in range(n):
    l, d, x, y = map(int, input("막대정보를 입력하세요: ").split())
    if d == 1:
        for i in range(0, l) :
            data[x+i][y] = 1
    else:
        for i in range(0, l) :
            data[x][y+i] = 1

for i in range(1, h+1) :                     
    for j in range(1, w+1) : 
        print(data[i][j], end=' ')   
    print() 