# Codeup_Python 기초100제_6015: 공백을 두고 입력된 정수 2개를 줄바꿔서 출력하기 
a, b = input("정수 2개를 띄어쓰기하여 입력하세요: ").split()
print(b,a,sep='\n')

# split 함수안에 구분자를 넣어서 쪼개는 기준을 자세히 지정할 수 도 있다. 그냥 split()으로 쓰면 알아서 띄어쓰기나 엔터를 기준으로 쪼갠다. 