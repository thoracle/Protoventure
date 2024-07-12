class NPC:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.dialogue = {}
        self.interaction_options = []

    def add_dialogue(self, key, text):
        self.dialogue[key] = text

    def add_interaction_option(self, option):
        self.interaction_options.append(option)

    def get_interaction_options(self):
        return self.interaction_options

    def get_dialogue(self, key):
        return self.dialogue.get(key, "I have nothing to say about that.")

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "dialogue": self.dialogue,
            "interaction_options": self.interaction_options
        }

    @classmethod
    def from_dict(cls, data):
        npc = cls(data['name'], data['description'])
        npc.dialogue = data['dialogue']
        npc.interaction_options = data['interaction_options']
        return npc
