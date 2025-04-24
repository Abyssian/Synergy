class Helicopter:
    def __init__(self):
        self.health = 3
        self.water_capacity = 1
        self.x = 0
        self.y = 0
        self.score = 0
        self.max_health = 3

    def move(self, direction, width, height):
        if direction == 'up' and self.y > 0:
            self.y -= 1
        elif direction == 'down' and self.y < height - 1:
            self.y += 1
        elif direction == 'left' and self.x > 0:
            self.x -= 1
        elif direction == 'right' and self.x < width - 1:
            self.x += 1

    def refill(self):
        self.water_capacity += 1

    def take_damage(self):
        self.health -= 1

    def heal(self):
        if self.health < self.max_health:
            self.health += 1
            return True
        return False

    def is_alive(self):
        return self.health > 0

    def increase_score(self, points):
        self.score += points
