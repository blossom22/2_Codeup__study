# Codeup_Python 기초3.if~else_1285: 계산기 2

a = input()
result = 0
current_number = ''
current_operator = '+'
index = 0

while index < len(a):
    char = a[index]
    if char.isdigit():      # isdigit함수는 문자열이 숫자로만 이루어졌는지 확인해준다. 하나라도 문자가 있으면 False, 전부 숫자면 True를 반환한다. 
        current_number += char
    elif char in ('+', '-', '*', '/'):
        if current_number:      # current_number에 숫자가 저장되어있다면, True반환
            number = int(current_number)
            if current_operator == '+':
                result += number
            elif current_operator == '-':
                result -= number
            elif current_operator == '*':
                result *= number
            elif current_operator == '/':
                result /= number
                result = int(result)  # 모든 계산은 정수형으로 처리하라고 했으므로, 나눗셈하면 소수가 나오는 결과를 int로 바꿔준다. 
        current_number = ''
        current_operator = char
    elif char == '=':
        if current_number:
            number = int(current_number)
            if current_operator == '+':
                result += number
            elif current_operator == '-':
                result -= number
            elif current_operator == '*':
                result *= number
            elif current_operator == '/':
                result /= number
                result = int(result)  # 나눗셈 결과를 정수형으로 처리
        break
    index += 1
print(result)