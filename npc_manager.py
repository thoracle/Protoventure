from npc import NPC

class NPCManager:
    def __init__(self):
        self.npcs = {}

    def add_npc(self, location, npc):
        if location not in self.npcs:
            self.npcs[location] = []
        self.npcs[location].append(npc)

    def get_npcs_at_location(self, location):
        return self.npcs.get(location, [])

    def to_dict(self):
        return {loc: [npc.to_dict() for npc in npcs] for loc, npcs in self.npcs.items()}

    @classmethod
    def from_dict(cls, data):
        manager = cls()
        for loc, npc_list in data.items():
            manager.npcs[loc] = [NPC.from_dict(npc_data) for npc_data in npc_list]
        return manager
