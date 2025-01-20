print("SECOND EXERCISE!")

'''**Завдання 2: Робота з об'єктами**

Створіть клас `Rectangle`, який представляє прямокутник.
Кожен об'єкт класу `Rectangle` повинен мати наступні атрибути:

- `width` (ширина прямокутника)
- `height` (висота прямокутника)

Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. Напишіть метод `calculate_area()`,
який розраховує площу прямокутника (площа = ширина * висота).

Створіть два об'єкта класу `Rectangle` з різними розмірами та викличте їхні методи `calculate_area()`,
виведіть площу прямокутників на екран.'''

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        print(f"Width of the rectangle: {self.width}, Height of the rectangle: {self.height}."
              f"\nArea of the rectangle: {self.width * self.height}.\n")

rectangle1 = Rectangle(10,2)
rectangle2 = Rectangle(5,3)

Rectangle.calculate_area(rectangle1)
Rectangle.calculate_area(rectangle2)