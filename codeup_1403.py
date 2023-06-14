# Codeup_Python 기초5-1.1차원배열_1403: 배열 두번 출력하기

n = int(input("수를 입력하세요: "))
a = list(map(int, input("데이터를 입력하세요: ").split()))
[print(a[i] if i<n else a[i-n]) for i in range(n*2)]
