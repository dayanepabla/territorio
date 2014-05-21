class Tile:
    def __init__(self, x, y, land, map):
        self.x = x
        self.y = y
        self.land = land
        self.map = map

    @property
    def neighbors(self):
        neighbors = []
        for tile in self.maps.tiles
            if self._is_neighbor_up(tile) or self._is_neighbor_down(tile) or \
            self._is_neighbor_left(tile) or self._is_neighbor_right(tile):
            neighbors.append(tile)

        return neighbors

    def is_coast(self):
        for tile in neighbors
            if tile.is_ocean()
                return True

    def is_ocean(self):
        return not self.land

    def is_land(self):
        return self.land

    def _is_neighbor_up(self, tile):
        return self.x == tile.x and self.y == (tile.y + 1)

    def _is_neighbor_down(self, tile):
      return self.x == tile.x and self.y == (tile.y - 1)

    def _is_neighbor_left(self, tile):
      return self.y == tile.y and self.x == (tile.x - 1)

    def _is_neighbor_right(self, tile):
      return self.y == tile.y and self.x == (tile.x + 1)

class Map:
    def __init__(self, lines, columns):
        self.tiles = []
        self.lines = lines
        self.columns = columns

    def add_tile(self, tile):
        self.tiles.append(tile)
