# -*- coding: utf-8 -*-

class Tile:
    def __init__(self, x, y, land, map):
        self.x = x
        self.y = y
        self.land = land
        self.map = map

    @property
    def neighbors(self):
        neighbors = []
        for tile in self.map.tiles:
            if self._is_neighbor_up(tile) or self._is_neighbor_down(tile) or \
               self._is_neighbor_left(tile) or self._is_neighbor_right(tile):
                neighbors.append(tile)

        return neighbors

    def is_coast(self):
        if self.is_ocean():
            return False
        if self.map.is_boundary(self):
            return True

        for tile in self.neighbors:
            if tile.is_ocean():
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

    MIN_M = 1
    MAX_N = 1000

    def __init__(self, lines, columns):
        if lines < self.MIN_M and self.MAX_N > columns:
           raise Exception(u'M ou N não satisfazem as restrições')

        self.tiles = []
        self.lines = lines
        self.columns = columns

    def add_tile(self, tile):
        self.tiles.append(tile)

    def count_coast(self):
        coasts = 0
        for tile in self.tiles:
            if tile.is_coast():
                coasts += 1
        return coasts

    def is_boundary(self, tile):
        return tile.x == 0 or\
               tile.y == 0 or\
               tile.x == (self.columns - 1) or\
               tile.y == (self.lines - 1)

