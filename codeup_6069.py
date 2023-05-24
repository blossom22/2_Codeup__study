# Codeup_Python 기초100제_6069: 평가 입력받아 다르게 출력하기
dic = {'A':'best!!!', 'B':'good!!', 'C':'run!', 'D':'slowly~'}  # 딕셔너리를 쓰면 굳이 if-elif-else로 길게 쓰지않고 코드를 간결하게 쓸 수 있다. 
a = input("문자를 입력하세요: ")
temp = dic.get(a, 'what?')      # 딕셔너리에서 get함수를 사용할때, 딕셔너리이름.get(key, default값)  ...이런식으로 사용한다. 
print(temp)                     # 이미 있는 key값이 get함수로 들어가면, 대응되는 value가 나오지만, 없는 key값을 입력하면 내가 설정한 default값이 출력된다.

# if문으로 이문제 해결하면 아래와 같다. 
a=input()
if a=='A':
    print("best!!!")
elif a=='B':
    print("good!!")
elif a=='C':
    print("run!")
elif a=='D':
    print("slowly~")
else:
    print("what?")  
