def calculator():
    print("간단한 사칙연산 계산기" )
    num1 = float(input("첫 번째 숫자를 입력하세요: ") )
    operator = input("연산자를 입력하세요 (+, -, *, /): " )
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("0으로 나눌 수 없습니다.")
            return
    else:
        print("잘못된 연산자입니다.")
        return

    print(f"결과: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()