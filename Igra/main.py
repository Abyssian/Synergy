import random
import time
import curses
from map import generate_field, generate_objects, Tree, River, Hospital
from helicopter import Helicopter
from shop import Shop
from exporter import save_game
from importer import load_game

def update_fire(trees):
    burning_trees = [tree for tree in trees if tree.burning]
    if len(burning_trees) < 2:
        non_burning_trees = [tree for tree in trees if not tree.burning]
        if non_burning_trees:
            random.choice(non_burning_trees).ignite()

def update_weather(last_weather_change_time):
    current_time = time.time()
    if current_time - last_weather_change_time >= 5:
        weather_conditions = ['Clear', 'Rainy', 'Thunderstorm']
        new_weather = random.choice(weather_conditions)
        last_weather_change_time = current_time
        return new_weather, last_weather_change_time
    return None, last_weather_change_time

def print_field(field, helicopter, trees, rivers, hospitals, weather, stdscr):
    stdscr.clear()

    stdscr.addstr(0, 0, f"Weather: {weather} | Health: {helicopter.health}/{helicopter.max_health} | Water: {helicopter.water_capacity}/{helicopter.max_water} | Score: {helicopter.score}")

    for y in range(len(field)):
        for x in range(len(field[0])):
            if (x, y) == (helicopter.x, helicopter.y):
                stdscr.addstr(y + 1, x * 2, 'X')
            elif any((tree.x == x and tree.y == y) for tree in trees):
                if any(tree.x == x and tree.y == y and tree.burning for tree in trees):
                    stdscr.addstr(y + 1, x * 2, 'F')
                else:
                    stdscr.addstr(y + 1, x * 2, 'T')
            elif any((river.x == x and river.y == y) for river in rivers):
                stdscr.addstr(y + 1, x * 2, '~')
            elif any((hospital.x == x and hospital.y == y) for hospital in hospitals):
                stdscr.addstr(y + 1, x * 2, 'H')
            else:
                stdscr.addstr(y + 1, x * 2, '.')

    stdscr.addstr(len(field) + 1, 0, "Control: WASD - move, E - extinguish, R - refill, H - hospital, B - shop, F5 - save, F7 - load, ESC - exit")
    stdscr.addstr(len(field) + 2, 0, "Для управления необходима включенная английская раскладка.")
    stdscr.refresh()

def open_shop(stdscr, helicopter, shop):
    stdscr.clear()
    stdscr.addstr(0, 0, "=== SHOP ===")
    stdscr.addstr(1, 0, f"1 - Увеличить бак для воды (цена: {shop.water_capacity_upgrade_cost} очков)")
    stdscr.addstr(2, 0, "B - Вернуться в игру")
    stdscr.refresh()

    while True:
        action = stdscr.getch()
        if action == ord('1'):
            if helicopter.score >= shop.water_capacity_upgrade_cost:
                helicopter.score -= shop.water_capacity_upgrade_cost
                helicopter.max_water += 1
                helicopter.water_capacity = helicopter.max_water
                stdscr.addstr(3, 0, f"Объём бака увеличен! Новый объём: {helicopter.water_capacity}")
                stdscr.refresh()
            else:
                stdscr.addstr(3, 0, "Недостаточно очков!          ")
                stdscr.refresh()
        elif action in [ord('b'), ord('B')]:
            break

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    width, height = 10, 10
    field = generate_field(width, height)

    helicopter = Helicopter()
    helicopter.max_water = 3
    helicopter.water_capacity = helicopter.max_water
    trees, rivers, hospitals = generate_objects(field, num_trees=8, num_rivers=8, num_hospitals=2)
    shop = Shop()

    burning_trees = random.sample(trees, 2)
    for tree in burning_trees:
        tree.ignite()

    last_weather_change_time = time.time()
    weather = update_weather(last_weather_change_time)[0]

    while helicopter.is_alive():
        update_fire(trees)
        print_field(field, helicopter, trees, rivers, hospitals, weather, stdscr)

        action = stdscr.getch()

        if action == ord('w'):
            helicopter.move('up', width, height)
        elif action == ord('s'):
            helicopter.move('down', width, height)
        elif action == ord('a'):
            helicopter.move('left', width, height)
        elif action == ord('d'):
            helicopter.move('right', width, height)
        elif action == ord('e'):
            if helicopter.water_capacity > 0:
                for tree in trees:
                    if tree.x == helicopter.x and tree.y == helicopter.y and tree.burning:
                        tree.extinguish()
                        helicopter.water_capacity -= 1
                        helicopter.increase_score(1)
                        stdscr.addstr(len(field) + 2, 0, f"Tree at ({tree.x}, {tree.y}) extinguished!       ")
                        break
                else:
                    stdscr.addstr(len(field) + 2, 0, "No fire to extinguish here!        ")
            else:
                stdscr.addstr(len(field) + 2, 0, "No water to extinguish fire!        ")
        elif action == ord('r'):
            if any(river.x == helicopter.x and river.y == helicopter.y for river in rivers):
                helicopter.water_capacity = helicopter.max_water
                stdscr.addstr(len(field) + 2, 0, "Water refilled!          ")
            else:
                stdscr.addstr(len(field) + 2, 0, "No river nearby!         ")
        elif action == ord('h'):
            if any(hospital.x == helicopter.x and hospital.y == helicopter.y for hospital in hospitals):
                if helicopter.health < helicopter.max_health:
                    helicopter.health += 1
                    stdscr.addstr(len(field) + 2, 0, "Healed at hospital!          ")
                else:
                    stdscr.addstr(len(field) + 2, 0, "Health is full!           ")
            else:
                stdscr.addstr(len(field) + 2, 0, "No hospital nearby!         ")
        elif action == ord('b'):
            open_shop(stdscr, helicopter, shop)
        elif action == curses.KEY_F5:
            save_game(helicopter, trees, rivers, hospitals)
            stdscr.addstr(len(field) + 2, 0, "Game saved!              ")
        elif action == curses.KEY_F7:
            h, t, r, hos = load_game()
            if h:
                helicopter, trees, rivers, hospitals = h, t, r, hos
                stdscr.addstr(len(field) + 2, 0, "Game loaded successfully!         ")
            else:
                stdscr.addstr(len(field) + 2, 0, "Failed to load game!         ")
        elif action == 27:
            break

        new_weather, last_weather_change_time = update_weather(last_weather_change_time)
        if new_weather:
            weather = new_weather

        time.sleep(0.1)

    stdscr.addstr(len(field) + 3, 0, "Game Over!")
    stdscr.refresh()
    time.sleep(2)

if __name__ == "__main__":
    curses.wrapper(main)
