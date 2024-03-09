from enum import Enum

class Tiles(Enum):
    """
    Put all your tiles here. They must be numbered. It is best to put air as 0. It doesn't matter what number you put your tiles at, just that it is able to be called. They will then be called as Tiles.name, name being the tile you specify here
    """
    air = 0
    # Examples. Uncomment any of these out to test.
    carpet = 1
    # tile = 2
    # wood = 3

class Map2D:
    """
    A 2D map class with width (x) and height (y)
    Mostly created by GPT, but it screwed up in a dozen places so I rewrote things. It's a typical thing with GPT.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[Tiles.air for _ in range(height)] for _ in range(width)]
    
    # Gets a tile with x and y as parameters.
    def get_tile(self, x, y):
        if self._is_valid_coordinates(x, y):  # Checks if it is within bounds of the map.
            return self.tiles[x][y]
        else:
            raise ValueError("Invalid coordinates")
    
    # Sets the tile at a given set of coordinates.
    def set_tile(self, x, y, tile):
        if self._is_valid_coordinates(x, y):  # Checking again that it is within the range of the map.
            self.tiles[x][y] = tile
        else:
            raise ValueError("Invalid coordinates")
    
    # Fill the map with tiles with provided boundaries.
    def fill_range(self, min_x, max_x, min_y, max_y, tile):
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                self.set_tile(x, y, tile)
    
    # Checks if coordinates are within range of the map.
    def _is_valid_coordinates(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
