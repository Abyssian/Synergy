import pickle

def load_game(filename="savegame.pkl"):
    try:
        with open(filename, 'rb') as file:
            game_data = pickle.load(file)
        return game_data['helicopter'], game_data['trees'], game_data['rivers'], game_data['hospitals']
    except FileNotFoundError:
        print("No saved game found.")
        return None, None, None, None
