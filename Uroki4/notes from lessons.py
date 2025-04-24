a = 5
b = 6 - 7
c = 4 * 5
# целочисленное деление где получится 1
d = 7 // 5 
# деление с остатком
e = 7 %  5
# степени
g = 2 ** 5
# переприсваивание(досчёт)
a += 10
a *= 10
print(a)
a = int(input())
b = int(input())
print(a * b)
a, b, c = map(int, input().split())
a = int(a)
print(a * 2)

a = int(input())
b = int(input())
c = a + b
print(c)

a, b = map(int, input().split())
c = a + b
print(c)

a, b = map(int, input().split())
c = (a + b) * 4
print(c)
#или
a, b = map(int, input().split())
d = a + b
c = d * 4
print(c)
#питон работает с большими числами

a = 10
b = 3
# /  - вещественное деление
# // - целочисленное
# %  - остаточное
print(a / b)

a = int(input())
b = int(input())

if a < b:
    print("less")
#если
else:
    #иначе
    if a == b:
        print("equal")
    else:
        print("greater")

a = int(input())

if a <= 2:
    print(1) 
elif a <= 4:
    print(2) # если не подходит первое условие
else:
    print(3) #если другие условия не подходят

cash = int(input())
cost = int(input())
cassa = int(input())

if cash >= cost and (cash - cost) <= cassa:
    print("Кола наша")
else:
    print("В этот раз на воде держимся")

cash = int(input()) #150
cost = int(input()) #125
cassa = int(input()) #50/1000

if (cash >= cost) and ((cash - cost) <= cassa):
    print("Кола наша")
else:
    print("В этот раз на воде держимся")

cash = int(input()) #200
cola = int(input()) #150
baykal = int(input()) #50
fanta = int(input()) #1000

if (cola <= cash) or (baykal <= cash) or (fanta <= cash):
    print("Купили")
else:
    print("Не повезло, не фортануло(")

cash = int(input()) #
mac = int(input()) #


if not (cash >= mac):
    print("Сорян")
else:
    print("Не повезло, не фортануло(")

#циклы while и for
a = int(input())
cnt = 0
while a >= 0:
    a -= 2
    cnt += 1
print(cnt)

#пример с клиентами и банками колы
clients = int(input())
cola = int(input())
cnt = 0

while(clients > 0) and (cola >=0):
    cans = int(input())
    clients -= 1
    if cola >= cans:
        cnt += 1
        cola -= cans

print(cnt)
#ход задачи данные: 5 клиентов 24 банки клиент первый клиент 10 банки второй 5 третий 15(не обслужен) четвертый 3 пятый 4(остаток 4 банки)
5 24
4 14
3 9
2 9
1 6
0 2

#python скажет что нельзя двигаться в шаг 0
for i in range(1, 11, 0):
    print(i)

# обратный ход, доходим до 1 за счёт a - 1
a = int(input())
b = int(input())
for i in range(b, a - 1, -1):
    print(i)

#с else конструкция не популярная, но нужен, чтобы знать что блок строго выполнится после while
a = 1
while a < 5:
    a += 1
    print(a)
 print('cheburek')
else:
    print('cheburek')

# согласно коду каждый работник с чётной зарплатой уволен
n = int(input())
for i in range(n): # 0 1 2 ... n -1
    salary = int(input())
    if salary % 2 == 0:
        print(i + 1, "fired") 

#индекс от нуля до 5 не включительно, с шагом 2
s1 = 'abcdefghijk'
print(s1[0:5:2])

#индекс от 5 до конца , с шагом 1
s1 = 'abcdefghijk'
print(s1[5::-1])

#индекс с шагом 2
tmp = [4, 3, 2 , 9, 7]
print(tmp[::2])

#.join соединяет
tmp = ['3', '4', '9', '157']
print(' + '.join(tmp))

#вариации строк
name = input()
print("Hello,", name)

name = input()
print(f'Hello, {name}')

name = input()
test = f'Hello, {name}'
print(test)

a1 = input()
a2 = input()
res = f'{a1} + {a2} = love'
print(res)

