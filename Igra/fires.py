import random

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

def start_fires(trees, num_fires):
    for _ in range(num_fires):
        tree = random.choice(trees)
        tree.ignite()

def update_fire(trees):
    for tree in trees:
        if tree.burning:
            print(f"Tree at ({tree.x}, {tree.y}) is burning!")

def extinguish_fire(helicopter, trees):
    for tree in trees:
        if (tree.x == helicopter.x and tree.y == helicopter.y and tree.burning):
            tree.extinguish()
            helicopter.water_capacity -= 1
            helicopter.increase_score(1)
            print(f"Tree at ({tree.x}, {tree.y}) extinguished!")
            return True
    return False
