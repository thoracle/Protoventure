import random

class Enemy:
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.health -= actual_damage
        return actual_damage

    def is_defeated(self):
        return self.health <= 0

    def attack_player(self):
        roll = random.randint(1, 20)
        if roll == 20:
            return ("critical", self.attack * 2)
        elif roll == 1:
            return ("miss", 0)
        else:
            return ("normal", self.attack)

    def to_dict(self):
        return {
            "name": self.name,
            "health": self.health,
            "max_health": self.max_health,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed
        }

    @classmethod
    def from_dict(cls, data):
        enemy = cls(data['name'], data['health'], data['attack'], data['defense'], data['speed'])
        enemy.max_health = data['max_health']
        return enemy
