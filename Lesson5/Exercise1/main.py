'''**Завдання 1: Робота з функціями**

Створіть Python-файл з ім'ям `calculator.py`. У цьому файлі створіть наступні функції:

1. `add(a, b)`: Приймає два числа `a` і `b` та повертає їхню суму.
2. `subtract(a, b)`: Приймає два числа `a` і `b` та повертає їхню різницю.
3. `multiply(a, b)`: Приймає два числа `a` і `b` та повертає їхній добуток.
4. `divide(a, b)`: Приймає два числа `a` і `b` і повертає результат ділення `a` на `b`.
Пам'ятайте про можливість ділення на нуль і додайте перевірку цього варіанту.

Після створення цих функцій, напишіть програму, яка імпортує модуль `calculator.py`
і використовує його функції для виконання обчислень. Попросіть користувача ввести два числа і операцію
(додавання, віднімання, множення або ділення), і виведіть результат обчислення.'''

import calculator

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
operation = input("Введіть операцію (додавання, віднімання, множення або ділення): ")

if operation in ["додавання", "+", "Додавання"]:
    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
elif operation in ["віднімання", "-", "Віднімання"]:
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
elif operation in ["множення", "*", "Множення"]:
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
elif operation in ["ділення", "/", "Ділення"]:
    temp = calculator.divide(num1, num2)
    if temp == None:
        print("Не можна ділити на нуль!")
    else:
        print(f"{num1} / {num2} = {temp}")
else:
    print("Помилка! Оператор не знайдено.")