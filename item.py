class Item:
    def __init__(self, name, description, item_type, effect_value):
        self.name = name
        self.description = description
        self.item_type = item_type  # e.g., "healing", "weapon", "armor"
        self.effect_value = effect_value

    def use(self, player):
        if self.item_type == "healing":
            player.health += self.effect_value
            return f"You used {self.name} and restored {self.effect_value} health."
        elif self.item_type == "weapon":
            player.attack += self.effect_value
            return f"You equipped {self.name} and increased your attack by {self.effect_value}."
        elif self.item_type == "armor":
            player.defense += self.effect_value
            return f"You equipped {self.name} and increased your defense by {self.effect_value}."

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "item_type": self.item_type,
            "effect_value": self.effect_value
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['description'], data['item_type'], data['effect_value'])
