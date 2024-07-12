class Quest:
    def __init__(self, title, description, faction, objectives, reward_reputation):
        self.title = title
        self.description = description
        self.faction = faction
        self.objectives = objectives
        self.reward_reputation = reward_reputation
        self.completed = False

    def complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "faction": self.faction,
            "objectives": self.objectives,
            "reward_reputation": self.reward_reputation,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        quest = cls(data['title'], data['description'], data['faction'], data['objectives'], data['reward_reputation'])
        quest.completed = data['completed']
        return quest
