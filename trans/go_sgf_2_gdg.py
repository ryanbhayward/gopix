#    input:  go sgf
#    output: go gdg 
from sys import stdin
import numpy as np
import copy

"""
points on the board
"""

EMPTY, BLACK, WHITE, BORDER, POINT_CHARS = 0, 1, 2, 999, '.*o'

def opponent(color):
  return BLACK + WHITE - color

def coord_to_point(r, c, C):
  return (C+1) * (r+1) + c + 1

"""
parsing
"""

def parse_token(t): # return whether-move-is-valid and move
  if len(t) < 2:
    return False, ''
  if (t[0] == 'B' or t[0] == 'W') and t[1] == '[':
    if t[2] == ']': # B[] or W[] is pass move
      return True, t[0] + '[]  '
    else:
      assert(t[4] == ']')
      return True, t[0:5]
  return False, ''

def parse_sgf():
  L = stdin.readlines()
  movenum = 1
  for k in L: 
    x = k.strip().split(';')
    for y in x:
      t = parse_token(y)
      if t[0]:
        print('{:3d}'.format(movenum), t[1], end = ' ')
        movenum += 1
        if 1 == movenum % 10:
          print('')

"""
go position
"""

class Position: # go board with movenumber values:
                # odd/even movenum => black/white stone

  def __init__(self, r, c):
    self.R, self.C = r, c
    self.n, self.guarded_n = r * c,  (r+2) * (c+1)
    self.brd = np.full(self.guarded_n, BORDER, dtype = np.int16)
    for j in range(self.R):
      for k in range(self.C):
        self.brd[coord_to_point(j, k, self.C)] = EMPTY
    # init nbrs
    self.nbrs = []
    for point in range(self.guarded_n):
        if self.brd[point] == BORDER:
            self.nbrs.append([])
        else:
            nbs = []
            for where in [point-1, point+1, point+self.C+1, point-(self.C+1)]:
              if self.brd[where] != BORDER:
                  nbs.append(where)
            self.nbrs.append(nbs)

  def brdstring(self):
    b = ''
    for r in range(self.R):
      this_row = ''
      for c in range(self.C):
        entry = self.brd[coord_to_point(r, c, self.C)]
        if entry == EMPTY:
          this_row += '   .'
        elif entry != BORDER:
          this_row += ' {:3d}'.format(entry)
      b += this_row + '\n'
    return b

  def makemove(self, where, color):
    self.brd[where] = color
    cap = []
    for p in self.nbrs[where]:
      if self.brd[p] == opponent(color):
        cap += self.captured(p, opponent(color))
    if (len(cap)>0):
      print('removing captured group at', point_to_alphanum(where, self.C))
      for j in cap:
        self.brd[j] = EMPTY
      return cap, True
    if self.captured(where, color):
      print('whoops, no liberty there: not allowed')
      self.brd[where] = EMPTY
      return cap, False
    return cap, True

p = Position(2,3)
print(p.brdstring())
p.brd[coord_to_point(1,2,3)] = 113
print(p.brdstring())

#parse_sgf()
