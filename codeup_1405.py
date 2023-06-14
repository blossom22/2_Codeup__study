# Codeup_Python 기초5-1.1차원배열_1405: 숫자 로테이션

n = int(input("수를 입력하세요: "))
a = list(map(int, input("데이터를 입력하세요: ").split()))
b=[]
c=0
for i in range(n):
    for j in range(n):
        if j+i<n:
            b.append(a[j+i])
        else:
            b.append(a[j+i-n])
while True: 
    if c+len(a) <= len(b):
        print(*b[c:c+len(a)])
        c+=len(a)
    else:
        break

# 아래는 간결하게 바꿔본 코드이다. 위에서는 리스트 b를 만들기위해 리스트길이가 n초과하면 a의 처음부터 다시 추가하였다. 이런과정을 생략하기 위해 애초에 b에 a를 2번복사해두면 된다. 
n = int(input("수를 입력하세요: "))
a = list(map(int, input("데이터를 입력하세요: ").split()))
b = a + a       # 만약 a에 1 2 3 4 5 가 입력되면, b는 [1,2,3,4,5,1,2,3,4,5]가 된다. 
for i in range(n):
    for j in range(i, i+n):
        print(b[j], end=' ')
    print()