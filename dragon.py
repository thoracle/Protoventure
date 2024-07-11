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
        self.is_ridden = False

    def mount(self):
        if self.energy >= 10:
            self.is_ridden = True
            self.energy -= 10
            return True
        return False

    def dismount(self):
        self.is_ridden = False

    def fly_to(self, location):
        if self.is_ridden and self.energy >= 20:
            self.energy -= 20
            return True
        return False

    def to_dict(self):
        return {
            "name": self.name,
            "color": self.color,
            "breed": self.breed,
            "level": self.level,
            "health": self.health,
            "energy": self.energy,
            "bond_level": self.bond_level,
            "abilities": self.abilities,
            "is_ridden": self.is_ridden
        }

    @classmethod
    def from_dict(cls, data):
        dragon = cls(data['name'], data['color'], data['breed'])
        dragon.level = data['level']
        dragon.health = data['health']
        dragon.energy = data['energy']
        dragon.bond_level = data['bond_level']
        dragon.abilities = data['abilities']
        dragon.is_ridden = data['is_ridden']
        return dragon
