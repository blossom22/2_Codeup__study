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

# 코드를 최대한 줄이면 이렇게도 표현가능하다. 파이썬에서 ';'는 한줄에 여러문장을 쓸 때 사용되지만, 가독성을 위해 문장을 개행하여 구분하는 것이 권장된다. 
n=int(input());a=list(map(int,input().split()));print(*a[::-1])