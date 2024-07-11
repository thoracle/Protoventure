import random
from dragon import Dragon

class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        self.health = 100
        self.mana = 50
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.inventory = []
        self.dragon = None
        self.attack = 10
        self.defense = 5

    def bond_with_dragon(self, dragon):
        self.dragon = dragon

    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.health -= actual_damage
        return actual_damage

    def is_defeated(self):
        return self.health <= 0

    def attack_enemy(self):
        return random.randint(1, self.attack)

    def to_dict(self):
        return {
            "name": self.name,
            "character_class": self.character_class,
            "level": self.level,
            "experience": self.experience,
            "health": self.health,
            "mana": self.mana,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "intelligence": self.intelligence,
            "inventory": self.inventory,
            "dragon": self.dragon.to_dict() if self.dragon else None,
            "attack": self.attack,
            "defense": self.defense
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(data['name'], data['character_class'])
        player.level = data['level']
        player.experience = data['experience']
        player.health = data['health']
        player.mana = data['mana']
        player.strength = data['strength']
        player.dexterity = data['dexterity']
        player.intelligence = data['intelligence']
        player.inventory = data['inventory']
        player.attack = data['attack']
        player.defense = data['defense']
        if data['dragon']:
            player.dragon = Dragon.from_dict(data['dragon'])
        return player
