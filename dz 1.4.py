def print_even_reverse():
    try:
        n = int(input("Введіть число n: "))

        if n < 1:
            print("Число має бути більше або дорівнювати 1.")
            return

        print("Парні числа у зворотному порядку:")
        print(" ".join(str(num) for num in range(n, 0, -1) if num % 2 == 0))
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")


if __name__ == "__main__":
    print_even_reverse()
