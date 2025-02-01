def print_range():
    try:
        start = int(input("Введіть початкове число: "))
        end = int(input("Введіть кінцеве число: "))

        if start > end:
            print("Початкове число має бути менше або дорівнювати кінцевому.")
            return

        print(f"Числа від {start} до {end}:")
        for num in range(start, end + 1):
            print(num)
    except ValueError:
        print("Будь ласка, введіть коректні цілі числа.")


if __name__ == "__main__":
    print_range()