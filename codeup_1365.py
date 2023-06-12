# Codeup_Python 기초4-2.중첩반복문_1365: 사각형 출력하기 3

n = int(input("사각형의 크기를 입력하세요: "))
# 사각형 패턴을 생성하고 출력
for i in range(n):
    row = [' '] * n
    if i == 0 or i == n - 1:
        print('*' * n)
    else:
        row[0] = '*'
        row[n - 1] = '*'
        row[i] = '*'
        row[n - i - 1] = '*'
        print(''.join(row))