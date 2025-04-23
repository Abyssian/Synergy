text = input("Введите строку: ")

if len(text) > 1000:
    print("Ошибка: строка превышает допустимую длину")
else:
    result = ""
    probel = False

    for char in text:
        if char == " ":
            if not probel:
                result += char
                probel = True
        else:
            result += char
            probel = False

    print(result)