import math
def calculate_factorial():
    try:
        n = int(input("Введіть число n: "))

        if n < 0:
            print("Факторіал визначений тільки для невід'ємних чисел.")
            return

        factorial = math.factorial(n)
        print(f"Факторіал числа {n} дорівнює {factorial}.")
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")


if __name__ == "__main__":
    calculate_factorial()
