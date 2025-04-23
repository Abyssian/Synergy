pets = {}

name = input("Введите имя питомца: ")
animal_type = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя владельца: ")

pets[name] = {
    "Вид питомца": animal_type,
    "Возраст питомца": age,
    "Имя владельца": owner
}

if 11 <= age % 100 <= 14:
    age_str = "лет"
elif age % 10 == 1:
    age_str = "год"
elif 2 <= age % 10 <= 4:
    age_str = "года"
else:
    age_str = "лет"

for pet_name in pets.keys():
    values = pets[pet_name]
    print(f'Это {values["Вид питомца"]} по кличке "{pet_name}". Возраст питомца: {values["Возраст питомца"]} {age_str}. Имя владельца: {values["Имя владельца"]}')