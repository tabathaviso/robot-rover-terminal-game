from map import Map

class Rover:
    def __init__(self, name, country, weight, fov, max_speed, map):
        self.name = name
        self.country = country
        self.size = 0
        self.weight = weight
        self.field_of_view = fov
        self.max_speed = max_speed
        self.turning_radius = 0.0
        self.energy_consumption_rate = 0.0
        self.speed = 1
        self.power = 100.0 
        self.position = (2, 2)
        self.map = map  # reference to the map instance
        self.symbol = 'R'

    def __repr__(self):
        return "You're driving " + self.country + "'s " + self.name + " rover."
    
    def move(self, direction):
        # 
        pass

    def check_terrain(self):
        # check what's in the next tile
        pass
