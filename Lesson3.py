print("CONDITIONAL CONSTRUCTIONS:")

'''1. **Перевірка паролю:**
Завдання: Напишіть програму, яка встановлює початковий пароль і перевіряє,
чи введений користувачем пароль співпадає з ним.
Якщо пароль дорівнює "password123", виведіть повідомлення "Ви увійшли в систему".
В іншому випадку виведіть повідомлення "Неправильний пароль".'''

print("FIRST EXERCISE!")
password = "password123"
entered = "password1234"
print(entered)
if entered == password:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

'''2. **Визначення днів тижня:**
Завдання: Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня.
Якщо номер дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку.'''

print("\nSECOND EXERCISE!")
day = 2
print(day)
if day == 1:
    print("Це Понеділок.")
elif day == 2:
    print("Це Вівторок.")
elif day == 3:
    print("Це Середа.")
elif day == 4:
    print("Це Четвер.")
elif day == 5:
    print("Це П'ятниця.")
elif day == 6:
    print("Це Субота.")
elif day == 7:
    print("Це Неділя.")
else:
    print(f"Помилка! Дня тижня з номером {day} не існує")

print("\nCYCLES:")

'''1. **Таблиця множення:**
Завдання: Виведіть таблицю множення для заданого числа від 1 до 10.'''

print("FIRST EXERCISE!")
num = 3
cnt = 1
while cnt<=10:
    print(f"{num} * {cnt} =", num * cnt)
    cnt+=1

'''2. **Сума чисел:**
Завдання: Визначте список чисел і обчисліть їх суму.'''

print("\nSECOND EXERCISE!")
nums = [1, 2, 3, 4, 5]
print(nums)
sumNums = 0
for num in nums:
    sumNums += num
print(sumNums)

'''3. **Факторіал числа:**
Завдання: Обчисліть факторіал заданого числа.'''

print("\nTHIRD EXERCISE!")
num = 5
factorial = 1
for i in range(num):
    factorial *= i+1
print(f"Факторіал числа !{num} = {factorial}")

'''4. **Парні числа:**
Завдання: Виведіть всі парні числа від 1 до 50.'''

print("\nFOURTH EXERCISE!\nПарні числа від 1 до 50:", end=" ")
for i in range(1, 51):
    if i%2==0:
        print(i, end=" ")
print()

'''5. **Пошук простих чисел:**
Завдання: Знайдіть всі прості числа в заданому діапазоні.'''

print("\nFIFTH EXERCISE!")
nums = [1,100]
print(f"Прості числа в діапазоні від {nums[0]} до {nums[1]}:", end=" ")
for i in range(nums[0], nums[1]+1):
    if i > 1:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            print(i, end=" ")
print()