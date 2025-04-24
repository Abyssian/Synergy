class Shop:
    def __init__(self):
        self.water_capacity_upgrade_cost = 10

    def buy_upgrade(self, helicopter):
        if helicopter.score >= self.water_capacity_upgrade_cost:
            helicopter.score -= self.water_capacity_upgrade_cost
            helicopter.max_water += 1
            helicopter.water_capacity = helicopter.max_water
            return True
        else:
            return False
