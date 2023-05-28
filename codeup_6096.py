# Codeup_Python 기초100제_6096: 바둑알 십자 뒤집기


d=[]
for i in range(20) :
    d.append([])
    for j in range(20) : 
        d[i].append(0)                  # 리스트들에 0을 20개씩 넣고 그런 리스트가 20개가 있는 형태가 만들어진다. (20*20 형태의 리스트가 만들어짐)
for i in range(1,20):
    a = list(map(int, input("바둑알이 어떻게 배치되었는지 입력하세요: ").split()))
    for j in range(1, 20):
        d[i][j] = a[j-1]                # 내가 원하는 바둑판 모양대로 입력한다 (19*19 형태의 리스트가 만들어진다)

n = int(input("십자뒤집기 횟수를 입력하세요: "))
for i in range(n) :
    x,y=input("십자뒤집기 할 좌표를 입력하세요: ").split()
    for j in range(1, 20) :
        if d[j][int(y)]==0 :
            d[j][int(y)]=1
        else :
            d[j][int(y)]=0
    for j in range(1, 20) :
        if d[int(x)][j]==0 :
            d[int(x)][j]=1
        else :
            d[int(x)][j]=0

for i in range(1, 20) :                     # 처음에 20*20 규모의 리스트를 만들었기에, 가로와 세로 1줄씩은 출력할때 제외시켜야한다. 
    for j in range(1, 20) : 
        print(d[i][j], end=' ')   
    print()      