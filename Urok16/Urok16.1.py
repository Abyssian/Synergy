class Kassa:
    def __init__(self):
        self.money = 0

    def top_up(self, x):
        self.money += x
        print(f"Касса пополнена на {x} рублей. Текущий баланс: {self.money} рублей.")

    def count_1000(self):
        thousands = self.money // 1000
        print(f"В кассе {thousands} полных тысяч.")
        return thousands

    def take_away(self, x):
        if x > self.money:
            print("Недостаточно денег в кассе.")
        else:
            self.money -= x
            print(f"Из кассы забрали {x} рублей. Осталось: {self.money} рублей.")

if __name__ == "__main__":
    kasa = Kassa()
    while True:
        print("\nВыберите команду:")
        print("1 - Пополнить кассу")
        print("2 - Забрать из кассы")
        print("3 - Узнать количество тысяч")
        command = input("Введите номер команды: ")

        if command == "1":
            x = int(input("Введите сумму пополнения: "))
            kasa.top_up(x)

        elif command == "2":
            x = int(input("Введите сумму для снятия: "))
            kasa.take_away(x)

        elif command == "3":
            kasa.count_1000()

        else:
            print("Неверная команда, попробуйте снова.")
