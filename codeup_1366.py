# Codeup_Python 기초4-2.중첩반복문_1366: 사각형 출력하기 4

n = int(input("사각형의 크기를 입력하세요: "))
for i in range(n):
    if i == 0 or i == n // 2 or i == n - 1:
        print('*' * n)
    else:
        row = [' '] * n
        row[0] = '*'
        row[n - 1] = '*'
        row[i] = '*'
        row[n - i - 1] = '*'
        row[n // 2] = '*'
        print(''.join(row))