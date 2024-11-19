import logging

logging.basicConfig(
    filename="calculation_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

class Calculation:
    def __init__(self):
        self.__operations = {
            "+": self.__add,
            "-": self.__subtract,
            "*": self.__multiply,
            "/": self.__divide
        }

    def __add(self, a, b):
        return a + b

    def __subtract(self, a, b):
        return a - b

    def __multiply(self, a, b):
        return a * b

    def __divide(self, a, b):
        if b == 0:
            raise ValueError("Ділення на нуль, не можливе")
        return a / b

    def __validate_and_convert(self, value):
        try:
            return float(value)
        except ValueError as e:
            logging.error(f"Помилка конвентарції: неможливе конвертувати '{value}' на число")
            raise ValueError(f"Неможливо конвертувати '{value}' на число") from e

    def __call__(self, a, b, operation):
        try:
            a = self.__validate_and_convert(a)
            b = self.__validate_and_convert(b)

            func = self.__operations.get(operation)
            if func is None:
                raise ValueError(f"Операція '{operation}' не підтримується")
            return func(a, b)
        except Exception as e:
            logging.error(f"Помилка розрахунку: {e}")
            raise


calc = Calculation()

try:
    print(calc(10, 5, "+"))
    print(calc(10, 5, "-"))
    print(calc(10, 5, "*"))
    print(calc(10, 5, "/"))
    print(calc(10, 0, "/"))
    print(calc("abc", 5, "+"))
except ValueError as e:
    print(f"Помилка: {e}")
