import json
import sqlite3
from player import Player
from world import World
from dragon import Dragon

class Game:
    def __init__(self):
        self.player = None
        self.world = None
        self.load_config()

    def load_config(self):
        with open('config.json', 'r') as config_file:
            self.config = json.load(config_file)

    def start_new_game(self, player_name, character_class):
        self.player = Player(player_name, character_class)
        self.world = World()
        self.save_game()

    def load_game(self):
        conn = sqlite3.connect('game.db')
        c = conn.cursor()
        c.execute('SELECT * FROM game_state')
        game_state = c.fetchone()
        if game_state:
            self.player = Player.from_dict(json.loads(game_state[1]))
            self.world = World.from_dict(json.loads(game_state[2]))
        conn.close()

    def save_game(self):
        conn = sqlite3.connect('game.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS game_state
                     (id INTEGER PRIMARY KEY, player TEXT, world TEXT)''')
        c.execute('DELETE FROM game_state')
        c.execute('INSERT INTO game_state (player, world) VALUES (?, ?)',
                  (json.dumps(self.player.to_dict()), json.dumps(self.world.to_dict())))
        conn.commit()
        conn.close()

    def bond_with_dragon(self, dragon_name, dragon_color, dragon_breed):
        dragon = Dragon(dragon_name, dragon_color, dragon_breed)
        self.player.bond_with_dragon(dragon)
        self.save_game()
        return f"{self.player.name} has bonded with {dragon.name} the {dragon.color} {dragon.breed} dragon!"

    def process_action(self, action):
        if action.startswith("bond_with_dragon"):
            _, name, color, breed = action.split(":")
            return self.bond_with_dragon(name, color, breed)
        # Handle other actions here
        result = f"Processed action: {action}"
        self.save_game()
        return result

    def get_game_state(self):
        return {
            "player": self.player.to_dict(),
            "world": self.world.to_dict()
        }
