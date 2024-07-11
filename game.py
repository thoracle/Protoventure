import json
import sqlite3
from player import Player
from world import World
from dragon import Dragon
from enemy import Enemy
import random

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

    def initiate_combat(self, enemy):
        combat_log = [f"You encounter a {enemy.name}!"]
        while not self.player.is_defeated() and not enemy.is_defeated():
            # Player's turn
            damage = self.player.attack_enemy()
            actual_damage = enemy.take_damage(damage)
            combat_log.append(f"You deal {actual_damage} damage to the {enemy.name}.")
            
            if enemy.is_defeated():
                combat_log.append(f"You have defeated the {enemy.name}!")
                self.world.remove_enemy(enemy)
                break
            
            # Enemy's turn
            damage = enemy.attack_player()
            actual_damage = self.player.take_damage(damage)
            combat_log.append(f"The {enemy.name} deals {actual_damage} damage to you.")
            
            if self.player.is_defeated():
                combat_log.append("You have been defeated!")
                break
        
        self.save_game()
        return "\n".join(combat_log)

    def mount_dragon(self):
        if self.player.dragon:
            if self.player.dragon.mount():
                return f"You have mounted {self.player.dragon.name}."
            else:
                return f"{self.player.dragon.name} is too tired to be ridden right now."
        else:
            return "You don't have a dragon to mount."

    def dismount_dragon(self):
        if self.player.dragon and self.player.dragon.is_ridden:
            self.player.dragon.dismount()
            return f"You have dismounted {self.player.dragon.name}."
        else:
            return "You are not currently riding a dragon."

    def fly_to_location(self, location):
        if self.player.dragon and self.player.dragon.is_ridden:
            if location in self.world.get_all_locations():
                if self.player.dragon.fly_to(location):
                    self.world.current_location = location
                    self.save_game()
                    return f"You have flown to {self.world.locations[location]['name']}. {self.world.locations[location]['description']}"
                else:
                    return f"{self.player.dragon.name} is too tired to fly right now."
            else:
                return "You can't fly to that location."
        else:
            return "You need to be riding a dragon to fly."

    def process_action(self, action):
        if action == "look":
            return self.world.get_current_location_info()
        elif action.startswith("move_to"):
            _, location = action.split(":")
            if self.world.move_to(location):
                self.save_game()
                enemies = self.world.get_current_enemies()
                if enemies:
                    return self.initiate_combat(random.choice(enemies))
                else:
                    return f"You have moved to {self.world.locations[location]['name']}. {self.world.locations[location]['description']}"
            else:
                return "You can't move there from your current location."
        elif action == "mount_dragon":
            return self.mount_dragon()
        elif action == "dismount_dragon":
            return self.dismount_dragon()
        elif action.startswith("fly_to"):
            _, location = action.split(":")
            return self.fly_to_location(location)
        elif action == "status":
            status = f"Health: {self.player.health}, Attack: {self.player.attack}, Defense: {self.player.defense}"
            if self.player.dragon:
                status += f"\nDragon: {self.player.dragon.name}, Energy: {self.player.dragon.energy}"
                if self.player.dragon.is_ridden:
                    status += " (mounted)"
            return status
        elif action.startswith("bond_with_dragon"):
            _, name, color, breed = action.split(":")
            return self.bond_with_dragon(name, color, breed)
        else:
            return f"Unknown action: {action}"

    def get_game_state(self):
        return {
        "player": {
            "name": self.player.name,
            "health": self.player.health,
            "attack": self.player.attack,
            "defense": self.player.defense,
            "dragon": {
                "name": self.player.dragon.name if self.player.dragon else None,
                "is_ridden": self.player.dragon.is_ridden if self.player.dragon else False,
                "energy": self.player.dragon.energy if self.player.dragon else 0
            } if self.player.dragon else None
        },
        "world": self.world.to_dict(),
        "current_location": self.world.get_current_location_info(),
        "available_moves": self.world.get_available_moves(),
        "all_locations": self.world.get_all_locations()
        }
