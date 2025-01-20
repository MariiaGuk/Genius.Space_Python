import pygame
import time
pygame.mixer.init()
print("\nFIRST EXERCISE!")

'''**Завдання 1: Створення класу і об'єктів**

Створіть клас `Animal`, який представляє тварину. Кожний об'єкт класу `Animal` повинен мати наступні атрибути:

- `name` (ім'я тварини)
- `species` (вид тварини)
- `age` (вік тварини)

Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. Напишіть метод `make_sound()`,
який буде виводити звук, який виділяє тварина.

Створіть два об'єкта класу `Animal` з різними характеристиками та викличте їхні методи `make_sound()`.'''


def play_sound():
    time.sleep(0.5)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def print_attrs(self):
        print(f"\nName: {self.name}, Species: {self.species}, Age: {self.age}.")

    def make_sound(self):
        if self.species == "Dog" or self.species == "Cat" or self.species == "Bird":
            self.print_attrs()
            if self.species == "Dog":
                pygame.mixer.music.load("Woof.mp3")
            elif self.species == "Cat":
                pygame.mixer.music.load("Meow.mp3")
            elif self.species == "Bird":
                pygame.mixer.music.load("Chirp.mp3")
            play_sound()
            time.sleep(0.5)
        else:
            self.print_attrs()
            time.sleep(0.5)
            print("Choose another animal!")
            time.sleep(0.5)

animal1 = Animal("Jack", "Dog", 4)
animal2 = Animal("Anfisa", "Cat", 12)
animal3 = Animal("Felix", "Bird", 1)
animal4 = Animal("Pearl", "Fish", 2)

Animal.make_sound(animal1)
Animal.make_sound(animal2)
Animal.make_sound(animal3)
Animal.make_sound(animal4)