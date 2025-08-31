def calculator():
    print("간단한 사칙연산 계산기" )
try:
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
except ValueError:
    print("유효한 숫자를 입력해주세요.")
    return

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        try:
            if num2 == 0:
                raise ZeroDivisionError("0으로 나눌 수 없습니다.")
            result = num1 / num2
        except ZeroDivisionError as e:
            print(str(e))
            return
        else:
            print("0으로 나눌 수 없습니다.")
            return
    else:
        print("잘못된 연산자입니다.")
        return

    print(f"결과: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()