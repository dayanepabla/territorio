class Tile:
    def __init__(self, x, y, land):
        self.x = x
        self.y = y
        self.land = land

    def is_ocean(self):
        return not self.land

    def is_land(self):
        return self.land
