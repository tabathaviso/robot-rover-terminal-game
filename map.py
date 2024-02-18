import random

class Map:
    def __init__(self, width, height, rover):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.terrain_types = {
            'plain': { 'symbol': '.', 'friction': 1 },
            'rock': { 'symbol': '#', 'friction': 2 },
            'water': { 'symbol': '~', 'friction': 3 }
        }
        self.rover = rover  # reference to rover instance
        self.generate_map()

    def generate_map(self):
        terrain_choices = ['plain'] * 500 + ['rock'] * 50 + ['water'] * 1
        for y in range(self.height):
            for x in range(self.width):
                terrain = random.choice(terrain_choices)
                self.grid[y][x] = self.terrain_types[terrain]['symbol']
    
        rover_x, rover_y = self.rover.position
        self.grid[rover_y][rover_x] = self.rover.symbol
    

    def display_map(self):
        for row in self.grid:
            print(' '.join(row))

