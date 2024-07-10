import json
import sqlite3
from player import Player
from world import World

class Game:
    def __init__(self):
        self.player = None
        self.world = None
        self.load_config()

    def load_config(self):
        with open('config.json', 'r') as config_file:
            self.config = json.load(config_file)

    def start_new_game(self, player_name):
        self.player = Player(player_name)
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

    def process_action(self, action):
        # Process the player's action and update the game state
        # This is where we'll implement the main game logic
        result = f"Processed action: {action}"
        self.save_game()
        return {"message": result, "game_state": self.get_game_state()}

    def get_game_state(self):
        # Return a dictionary representing the current game state
        return {
            "player": self.player.to_dict(),
            "world": self.world.to_dict()
        }
