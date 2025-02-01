def calculator():
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        operation = input("Введіть операцію (+, -, *, /): ")

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                print("Ділення на нуль")
                return
            result = a / b
        else:
            print("Некоректна операція")
            return

        print(f"Результат: {result}")
    except ValueError:
        print("Будь ласка, введіть коректні числа.")


if __name__ == "__main__":
    calculator()