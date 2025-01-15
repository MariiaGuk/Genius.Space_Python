# 1. Створити змінні таких типів: string, integer, float, bool, list, dict, tuple, None
print("FIRST EXERCISE!")
string_var = "String variable!"
print(type(string_var))

integer_var = 1
print(type(integer_var))

float_var = 1.5
print(type(float_var))

bool_var = True
print(type(bool_var))

list_var1 = [1, 2, 3]
list_var2 = ["One", "Two", "Three"]
print(type(list_var1), type(list_var2))

dict_var = {'University course': 1, "Name": "Mary"}
print(type(dict_var))

tuple_var = (1,2,3)
print(type(tuple_var))

None_var = None
print(type(None_var))

#2. Використати вивчені оператори та порівняти між собою числа, рядки, булеві значення, списки, словники і кортежі
# + Використано логічні оператори.
print("\nSECOND EXERCISE!")
num1 = 12
num2 = 4.5
print("Numbers:")
print("12 > 4.5? —", num1>num2)
print("12 <= 12? —", num1<=num1)
print("12 == 4.5? —", num1==num2)
print("12 != 4.5? —", num1!=num2)

string1 = "Name"
string2 = "name"
string3 = "Names1234567890"
print("\nStrings:")
print("Name == name? —", string1==string2)
print("Name < Names1234567890? —", string1<string3)
print("Name >= Names1234567890? —", string1>=string3)
sentence = "My name is Mary."
print("Is there \"Mary\" in the sentence \"My name is Mary.\"? —", "Mary" in sentence)
print("Is there \"Sofia\" in the sentence \"My name is Mary.\"? —", "Sofia" in sentence)
print("Is there no \"Sofia\" in the sentence \"My name is Mary.?\" —", "Sofia" not in sentence)
print("Combinations:")
print("Name == Name and Name != name? —", string1==string1 and string1!=string2)
print("12 == 4.5 and Letter \"M\" in the sentence \"My name is Mary.\"? —", num1==num2 and "M" in sentence)
print("12 == 4.5 or Letter \"M\" in the sentence \"My name is Mary.\"? —", num1==num2 or "M" in sentence)

check1 = True
check2 = False
print("\nBool:")
print("True == True? —", check1 == check1)
print("True == False? —", check1 == check2)
print("True and True? —", check1 and check1)
print("True and False? —", check1 and check2)
print("False and False? —", check2 and check2)
print("True or True? —", check1 or check1)
print("True or False? —", check1 or check2)
print("False or False? —", check2 or check2)

list1 = [1, "Two", 3]
list2 = ["One", 2, 3]
list3 = ["Two", 1, 3]
list4 = [1, 2]
list5 = [1, 2, 3]
print("\nLists:")
print("[1, \"Two\", 3] == [\"One\", 2, 3]? —", list1 == list2)
print("[1, \"Two\", 3] == [\"Two\", 1, 3]? —", list1 == list3)
print("[1, \"Two\", 3] == [1, \"Two\", 3]? —", list1 == list1)
print("[1, 2, 3] > [1, 2]? —", list5 > list4)
print("Is there \"Two\" in the list [1, \"Two\", 3]? —", "Two" in list1)
print("Is there no \"Two\" in the list [1, \"Two\", 3]? —", "Two" not in list1)

dict1 = {'University course': 1, "Name": "Mary"}
dict2 = {"Name": "Mary", 'Age': 18}
dict3 = {"a": 1, "b": 2}
dict4 = {"b": 2, "a": 1}
dict5 = {"a": 3, "b": 2}
print("\nDictionaries:")
print("{\'University course\': 1, \"Name\": \"Mary\"} != {\"Name\": \"Mary\", \'Age\': 18}? —", dict1 != dict2)
print("{\"a\": 1, \"b\": 2} == {\"b\": 2, \"a\": 1}?, —", dict3 == dict4)
print("{\"a\": 1, \"b\": 2} == {\"a\": 3, \"b\": 2}?, —", dict3 == dict5)
print("What value is in dictionary {\'University course\': 1, \"Name\": \"Mary\"} for the key \"Name\"? —", dict1["Name"])

tuple1 = (1, "Two", 3)
tuple2 = ('a', 'b', 'c')
tuple3 = ("Two", 1, 3)
tuple4 = (1, 2)
tuple5 = (1, 2, 3)
print("\nTuples:")
print("(1, \"Two\", 3) == (\"Two\", 1, 3)? —", tuple1 == tuple3)
print("('a', 'b', 'c') == ('a', 'b', 'c')? —", tuple2 == tuple2)
print("(1, 2, 3) > (1, 2)? —", tuple5 > tuple4)
print("Is there \"Two\" in the tuple (1, \"Two\", 3)? —", "Two" in tuple1)
print("Is there no \"Two\" in the tuple (1, \"Two\", 3)? —", "Two" not in tuple1)

print("\nTHIRD EXERCISE!")
'''3. Використати вивчені функції Python:
Робота з рядками:
 1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
 2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити
усі букви 'y' на '0' та 'i' на '1'.
 3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за
допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join
 4. Визначити довжину рядку string_join за допомогою функції len()
Робота зі списками:
 1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5
 2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()
 3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
 4. Визначити довжину списку list_append за допомогою функції len()
Робота зі словниками:
 1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані, які знаходяться в ключах car та where
 2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення
 3. За допомогою функції items() вивести на екран пари ключ - значення'''

print("Робота з рядками:\n1.")
num_str = 125
num_str = str(num_str)
print(type(num_str))

print("2.")
message = 'Hi, my name is Python!'
print(message, end=" → ")
message = message.replace('y', '0')
message = message.replace('i', '1')
print(message)

print("3.")
split_test = 'This is a split test'
print(split_test, end=" → ")
split_test = split_test.split(" ")
print(split_test, end=" → ")
string_join = " ".join(split_test)
print(string_join)

print(f"4.\n{len(string_join)}")

print("\nРобота зі списками:\n1.")
list_append = [1, 2, 3]
print(list_append, end=" → ")
list_append.append(4)
list_append.append(5)
print(list_append)

print("2.")
list_extend = [4, 5, 6]
print(list_extend, end=" → ")
list_extend.extend([7, 8, 9])
print(list_extend)

print(f"3.\n{list_extend.index(6)}")

print(f"4.\n{len(list_append)}")

print("\nРобота зі словниками:\n1.")
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(f"car = {dict_test['car']}, where = {dict_test['where']}")

print(f"2.\n{dict_test.keys()}\n{dict_test.values()}")

print(f"3.\n{dict_test.items()}")

print("\nFINISH!")