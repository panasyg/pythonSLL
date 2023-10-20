class Calculator:
    def __init__(self):
        self.history = []

    def get_user_input(self):
        self.num1 = float(input("Введіть перше число: "))
        self.num2 = float(input("Введіть друге число: "))
        self.operator = input("Введіть оператор (+, -, *, /): ")

    def check_operator(self):
        if self.operator not in ['+', '-', '*', '/']:
            print("Введений недійсний оператор.")
            return False
        return True

    def perform_calculation(self):
        if self.operator == '/':
            if self.num2 == 0:
                raise ZeroDivisionError("Ділення на нуль неможливе.")
            self.result = self.num1 / self.num2
        elif self.operator == '+':
            self.result = self.num1 + self.num2
        elif self.operator == '-':
            self.result = self.num1 - self.num2
        elif self.operator == '*':
            self.result = self.num1 * self.num2

        self.rounded_result = round(self.result, 2)
        print(f"Результат: {self.rounded_result}")
        self.history.append((self.num1, self.num2, self.operator, self.rounded_result))

    def handle_errors(self):
        try:
            self.perform_calculation()
        except ValueError:
            print("Будь ласка, введіть дійсне число.")
        except ZeroDivisionError as e:
            print(f"Помилка: {e}")
        except Exception as e:
            print(f"Сталася помилка: {e}")

    def run_calculator(self):
        while True:
            self.get_user_input()
            if not self.check_operator():
                continue
            self.handle_errors()

            repeat = input("Бажаєте виконати ще одне обчислення? (так/ні): ")

            if repeat.lower() != 'так':
                print("До побачення!")
                break


if __name__ == '__main__':
    calc = Calculator()
    calc.run_calculator()
