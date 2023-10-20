history = []

while True:
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        operator = input("Введіть оператор (+, -, *, /): ")

        if operator not in ['+', '-', '*', '/']:
            print("Введений недійсний оператор.")
            continue

        if operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль неможливе.")
            result = num1 / num2
        elif operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2

        rounded_result = round(result, 2)
        print(f"Результат: {rounded_result}")

        history.append((num1, num2, operator, rounded_result))
        operation_number = 1

        repeat = input("Бажаєте виконати ще одне обчислення? (так/ні/історія): ")

        if repeat.lower() == 'ні':
            break
        elif repeat.lower() == 'історія':
            print("Історія обчислень:")
            for entry in history:
                print(f"{operation_number}. Операція: {entry[0]} {entry[2]} {entry[1]} = {entry[3]}")
                operation_number += 1
            operation_choice = int(input("Виберіть номер операції для відновлення результату: "))
            if 1 <= operation_choice <= len(history):
                selected_operation = history[operation_choice - 1]
                print(f"Ви вибрали операцію: {selected_operation[0]} {selected_operation[2]} {selected_operation[1]} = {selected_operation[3]}")
            else:
                print("Недійсний номер операції.")
            continue

    except ValueError:
        print("Будь ласка, введіть дійсне число.")
    except ZeroDivisionError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Сталася помилка: {e}")
