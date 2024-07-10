class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.inventory = []

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "experience": self.experience,
            "inventory": self.inventory
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(data['name'])
        player.level = data['level']
        player.experience = data['experience']
        player.inventory = data['inventory']
        return player
