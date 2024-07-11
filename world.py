class World:
    def __init__(self):
        self.locations = {
            "starting_area": {
                "name": "Starting Area",
                "description": "A serene meadow surrounded by ancient trees. Paths lead to the north and east.",
                "connected_locations": ["forest_entrance", "village_outskirts"]
            },
            "forest_entrance": {
                "name": "Forest Entrance",
                "description": "The edge of a dense forest. The path continues north, and you can return south to the starting area.",
                "connected_locations": ["starting_area", "deep_forest"]
            },
            "deep_forest": {
                "name": "Deep Forest",
                "description": "A dark and mysterious part of the forest. Paths lead south to the forest entrance and east to a hidden grove.",
                "connected_locations": ["forest_entrance", "hidden_grove"]
            },
            "hidden_grove": {
                "name": "Hidden Grove",
                "description": "A beautiful, secluded grove with a small stream. You can go west to the deep forest or north to the mountain pass.",
                "connected_locations": ["deep_forest", "mountain_pass"]
            },
            "mountain_pass": {
                "name": "Mountain Pass",
                "description": "A narrow pass through towering mountains. The pass continues north, and you can return south to the hidden grove.",
                "connected_locations": ["hidden_grove", "mountain_peak"]
            },
            "mountain_peak": {
                "name": "Mountain Peak",
                "description": "The summit of a tall mountain, offering breathtaking views. You can descend south to the mountain pass or east to the dragon's lair.",
                "connected_locations": ["mountain_pass", "dragon_lair"]
            },
            "dragon_lair": {
                "name": "Dragon's Lair",
                "description": "A vast cavern high in the mountains, home to ancient dragons. You can exit west to the mountain peak.",
                "connected_locations": ["mountain_peak"]
            },
            "village_outskirts": {
                "name": "Village Outskirts",
                "description": "The outskirts of a small village. You can enter the village to the east or return west to the starting area.",
                "connected_locations": ["starting_area", "village_center"]
            },
            "village_center": {
                "name": "Village Center",
                "description": "The bustling center of a small village. You can go west to the village outskirts or south to the marketplace.",
                "connected_locations": ["village_outskirts", "marketplace"]
            },
            "marketplace": {
                "name": "Marketplace",
                "description": "A lively marketplace filled with vendors and shoppers. You can return north to the village center.",
                "connected_locations": ["village_center"]
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
