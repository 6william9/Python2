import re


def safe_calculator(func):
    def wrapper(expression):
        try:
            if not re.match(r'^[0-9+\-*/(). ]+$', expression):
                raise ValueError("Вираз містить недозволені символи!")

            result = func(expression)
            return result
        except ZeroDivisionError:
            return "Помилка: Ділення на нуль!"
        except SyntaxError:
            return "Помилка: Неправильний синтаксис виразу!"
        except ValueError as e:
            return f"Помилка: {e}"
        except Exception as e:
            return f"Невідома помилка: {e}"

    return wrapper


@safe_calculator
def calculate(expression):
    return eval(expression)


print(calculate("10 + 5"))
print(calculate("10 / 0"))
print(calculate("10 +"))
print(calculate("10 + abc"))
