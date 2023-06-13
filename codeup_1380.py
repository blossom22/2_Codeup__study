# Codeup_Python 기초4-2.중첩반복문_1380: 두 주사위의 합

n = int(input("자연수를 입력하세요: "))
[print(i, n-i) for i in range(1,n) if i<=6 and n-i<=6]      # 리스트컴프리헨션으로 간결하게 만들었다. 
