import pickle

def save_game(helicopter, trees, rivers, hospitals, filename="savegame.pkl"):
    game_data = {
        'helicopter': helicopter,
        'trees': trees,
        'rivers': rivers,
        'hospitals': hospitals
    }
    with open(filename, 'wb') as file:
        pickle.dump(game_data, file)
    print("Game saved.")
