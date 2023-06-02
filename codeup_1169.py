# Codeup_Python 기초3.if~else_1169: 나이 계산 2

age = int(input("나이를 입력하세요: "))
birth_year = 2012 - age + 1
c = birth_year % 100        
d = 1 if birth_year < 2000 else 3
birth_info = f"{c} {d}"
print(birth_info)

