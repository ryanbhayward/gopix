#TODO: fix makemove, then input sgf, then make sgfmoves, then done

#    input:  go sgf
#    output: go gdg 
from sys import stdin
import numpy as np
#import copy

"""
points on the board
"""

EMPTY, BLACK, WHITE, BORDER, POINT_CHARS = 0, 1, 2, -1, '.*o'

def opponent(color):
  return BLACK + WHITE - color

def coord_to_point(r, c, C):
  return (C+1) * (r+1) + c + 1

def point_to_alphanum(p, C):
  r, c = divmod(p, C+1)
  return COLUMNS[c-1] + str(r+1)

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
    for r in reversed(range(self.R)):
      this_row = ''
      for c in range(self.C):
        entry = self.brd[coord_to_point(r, c, self.C)]
        if entry == EMPTY:
          this_row += '   .'
        elif entry != BORDER:
          this_row += ' {:3d}'.format(entry)
      b += this_row + '\n'
    return b

  # brd entries are move numbers: parity gives stone color
  def color(self, j):
    entry = self.brd[j]
    print('j',j,'entry',entry)
    if entry == EMPTY:
      return EMPTY
    elif entry == BORDER:
      return BORDER
    elif 1 == entry%2:
      return BLACK
    else:
      return WHITE

  def tromp_taylor_score(self):
    bs, bt, ws, wt, empty_seen = 0, 0, 0, 0, set()
    for p in range(self.guarded_n):
      if   self.color(p) == BLACK:
        bs += 1
      elif self.color(p) == WHITE:
        ws += 1
      elif (self.brd[p] == EMPTY) and (p not in empty_seen):
        b_nbr, w_nbr = False, False
        empty_seen.add(p)
        empty_points = [p]
        territory = 1
        while (len(empty_points) > 0):
          q = empty_points.pop()
          for x in self.nbrs[q]:
            b_nbr |= (self.color(x) == BLACK)
            w_nbr |= (self.color(x) == WHITE)
            if self.brd[x] == EMPTY and x not in empty_seen:
              empty_seen.add(x)
              empty_points.append(x)
              territory += 1
        if   b_nbr and not w_nbr:
          bt += territory
        elif w_nbr and not b_nbr:
          wt += territory
    return bs, bt, ws, wt

  def captured(self, where, where_color):
  # return points in captured group containing where
  #   empty if group is not captured
    self.show_colors()
    print('captured where color', where, where_color)
    assert (self.color(self.brd[where]) == where_color)
    j, points, seen = 0, [where], {where}
    while (j < len(points)):
      p = points[j]
      for nbr in self.nbrs[p]:
        if self.brd[nbr] == EMPTY: # group has liberty, not captured
          return []
        print('self.brd[nbr]', self.brd[nbr])
        print('self.color(self.brd[nbr])',self.color(self.brd[nbr]))
        if (self.color(self.brd[nbr]) == where_color) and (nbr not in seen):
          print('append', nbr)
          points.append(nbr)
          seen.add(nbr)
      j += 1
    # no liberty found, so group is captured
    return points

  # write the movenum at the given location
  def make_sgf_move(self, where, movenum):
    assert self.brd[where] == EMPTY
    self.brd[where] = movenum
    print(self.brdstring())
    where_color = self.color(movenum)
    print('where, movenum, color', where, movenum, where_color)
    cap = []
    for nbr in self.nbrs[where]:
      print('nbr', nbr)
      if self.color(self.brd[nbr]) == opponent(where_color):
        cap += self.captured(nbr, opponent(where_color))
    if (len(cap) > 0):
      print('removing captured group at', point_to_alphanum(where, self.C))
      for j in cap:
        self.brd[j] = EMPTY
      return cap, True
    if self.captured(where, where_color):
      print('whoops, no liberty there: not allowed')
      self.brd[where] = EMPTY
      return cap, False
    return cap, True

def score_difference(score):
  return score[0] + score[1] - (score[2] + score[3])

def report(p):
  print(p.brdstring())
  with open('out.gdg', 'w', encoding="utf-8") as f:
    tts = p.tromp_taylor_score()
    sd = score_difference(tts)
    f.write('score ' + str(tts))
    if sd == 0:
      f.write(': black and white draw\n')
    elif sd > 0:
      f.write(': black wins by ' + str(sd) + ' \n')
    else:
      f.write(': white wins by ' + str(-sd) + ' \n')

p = Position(2,3)
report(p)
p.make_sgf_move(coord_to_point(1,2,3),1)
report(p)
p.make_sgf_move(coord_to_point(0,0,3),2)
report(p)
p.make_sgf_move(coord_to_point(0,1,3),4)
report(p)
p.make_sgf_move(coord_to_point(1,1,3),5)
report(p)
p.make_sgf_move(coord_to_point(0,2,3),6)
report(p)

parse_sgf()
