class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            print("Ошибка: скорость не может быть меньше 1")

    def count_moves(self, x2, y2):
        dx = abs(self.x - x2)
        dy = abs(self.y - y2)
        moves_x = dx // self.s
        if dx % self.s != 0:
            moves_x += 1
        moves_y = dy // self.s
        if dy % self.s != 0:
            moves_y += 1
        return moves_x + moves_y

    def info(self):
        print("Позиция:", self.x, self.y, "| скорость:", self.s)


turtle = Turtle()
command = ""

print("Команды: up, down, left, right, evolve, degrade, move, info, stop")

while command != "stop":
    command = input("Введите команду: ")

    if command == "up":
        turtle.go_up()
    elif command == "down":
        turtle.go_down()
    elif command == "left":
        turtle.go_left()
    elif command == "right":
        turtle.go_right()
    elif command == "evolve":
        turtle.evolve()
    elif command == "degrade":
        turtle.degrade()
    elif command == "info":
        turtle.info()
    elif command == "move":
        x2 = input("Введите x2: ")
        y2 = input("Введите y2: ")
        if x2.isdigit() or (x2[0] == '-' and x2[1:].isdigit()):
            if y2.isdigit() or (y2[0] == '-' and y2[1:].isdigit()):
                x2 = int(x2)
                y2 = int(y2)
                moves = turtle.count_moves(x2, y2)
                print("Шагов до точки:", moves)
            else:
                print("y2 должно быть целым числом")
        else:
            print("x2 должно быть целым числом")
    elif command == "stop":
        print("Завершение программы.")
    else:
        print("Неизвестная команда")
