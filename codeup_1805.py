# Codeup_Python 구조체연습_1287: 입체기동장치 생산공장
import sys
n = int(sys.stdin.readline())
k = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
k.sort()
for i in range(n):
    print(*k[i])
