#    input:  go sgf
#    output: go gdg 
from sys import stdin

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

parse_sgf()
