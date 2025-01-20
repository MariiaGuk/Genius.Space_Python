print("FIRST EXERCISE!")

'''**Завдання 1: Створення класу і об'єктів**

Створіть клас `Animal`, який представляє тварину. Кожний об'єкт класу `Animal` повинен мати наступні атрибути:

- `name` (ім'я тварини)
- `species` (вид тварини)
- `age` (вік тварини)

Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. Напишіть метод `make_sound()`,
який буде виводити звук, який виділяє тварина.

Створіть два об'єкта класу `Animal` з різними характеристиками та викличте їхні методи `make_sound()`.'''

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def print_attrs(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}."

    def make_sound(self):
        if self.species == "Dog" or self.species == "Cat" or self.species == "Bird":
            print(f"{self.print_attrs()}\n{self.species} says {sounds.get(self.species)}!\n")
        else:
            print(f"{self.print_attrs()}\nChoose another animal!\n")


animal1 = Animal("Jack", "Dog", 4)
animal2 = Animal("Anfisa", "Cat", 12)
animal3 = Animal("Felix", "Bird", 1)
animal4 = Animal("Pearl", "Fish", 2)
sounds = {"Dog": "woof", "Cat": "meow", "Bird": "chirp"}

Animal.make_sound(animal1)
Animal.make_sound(animal2)
Animal.make_sound(animal3)
Animal.make_sound(animal4)