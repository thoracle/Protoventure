class World:
    def __init__(self):
        self.locations = {
            "starting_area": {
                "name": "Starting Area",
                "description": "A serene meadow surrounded by ancient trees. A path leads to the north.",
                "connected_locations": ["forest_entrance"]
            },
            "forest_entrance": {
                "name": "Forest Entrance",
                "description": "The edge of a dense forest. The path continues north, and you can return south to the starting area.",
                "connected_locations": ["starting_area", "deep_forest"]
            },
            "deep_forest": {
                "name": "Deep Forest",
                "description": "A dark and mysterious part of the forest. You can go south to return to the forest entrance.",
                "connected_locations": ["forest_entrance"]
            }
        }
        self.current_location = "starting_area"

    def move_to(self, location):
        if location in self.locations[self.current_location]["connected_locations"]:
            self.current_location = location
            return True
        return False

    def get_current_location_info(self):
        location = self.locations[self.current_location]
        return f"You are in the {location['name']}. {location['description']}"

    def get_available_moves(self):
        return self.locations[self.current_location]["connected_locations"]

    def to_dict(self):
        return {
            "locations": self.locations,
            "current_location": self.current_location
        }

    @classmethod
    def from_dict(cls, data):
        world = cls()
        world.locations = data['locations']
        world.current_location = data['current_location']
        return world
