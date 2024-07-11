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

    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.health -= actual_damage
        return actual_damage

    def is_defeated(self):
        return self.health <= 0

    def attack_enemy(self):
        roll = random.randint(1, 20)
        if roll == 20:
            return ("critical", self.attack * 2)
        elif roll == 1:
            return ("miss", 0)
        else:
            return ("normal", self.attack)

    def special_ability(self):
        if self.character_class == "warrior":
            return ("power_strike", self.attack * 1.5)
        elif self.character_class == "mage":
            return ("fireball", self.intelligence * 2)
        elif self.character_class == "rogue":
            return ("backstab", self.dexterity * 1.5)

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= 100 * self.level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
        self.max_mana += 5
        self.mana = self.max_mana
        self.strength += 2
        self.dexterity += 2
        self.intelligence += 2
        self.attack += 2
        self.defense += 1
        self.speed += 1
        self.experience -= 100 * (self.level - 1)

    def bond_with_dragon(self, dragon):
        self.dragon = dragon

    def add_item(self, item):
        if len(self.inventory) < self.max_inventory_size:
            self.inventory.append(item)
            return True
        return False

    def remove_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                return item
        return None

    def use_item(self, item_name):
        item = self.remove_item(item_name)
        if item:
            return item.use(self)
        return "You don't have that item."

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
        player.attack = data['attack']
        player.defense = data['defense']
        player.speed = data['speed']
        if data['dragon']:
            player.dragon = Dragon.from_dict(data['dragon'])
        return player
