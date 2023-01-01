#    input:  go sgf
#    output: go gdg 
from sys import stdin

def parse_sgf():
  L = stdin.readlines()
  movenum = 1
  for k in L: 
    x = k.strip().split(';')
    for y in x:
      if len(y) >= 5: 
        if (y[0] == 'B') or (y[0] == 'W'):
          print('{:3d}'.format(movenum), y[0:5])
          movenum += 1

parse_sgf()
