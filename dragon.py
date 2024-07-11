class Dragon:
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed
        self.level = 1
        self.health = 100
        self.energy = 100
        self.bond_level = 0
        self.abilities = []

    def to_dict(self):
        return {
            "name": self.name,
            "color": self.color,
            "breed": self.breed,
            "level": self.level,
            "health": self.health,
            "energy": self.energy,
            "bond_level": self.bond_level,
            "abilities": self.abilities
        }

    @classmethod
    def from_dict(cls, data):
        dragon = cls(data['name'], data['color'], data['breed'])
        dragon.level = data['level']
        dragon.health = data['health']
        dragon.energy = data['energy']
        dragon.bond_level = data['bond_level']
        dragon.abilities = data['abilities']
        return dragon
