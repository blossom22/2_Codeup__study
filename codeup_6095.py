# Codeup_Python 기초100제_6095: 바둑판에 흰 돌 놓기



d=[]
for i in range(20) :
    d.append([])
    for j in range(20) : 
        d[i].append(0)    # 리스트들에 0을 20개씩 넣고 그런 리스트가 20개가 있는 형태가 만들어진다. (20*20 형태의 리스트가 만들어짐)

n = int(input())
for i in range(n) :
    x, y = input().split()                  
    d[int(x)][int(y)] = 1

for i in range(1, 20) :                     # 처음에 20*20 규모의 리스트를 만들었기에, 가로와 세로 1줄씩은 출력할때 제외시켜야한다. 
    for j in range(1, 20) : 
        print(d[i][j], end=' ')   
    print()                                 # 줄바꿈을 해준다. 