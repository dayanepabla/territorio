from map import Map, Tile

def main():
  m = input('M: ')
  n = input('N: ')
  coasts = 0
  map = Map(m, n)

  for i in range(m):
    line = raw_input()
    for j, c in enumerate(line):
      if c == '.':
        tile = Tile(j, i, False, map)
      elif c == '#':
        tile = Tile(j, i, True, map)

      map.add_tile(tile)

  for tile in map.tiles:
    if tile.is_coast():
      coasts += 1

  print coasts
