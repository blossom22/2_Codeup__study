# Codeup_Python 기초100제_6067: 정수 1개 입력받아 분류하기
a = int(input("정수 1개를 입력하세요: "))
if a<0 and a%2==0 : 
    print("A")
elif a<0 and a%2==1:
    print("B")
elif a>0 and a%2==0: 
    print("C")
else:
    print("D")
