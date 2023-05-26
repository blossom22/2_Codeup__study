# Codeup_Python 기초100제_6083: 빛 섞어 색 만들기
s = 0
a, b, c = map(int, input("정수 3개를 입력하세요: ").split())
for i in range(0,a):
    for j in range(0,b):
        for k in range(0,c):
            print(i, j, k)
            s += 1
print(s)