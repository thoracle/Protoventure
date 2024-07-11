import random
from dragon import Dragon
from item import Item

class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        self.health = 100
        self.max_health = 100
        self.mana = 50
        self.max_mana = 50
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.inventory = []
        self.max_inventory_size = 10
        self.dragon = None
        self.attack = 10
        self.defense = 5
        self.speed = 10

    # ... (other methods remain the same)

    def to_dict(self):
        return {
            "name": self.name,
            "character_class": self.character_class,
            "level": self.level,
            "experience": self.experience,
            "health": self.health,
            "max_health": self.max_health,
            "mana": self.mana,
            "max_mana": self.max_mana,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "intelligence": self.intelligence,
            "inventory": [item.to_dict() for item in self.inventory],
            "max_inventory_size": self.max_inventory_size,
            "dragon": self.dragon.to_dict() if self.dragon else None,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(data['name'], data['character_class'])
        player.level = data['level']
        player.experience = data['experience']
        player.health = data['health']
        player.max_health = data['max_health']
        player.mana = data['mana']
        player.max_mana = data['max_mana']
        player.strength = data['strength']
        player.dexterity = data['dexterity']
        player.intelligence = data['intelligence']
        player.inventory = [Item.from_dict(item_data) for item_data in data['inventory']]
        player.max_inventory_size = data['max_inventory_size']
        player.attack = data['attack']
        player.defense = data['defense']
        player.speed = data['speed']
        if data['dragon']:
            player.dragon = Dragon.from_dict(data['dragon'])
        return player
