# Codeup_Python 기초5-1.1차원배열_1440: 자리 배치

n = int(input())
a = list(map(int, input().split()))
b = []

for i in range(n):
    b.append([])

for i in range(n):
    c = a[:]  # 원본 리스트를 복사하여 새로운 리스트 c를 생성
    for j in range(n-1):
        d = c[i]
        del c[i]
        if a[i] > c[j]:
            b[i].append('>')
            c.insert(i, d)  # 삭제한 값을 다시 삽입 (insert는   리스트.insert(들어갈index, 값)   꼴로 쓰인다)
        elif a[i] == c[j]:
            b[i].append('=')
            c.insert(i, d)
        else:
            b[i].append('<')
            c.insert(i, d)
    print('{0}: '.format(i+1), ' '.join(b[i]), sep='')