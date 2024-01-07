# Codeup_스택_3102: STL stack

n = int(input())
stack = []
for i in range(n):
    k = input()
    if k[0:2]=='pu':
        tmp = k.strip('push( )')    # 쓸모없는 글자는 전부 지우고 숫자부분만 필요하다
        stack.append(int(tmp))
    elif k[0]=='t':
        print(stack[-1]) if stack else print(-1)
    elif k=='pop()':
        if stack:
            stack.pop()
    elif k=='size()':
        print(len(stack))
    elif k=='empty()':
        print('false') if stack else print('true')
