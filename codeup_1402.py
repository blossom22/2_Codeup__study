# Codeup_Python 기초5-1.1차원배열_1402: 거꾸로 출력하기 3

n = int(input("수를 입력하세요: "))
a = list(map(int, input("데이터를 입력하세요: ").split()))
b=[]
for i in range(n-1,-1,-1):
    b.append(a[i])
print(*b)


# b리스트를 만들지 않고 이렇게 풀 수도 있다. 
n = int(input("수를 입력하세요: "))
a = list(map(int, input("데이터를 입력하세요: ").split()))
for i in range(n-1,-1,-1):
    print(a[i],end=' ')
