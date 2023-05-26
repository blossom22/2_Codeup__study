# Codeup_Python 기초100제_6082: 3 6 9 게임의 왕이 되자
# 문제: 1 부터 입력한 수까지 순서대로 공백을 두고 수를 출력하는데, 3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 'X' 를 출력한다. 
a = int(input("정수를 입력하세요: "))
for i in range(1, a+1):
    if (i % 10 == 3) or (i % 10 == 6) or (i % 10 == 9):
        print('X', end=' ')
    else:
        print(i, end=' ')
# sep='' 속성을 사용하면, print 출력문들 사이사이에 원하는 ''사이의 내용을 추가할 수 있다. 
# end='' 속성을 사용하면, print문의 출력을 완료후에, ''사이의 내용을 추가하는 것이다. 기본값으로 줄바꿈을 하는 \n이 들어가있다. 
# 그래서 위코드에서 6, 8번줄에서 end=' '를 넣지 않으면 기본값인 \n이 작용해서 줄바꿈을 해버린다. 