def determine_grade():
    try:
        score = int(input("Введіть кількість балів: "))

        if score < 0 or score > 100:
            print("Бали повинні бути в діапазоні від 0 до 100.")
            return

        if 0 <= score <= 49:
            grade = "незадовільно"
        elif 50 <= score <= 69:
            grade = "задовільно"
        elif 70 <= score <= 89:
            grade = "добре"
        else:
            grade = "відмінно"

        print(f"Ваша оцінка: {grade}")
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")


if __name__ == "__main__":
    determine_grade()