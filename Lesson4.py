print("СПИСКИ:")

'''1. **Робота із списками:**
Завдання: Створіть список чисел. Додайте до списку числа 10 і 20, видаліть число 10 і виведіть отриманий список.'''

print("ПЕРШЕ ЗАВДАННЯ!")
nums = [10, 25, 312, 42, 54]
print(nums, end=" --> ")
nums.append(10)
nums.append(20)
nums.reverse()
nums.remove(10)
nums.reverse()
print(nums)

print("\nДРУГЕ ЗАВДАННЯ!")
'''2. **Знаходження суми:**
Завдання: Створіть список чисел. Знайдіть та виведіть суму всіх чисел у списку.'''
nums = [10, 20, 30]
print(nums, end=" --> ")
sum = 0
for num in nums:
    print(num, end=" + ")
    sum += num
print("\b\b=", sum)

print("\nТРЕТЄ ЗАВДАННЯ!")
'''3. **Подвійні значення:**
Завдання: Створіть список чисел. Подвойте кожне число у списку та виведіть результат.'''
nums = [5, 10, 15, 20]
print(nums, end=" --> ")
for i in range(len(nums)):
    nums[i] *= nums[i]
print(nums)

print("\nКОРТЕЖІ:")
print("ПЕРШЕ ЗАВДАННЯ!")
'''1. **Робота із кортежами:**
Завдання: Створіть кортеж з трьох різних предметів, таких як ("яблуко", "банан", "апельсин").
Виведіть кожен елемент кортежу окремо.'''
fruits = ("яблуко", "банан", "апельсин")
print(fruits)
for i in fruits:
    print(i)

print("\nДРУГЕ ЗАВДАННЯ!")
'''2. **Об'єднання кортежів:**
Завдання: Створіть два кортежі з числами і об'єднайте їх у новий кортеж. Виведіть отриманий кортеж.'''
nums1 = (1,2,3,4,5)
nums2 = (6,7,8,9,0)
nums = nums1 + nums2
print(nums1, "+", nums2, "=", nums)

print("\nСЛОВНИКИ:")
print("ПЕРШЕ ЗАВДАННЯ!")
'''1. **Робота із словниками:**
Завдання: Створіть словник, що містить інформацію про вашого улюбленого спортсмена
(ім'я, вік, спорт, команда тощо).Виведіть цю інформацію на екран.'''
sport = {
    "Ім'я": "Анна Хниченкова",
    "Вік": 28,
    "Спорт": "Фігурне катання",
    "Дисципліна": "Одиночне катання",
    "Країна": "Україна",
    "Досягнення":["Чемпіонка України 2017 року", "Учасниця Олімпійських ігор 2018 року"]
}
for key, value in sport.items():
    if type(value) != list:
        print(f"{key}: {value}")
    else:
        print(key, end=": ")
        for i in range(len(value)):
            print(value[i], end=", ")
        print("\b\b")

print("\nДРУГЕ ЗАВДАННЯ!")
'''2. **Оновлення словника:**
Завдання: Створіть словник, що містить ваші улюблені книги (назва книги та рік видання).
Додайте до словника нову улюблену книгу та виведіть оновлений словник.'''
books = {
    "Полліанна": 1913,
    "Зелена миля": 1996,
}
print(books, end=" --> ")
books.update({"Гаррі Поттер і філософський камінь": 1997})
print(books)

print("\nТРЕТЄ ЗАВДАННЯ!")
'''3. **Пошук значення:**
Завдання: Створіть словник, що містить інформацію про країни та їх столиці.
Запитайте користувача про назву країни і виведіть столицю цієї країни (якщо така країна є у словнику).'''
capitals = {
    "Україна": "Київ",
    "США": "Вашингтон",
    "Німеччина": "Берлін",
    "Польща": "Варшава",
    "Велика Британія": "Лондон"
}
country = input("Введіть назву країни: ")
print(country, end=" --> ")
print(capitals.get(country, "Такої країни немає в словнику"))