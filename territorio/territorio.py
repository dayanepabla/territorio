from map import Map, Tile

def main():
  m = input('M: ')
  n = input('N: ')
  map = Map(m, n)

  for i in range(m):
    line = raw_input()
    for j, c in enumerate(line):
      if c == '.':
        tile = Tile(j, i, False, map)
      elif c == '#':
        tile = Tile(j, i, True, map)

      map.add_tile(tile)


  print map.count_coast()

