import random


def guess_the_number():
    number = random.randint(1, 10)
    attempts = 3

    print("Гра 'Вгадай число'! Комп'ютер загадав число від 1 до 10. У вас є 3 спроби.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Спроба {attempt}. Введіть число: "))

            if guess < 1 or guess > 10:
                print("Будь ласка, введіть число в діапазоні від 1 до 10.")
                continue

            if guess == number:
                print("Вітаємо! Ви вгадали число!")
                return
            elif guess < number:
                print("Більше!")
            else:
                print("Менше!")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    print(f"На жаль, ви не вгадали. Загадане число було {number}.")


if __name__ == "__main__":
    guess_the_number()
