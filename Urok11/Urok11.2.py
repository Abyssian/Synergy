import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_suffix(age):
    if 11 <= age % 100 <= 14:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    elif 2 <= age % 10 <= 4:
        return 'года'
    else:
        return 'лет'

def get_pet(ID):
    return pets.get(ID, False)

def pets_list():
    if not pets:
        print("База данных пуста.")
    else:
        for ID, info in pets.items():
            for name, data in info.items():
                suffix = get_suffix(data["Возраст питомца"])
                print(f'ID: {ID} — Это {data["Вид питомца"]} по кличке "{name}". Возраст питомца: {data["Возраст питомца"]} {suffix}. Имя владельца: {data["Имя владельца"]}')


def create():
    last = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last + 1
    name = input("Введите имя питомца: ")
    species = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")
    pets[new_id] = {
        name: {
            "Вид питомца": species,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print("Питомец добавлен!")

def read():
    ID = int(input("Введите ID питомца: "))
    pet = get_pet(ID)
    if pet:
        for name, info in pet.items():
            suffix = get_suffix(info['Возраст питомца'])
            print(f"Это {info['Вид питомца']} по кличке \"{name}\". Возраст питомца: {info['Возраст питомца']} {suffix}. Имя владельца: {info['Имя владельца']}")
    else:
        print("Питомец не найден.")

def update():
    ID = int(input("Введите ID питомца для обновления: "))
    if ID in pets:
        name = input("Введите новое имя питомца: ")
        species = input("Введите новый вид питомца: ")
        age = int(input("Введите новый возраст питомца: "))
        owner = input("Введите новое имя владельца: ")
        pets[ID] = {
            name: {
                "Вид питомца": species,
                "Возраст питомца": age,
                "Имя владельца": owner
            }
        }
        print("Информация обновлена.")
    else:
        print("Питомец с таким ID не найден.")

def delete():
    ID = int(input("Введите ID питомца для удаления: "))
    if ID in pets:
        del pets[ID]
        print("Питомец удален.")
    else:
        print("Питомец с таким ID не найден.")

while True:
    command = input("Введите команду (create, read, update, delete, list, stop): ")
    if command == 'stop':
        break
    elif command == 'create':
        create()
    elif command == 'read':
        read()
    elif command == 'update':
        update()
    elif command == 'delete':
        delete()
    elif command == 'list':
        pets_list()
    else:
        print("Неизвестная команда.")
