# Codeup_Python 기초3.단순 반복문_1271: 최댓값 구하기

n=int(input("자연수를 입력하세요: "))
a=list(map(int, input("수를 입력하세요: ").split()))
print(max(a))

# max함수를 이용하지 않고 풀면 아래와 같다. 원소들을 하나하나 비교해서 더 큰값을 출력하는 방식이다. 
n = int(input("자연수를 입력하세요: "))
a = list(map(int, input("수를 입력하세요: ").split()))
b = a[0]
for i in a[1:]:
    if i > b:
        b = i
print(b)