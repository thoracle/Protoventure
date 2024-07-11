from enemy import Enemy

class World:
    def __init__(self):
        self.locations = {
            "starting_area": {
                "name": "Starting Area",
                "description": "A serene meadow surrounded by ancient trees. Paths lead to the north and east.",
                "connected_locations": ["forest_entrance", "village_outskirts"],
                "enemies": []
            },
            "forest_entrance": {
                "name": "Forest Entrance",
                "description": "The edge of a dense forest. The path continues north, and you can return south to the starting area.",
                "connected_locations": ["starting_area", "deep_forest"],
                "enemies": [Enemy("Wolf", 20, 5, 2, 8)]
            },
            "deep_forest": {
                "name": "Deep Forest",
                "description": "A dark and mysterious part of the forest. Paths lead south to the forest entrance and east to a hidden grove.",
                "connected_locations": ["forest_entrance", "hidden_grove"],
                "enemies": [Enemy("Bear", 40, 8, 4, 6)]
            },
            "hidden_grove": {
                "name": "Hidden Grove",
                "description": "A beautiful, secluded grove with a small stream. You can go west to the deep forest or north to the mountain pass.",
                "connected_locations": ["deep_forest", "mountain_pass"],
                "enemies": []
            },
            "mountain_pass": {
                "name": "Mountain Pass",
                "description": "A narrow pass through towering mountains. The pass continues north, and you can return south to the hidden grove.",
                "connected_locations": ["hidden_grove", "mountain_peak"],
                "enemies": [Enemy("Mountain Lion", 30, 7, 3, 10)]
            },
            "mountain_peak": {
                "name": "Mountain Peak",
                "description": "The summit of a tall mountain, offering breathtaking views. You can descend south to the mountain pass or east to the dragon's lair.",
                "connected_locations": ["mountain_pass", "dragon_lair"],
                "enemies": []
            },
            "dragon_lair": {
                "name": "Dragon's Lair",
                "description": "A vast cavern high in the mountains, home to ancient dragons. You can exit west to the mountain peak.",
                "connected_locations": ["mountain_peak"],
                "enemies": []
            },
            "village_outskirts": {
                "name": "Village Outskirts",
                "description": "The outskirts of a small village. You can enter the village to the east or return west to the starting area.",
                "connected_locations": ["starting_area", "village_center"],
                "enemies": []
            },
            "village_center": {
                "name": "Village Center",
                "description": "The bustling center of a small village. You can go west to the village outskirts or south to the marketplace.",
                "connected_locations": ["village_outskirts", "marketplace"],
                "enemies": []
            },
            "marketplace": {
                "name": "Marketplace",
                "description": "A lively marketplace filled with vendors and shoppers. You can return north to the village center.",
                "connected_locations": ["village_center"],
                "enemies": []
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

    def get_current_enemies(self):
        return self.locations[self.current_location]["enemies"]

    def remove_enemy(self, enemy):
        self.locations[self.current_location]["enemies"].remove(enemy)

    def get_all_locations(self):
        return list(self.locations.keys())

    def to_dict(self):
        serializable_locations = {}
        for loc_name, loc_data in self.locations.items():
            serializable_locations[loc_name] = {
                "name": loc_data["name"],
                "description": loc_data["description"],
                "connected_locations": loc_data["connected_locations"],
                "enemies": [enemy.to_dict() for enemy in loc_data["enemies"]]
            }
        return {
            "locations": serializable_locations,
            "current_location": self.current_location
        }

    @classmethod
    def from_dict(cls, data):
        world = cls()
        world.current_location = data['current_location']
        for loc_name, loc_data in data['locations'].items():
            world.locations[loc_name] = {
                "name": loc_data["name"],
                "description": loc_data["description"],
                "connected_locations": loc_data["connected_locations"],
                "enemies": [Enemy.from_dict(enemy_data) for enemy_data in loc_data["enemies"]]
            }
        return world
