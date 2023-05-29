# Codeup_Python 기초100제_6098: 성실한 개미


maze=[]
for i in range(20) :
    maze.append([])
    for j in range(11) : 
        maze[i].append(0)                  # 리스트들에 0을 11개씩 넣고 그런 리스트가 11개가 있는 형태가 만들어진다. (11*11 형태의 리스트가 만들어짐)
for i in range(1,11):
    a = list(map(int, input("미로가 어떻게 배치되었는지 입력하세요: ").split()))
    for j in range(1, 11):
        maze[i][j] = a[j-1]                 # 미로 초기설정(테두리만들고, 벽만드는 과정)

x = 2
y = 2

while True:
    if maze[x][y] == 2:  # 먹이를 찾은 경우 먹이 있는 곳까지는 9로 출력하고 종료
        maze[x][y] = 9
        break
    
    maze[x][y] = 9  # 개미의 이동 경로를 9로 표시한다.
    
    if maze[x][y+1] != 1:  # 오른쪽으로 이동 가능한 경우
        y += 1
    elif maze[x+1][y] != 1:  # 아래쪽으로 이동 가능한 경우
        x += 1
    else:  # 더 이상 이동할 수 없는 경우 종료
        break

# 개미의 이동 경로 출력
for i in range(1,11):
    for j in range(1,11):
        print(maze[i][j], end=' ')
    print()