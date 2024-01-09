# Codeup_Python 재귀함수_1953: (재귀함수) 삼각형 출력하기 1

n = int(input())
def DFS(n):
    if n==1:
        print('*')
    else:
        DFS(n-1)
        print('*'*n)
DFS(n)