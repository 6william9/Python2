import random


class Encryptor:
    def __init__(self, *numbers):
        self._numbers = numbers
        self._operation = random.choice(['+', '-', '*', '/'])

    def _calculate(self):
        result = self._numbers[0]
        for num in self._numbers[1:]:
            if self._operation == '+':
                result += num
            elif self._operation == '-':
                result -= num
            elif self._operation == '*':
                result *= num
            elif self._operation == '/' and num != 0:
                result /= num
        return result

    def __str__(self):
        return f'Result: {self._calculate():.2f} (Operation: {self._operation})'


enc = Encryptor(20, 5, 2)
print(enc)