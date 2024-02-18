# initializing robot rover terminal game
from map import Map
from rover import Rover

sojourner = Rover("Sojourner", "USA", 10.6, 45, 0.4, map)
spirit = Rover("Spirit", "USA", 185, 120, 5, map)
opportunity = Rover("Opportunity", "USA", 185, 120, 5, map)
curiosity = Rover("Curiosity", "USA", 899, 15, 30, map)
perseverance = Rover("Perseverance", "USA", 1025, 26.2, 152, map)
lunokhod = Rover("Lunokhod 1", "the Soviet Union", 756, 120, 2, map)
yutu = Rover("Yutu (Jade Rabbit)", "China", 120, 120, 200, map)
zhurong = Rover("Zhurong", "China", 240, 120, 200, map)
pragyan = Rover("Pragyan", "India", 27, 120, 5, map)
hayabusa = Rover("MINERVA-II-1 hopping", "Japan", 1.1, 100, 4, map)

def main():
    game_map = Map(50, 20, hayabusa)
    print(hayabusa)
    game_map.display_map()

if __name__ == "__main__":
    main()
    
