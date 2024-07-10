class World:
    def __init__(self):
        self.locations = {}
        self.current_location = "starting_area"

    def to_dict(self):
        return {
            "current_location": self.current_location,
            "locations": self.locations
        }

    @classmethod
    def from_dict(cls, data):
        world = cls()
        world.current_location = data['current_location']
        world.locations = data['locations']
        return world