#верхний регистр(заглавные). lower нижний регистр
s1 = "akdl;kdlkd;ddd"
print(s1.upper())

#пример как выглядит табличные значения цифры и буквы
print(ord('a'))
print(chr(97))

#шифр Цезаря   z = 122
t = 'abzr'
for c in t:
    code = ord(c) + 3
    if code > 122:
        print(chr(97 + code - 122), end='')
    else:
        print(chr(code), end='')

a = [3, 4, 9, 1]
#3, 4, 9, 1   4 элемента у каждого свой индекс и идут с 0
#0  1  2  3
print(a[2])
#запрос индекса 2
# в python есть обратная индексация -1 -2 и тд


a = [3, 4, -150, 1, 2]
#3, 4, -150, 1, 2 
#0  1    2   3  4
#можно менять элементы
a[1] = 10
print(a[1])

#можно добавлять элементы
a.append(190)
print(a[-1])
#выводит весь массив
print(*a)
#длина массива в виде числа
print(len(a))
#добавляет массив после 3
a.insert(3, 99)
#удаляет последний элемент в массиве. a.pop(1) удалит 2 элемент.
a.pop()
#очищает массив
a.clear()
#разворачивает порядок в массиве
a.reverse()

a = [3, 4, -150, 1, 2, 4, 9, 4]
#считает сколько 4 в массиве (3)
print(a.count(4))

#берем 5 чисел 1 2 4 50 50 и не выводит 50
n = int(input())
tmp = list(map(int, input().split()))
res = []
for i in range(0, len(tmp)):
    if tmp[i] != 50:
        res.append(tmp[i])
print(res)
#создается список из 3 и их будет 10
a = [3 for i in range(10)]
#такой способ позволяет менять числа в таблице
a = [5]
b = a
a[0] = 3
print(b)

#множества

tmp = set()
#в множестве {} содержаться только уникальные объекты и поэтому будет {2, 3, 4}
tmp2 = {2, 3, 3, 4}
#добавит 7
tmp2.add(7)
#уберет 3
tmp2.discard(3)


n = int(input())
used = set()
for i in range(n):
    promo = input()
    if promo in used:  #выдает used если промокод уже был использован
        print("Sorry, already used")
    else:
        used.add(promo)
print(len(used)) #сколько было использовано


c1 = int(input())
cl1 = []
for i in range(c1):
    name = input()
    cl1.append(name)
uc1 = set(cl1)

c2 = int(input())
cl2 = []
for i in range (c2):
    name = input()
    cl2.append(name)
uc2 = set(cl2)
# 2 anna gena 3 gena masha gena отобразится {'masha', 'gena', 'anna'}
print(uc1.union(uc2))
# .intersection отобразит только тех кто есть в двух компаниях
print(uc1.intersection(uc2))

# frozenset не дает изменять число
s1 = frozenset()
s2 = s1
s2.add(7)

#Словари

bank = {'anton': 10, 'dima': 20, 'petya': 4, 'anton': 15} #будет указываться последняя переменная
bank['anton'] = 159 #можно изменять переменные
print(bank)


bank = dict()
n = int(input())

for i in range(n):
    req = input()
    if req == "create":
        k = input()
        bank[k] = 0
    elif req == "add":
        k = input()
        amount = int(input())
        if k in bank.keys():
            bank[k] += amount
        else:
            print("sorry, no such key")
    else:
        print("sorry, bad request")
print(bank)
# 4 create buratino create malvina add buratino 1000000 add pinoccio 5 sorry, no such key {'buratino': 1000000, 'malvina': 0}   не дали добавить деньги пиннокио из-за того что он отсутсвтует в банке

tmp = {'k1': 1, 'k2': 10, 'querty': 5}
print(tmp.keys()) # ключи
print(tmp.values()) # значения
print(tmp.items()) # общее 

for k in tmp.values():  # выдает значения
    print(k) 

tmp.pop('k1') # удаляет ключ k1 со значением

# Функции

def chet(a): # показывает четность
    if a % 2 == 0:
        return True
    a += 2
    print(a) # не будет True пока не будет соответствие


