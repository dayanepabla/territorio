class Tile:
    def __init__(self, x, y, land, map):
        # x -> coluna / y -> linha
        self.x = x
        self.y = y
        self.land = land
        self.map = map

    def is_ocean(self):
        return not self.land

    def is_land(self):
        return self.land

    def _is_neighbor_up(self, tile):
        return self.x == tile.x && self.y == (tile.y + 1)

    def _is_neighbor_down(self, tile):
      return self.x == tile.x && self.y == (tile.y - 1)

    def _is_neighbor_left(self, tile):
      return self.y == tile.y && self.x == (tile.x - 1)

    def _is_neighbor_right(self, tile):
      return self.y == tile.y && self.x == (tile.x + 1)

class Map:
    def __init__(self, lines, columns):
        self.tiles = []
        self.lines = lines
        self.columns = columns




