# Codeup_Python 기초3.if~else_1210: 칼로리 계산하기

a,b=map(int, input("메뉴번호를 입력하세요: ").split())
dic={1:400, 2:340, 3:170, 4:100, 5:70}
c=dic[a]+dic[b]
print('angry') if (c>500) else print('no angry')