def chet(a): # показывает четность
    if a % 2 == 0:
        return True
    else:
        return False

print(chet(5)) # False
print(chet(4)) # True



def vis(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
        return True
    return False

y = int(input())
print(vis(y))



def nechet(n):
    return (n % 2 != 0)  #если нечетное True 

def res(l):
    for el in l:
        if nechet(el):
            print(el)  #выдает только нечетные

tmp = [1, 3, 4, 9, 2, 7]
res(tmp)


def new_year():
    print('Happy New Year!')

def birthday(name):
    print(f'Happy Birthday, {name}!')

def mart8():
    print('Happy 8th of March')

n = int(input())
for i in range(n):
    cm = input()
    if cm == 'new year':
        new_year()
    elif cm == 'birthday':
        name = input()
        birthday(name)
    elif cm == '8 march':
        mart8()
    else:
        print("wrong command")  # 5 => new year => Happy New Year! => birthday => Katya => Happy Birthday, Katya! => 8 march => Happy 8th of March => afjgkj => wrong command


        def new_year():
    print('Happy New Year!')

def birthday():
    print('Tell us a name of a person')
    name = input()
    print(f'Happy Birthday, {name}!')

def mart8():
    print('Happy 8th of March')

n = int(input())
for i in range(n):
    cm = input()
    if cm == 'new year':
        new_year()
    elif cm == 'birthday':
        birthday()
    elif cm == '8 march':
        mart8()
    else:
        print("wrong command")

        # Сортировка

        a = [4, 9, 0, 17, 23, 4, 1, 0]
n = len(a)

for i in range(n):
    for j in range(n - 1 -i):
        if a[j] > a[j + 1]:
            a[j], a [j + 1] = a[j + 1], a[j]
print(*a) #сортировка пузырьком


n = 5
sph = [12, 30, 97, 5, 6]
hs = [10, 120, 4, 8, 9]
res = []
for i in range(n):
    r = sph[i] * hs[i]
    res.append(r)
res.sort()
print(res) #пример сортировки

print(min(a, b, c, d)) #показывает минимальное значение есть max для большего

#Двумерные списки

tmp = [[1, 2, 3], [4, 5], [9, 8, 7]]

# 0 [1, 2, 3]  
# 1 [4, 5]
# 2 [9, 8, 7]

print(tmp[1][0]) # обращение к 2 индексу и 1 числу в индексе

tmp[1][0] = 9

print(tmp[1][0]) #присвоили 9

tmp = [[1, 2, 3], [4, 5], [9, 8, 7]]
tmp.append([6, 9, 2])
for i in tmp:
    print(*i)# выводит не списком а строками


n = int(input())
tmp = []
for i in range(n):
    a = list(map(int, input().split()))
    tmp.append(a)
print(tmp)  #ввод списков


def pl(t):
    for i in t:
        print(*i)

n = int(input())
tmp = []
for i in range(n):
    a = list(map(int, input().split()))
    tmp.append(a)

pl(tmp) # введенные данные выводятся строками без скобок

def pl(t):
    for i in t:
        print(*i)
tmp = [[1 for i in range(7)] for i in range(5)] #генерация списков
print(tmp)
pl(tmp) 


def pl(t):
    for i in t:
        print(*i)

x = int(input())
y = int(input())

house = [[0 for i in range(y)] for i in range(x)]
cnt = 1

for i in range(-1, -x - 1, -1):
    if i % 2 == 1:
        for j in range(y):
            house[i][j] = cnt
            cnt += 1
    else:
        for j in range(-1, -y -1, -1):
            house[i][j] = cnt
            cnt += 1
pl(house) # на каждом четном этаже, числа идут в обратную сторону по списку


#Рекурсия

def tmp(x):
    if x < 0: #рекурсия до 0
        return
    print(x)
    tmp(x - 1) #рекурсия

n = int(input())
tmp(n)


def fib(n):   #числа Фибоначчи
    if n < 0:
        return 0 
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    res = fib(n - 1) + fib(n - 2)
    return res

x = 6
print(fib(x))

#Объектно-ориентированное программирование

class Human(object):
    name = "Ivan"
    height = 175
    age = 25

default_human = Human()
default_human.name = "Anton" # можно менять значение
print(default_human.age) # вывод возраста



class Human(object):
    name = "Ivan"
    height = 175
    age = 25

    def __init__(self, n, h, a):  #функция-констуктор
        self.name = n
        self.height = h
        self.age = a
    
    def privet(self):
        print(f'My name is {self.name}, my age is {self.age}') 

    def get_older(self):
        self.age += 5

    def goodbye(self):
        print('Goodbye')

h1 = Human('Anton', 120, 12)
h2 = Human('Dima', 190, 23)

print(h1.age)
h1.get_older() # выдаст возраст старше на 5
print(h1.age)
h1.goodbye()


#Классы и объекты

class Car(object):
    brand = 'Mazda'
    max_speed = 100
    color = 'black'
    
    def __init__(self, b, ms):
        self.brand = b
        self.max_speed = ms

    def upgrade(self):
        self.max_speed += 25

nissan = Car('Nissan', 190)
print(nissan.brand, nissan.max_speed)



class Car(object):
    brand = 'Mazda'
    max_speed = 100
    color = 'black'
    
    def __init__(self, b, ms):
        self.brand = b
        self.max_speed = ms

    def upgrade(self):
        self.max_speed += 25

class Truck(Car):
    max_weight = 10

    def add(self):
        self.max_weight += 10

mazda = Car('Mazda', 200)
print(mazda.max_speed)

gazel = Truck('Gazel', 60)
gazel.upgrade()
gazel.add()
print(gazel.max_weight)



class Car(object):
    brand = 'Mazda'
    max_speed = 100
    color = 'black'
    
    def __init__(self, b, ms):
        self.brand = b
        self.max_speed = ms

    def upgrade(self):
        self.max_speed += 25

class Truck(Car):
    max_weight = 10

    def __init__(self, b, ms, mw):
        super().__init__(b, ms)
        self.max_weight = mw

    def add(self):
        self.max_weight += 10

mazda = Car('Mazda', 200)
print(mazda.max_speed)

gazel = Truck('Gazel', 60, 120)

print(gazel.brand, gazel.color, gazel.max_speed, gazel.max_weight)


class Car(object):
    brand = 'Mazda'
    max_speed = 100
    color = 'black'
    __password = 1234
    
    def __init__(self, b, ms):
        self.brand = b
        self.max_speed = ms

    def __update_password(self):
        self.__password = 234


    def upgrade(self):
        self.max_speed += 25
        self.__update_password()

    def get_password(self):
        return self.__password

class Truck(Car):
    max_weight = 10

    def __init__(self, b, ms, mw):
        super().__init__(b, ms)
        self.max_weight = mw

    def add(self):
        self.max_weight += 10

mazda = Car('Mazda', 200)
print(mazda.max_speed)

tmp = Car('Mazda', 3)
print(tmp.get_password())

tmp.upgrade()
print(tmp.get_password())

gazel = Truck('Gazel', 60, 120)

print(gazel.brand, gazel.color, gazel.max_speed, gazel.max_weight)

#Исключения

try:
    print(45 // 0)
except ZeroDivisionError:
    print('Ну не надо так, на ноль делить низя')
print('TEST')


t = [1, 2, 5]
try:
    print(t[10])
    print(45 // 0)
except ZeroDivisionError:  #в блоке try, при ошибке, try ищет первую подходящую ошибку и выдаёт её
    print('Ну не надо так, на ноль делить низя')
except IndexError:
    print('Тут ничего нет, попробуйте другой индекс')
except Exception: #Общее исключение
    print('абракадабра')
finally:
    print('finish') # В любом случае выдает finish
print('TEST')

# О-нотация

n = int(input())
m = int(input())
a = 3
for i in range(n):
    for j in range(n):
        a += 1

for k in range(100):
    for j in range(m):
        a += 1

O(n ^ 2 + m)