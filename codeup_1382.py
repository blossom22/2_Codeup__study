# Codeup_Python 기초4-2.중첩반복문_1382: GuguClass

for i in range(1, 10):
    for j in range(2, 6):
        if j == 5:
            print("%d x %d = %2d" % (j, i, j * i), end="")      # 5단일때는 공백없이 다음줄로 넘기라고 해서 이렇게 if문을 걸어야한다. 
        else:
            print("%d x %d = %2d\t" % (j, i, j * i), end="")
    print()