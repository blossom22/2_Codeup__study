# Codeup_Python 기초100제_6014: 실수 1개 입력받아 3번 출력하기
a = float(input("실수를 입력하세요: "))
print(a,a,a, sep='\n')


# 아래와 같이, for문을 이용해서 연속으로 출력할 수도 있다. 
a = float(input("실수를 입력하세요: "))
for i in range(3):
    print(a)