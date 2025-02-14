result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a повинно бути більше або рівне b")
        if b > 100:
            raise IndexError("b не повинно бути більше 100")
        return a / b
    except ZeroDivisionError:
        print(f"Помилка: ділення на нуль при a={a}, b={b}")
    except ValueError as e:
        print(f"ValueError: {e}, a={a}, b={b}")
    except IndexError as e:
        print(f"IndexError: {e}, a={a}, b={b}")
    except TypeError as e:
        print(f"TypeError: {e}, a={a}, b={b}")
    return None

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        key = int(key)
        res = divider(key, value)
        if res is not None:
            result.append(res)
    except Exception as e:
        print(f"Помилка обробки елемента key={key}, value={value}: {e}")

print("Результат:", result)
