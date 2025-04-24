import random
import os

class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.burning = False

    def ignite(self):
        self.burning = True

    def extinguish(self):
        self.burning = False

class River:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Hospital:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def heal(self, helicopter):
        if helicopter.health < helicopter.max_health:
            helicopter.health += 1
            return True
        return False

def generate_field(width, height):
    field = [[' ' for _ in range(width)] for _ in range(height)]
    return field

def generate_objects(field, num_trees, num_rivers, num_hospitals):
    trees = []
    rivers = []
    hospitals = []

    for _ in range(num_trees):
        x, y = random.randint(0, len(field[0]) - 1), random.randint(0, len(field) - 1)
        trees.append(Tree(x, y))
        field[y][x] = 'T'

    for _ in range(num_rivers):
        x, y = random.randint(0, len(field[0]) - 1), random.randint(0, len(field) - 1)
        rivers.append(River(x, y))
        field[y][x] = '~'

    for _ in range(num_hospitals):
        x, y = random.randint(0, len(field[0]) - 1), random.randint(0, len(field) - 1)
        hospitals.append(Hospital(x, y))
        field[y][x] = 'H'

    return trees, rivers, hospitals

def print_field(field, helicopter, trees, rivers, hospitals, weather):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Weather: {weather}\nHealth: {helicopter.health}/{helicopter.max_health} | Score: {helicopter.score}")
    for y in range(len(field)):
        for x in range(len(field[0])):
            if (x, y) == (helicopter.x, helicopter.y):
                print('H', end=' ')
            elif any((tree.x == x and tree.y == y) for tree in trees):
                print('T' if not any(tree.x == x and tree.y == y and tree.burning for tree in trees) else 'F', end=' ')
            elif any((river.x == x and river.y == y) for river in rivers):
                print('~', end=' ')
            elif any((hospital.x == x and hospital.y == y) for hospital in hospitals):
                print('H', end=' ')
            else:
                print('.', end=' ')
        print()
