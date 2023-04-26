# Codeup_Python 기초100제_6020: 주민번호 입력받아 형태 바꿔 출력하기
n = input("주민번호를 입력하세요: ").split('-') 
number = "".join(n)
print(number)

# join함수를 써서 리스트의 문자들을 하나로 합칠 수 있다. 이때 위와같이 한번에 붙일수도 있고, 아니면 아래처럼 구분자를 이용하여 붙일수도 있다.
a = ['b','c','d','e']
x = "-".join(a)
print(x)