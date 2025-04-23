word = input("Введите слово из маленьких латинских букв: ")

a = word.count('a')
e = word.count('e')
i = word.count('i')
o = word.count('o')
u = word.count('u')

# Подсчёт гласных и согласных
vowels = a + e + i + o + u
consonants = len(word) - vowels

print("Гласных:", vowels)
print("Согласных:", consonants)

# Отдельно по каждой гласной — как сказано в задаче
print("a:", a if a > 0 else False)
print("e:", e if e > 0 else False)
print("i:", i if i > 0 else False)
print("o:", o if o > 0 else False)
print("u:", u if u > 0 else False)