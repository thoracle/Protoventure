class Faction:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.reputation = 0  # Reputation ranges from -100 (hated) to 100 (exalted)

    def adjust_reputation(self, amount):
        self.reputation = max(-100, min(100, self.reputation + amount))

    def get_standing(self):
        if self.reputation >= 75:
            return "Exalted"
        elif self.reputation >= 50:
            return "Honored"
        elif self.reputation >= 25:
            return "Friendly"
        elif self.reputation >= 0:
            return "Neutral"
        elif self.reputation >= -25:
            return "Unfriendly"
        elif self.reputation >= -50:
            return "Hostile"
        else:
            return "Hated"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "reputation": self.reputation
        }

    @classmethod
    def from_dict(cls, data):
        faction = cls(data['name'], data['description'])
        faction.reputation = data['reputation']
        return faction
