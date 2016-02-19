import sys

CellRadius    =  5
StoneRadius   = 4
BoardShade    = .8

def goPoint(x,y):
  return str((2*x+1)*CellRadius)+ ' ' + str((2*y+1)*CellRadius)

def getLines():
  L = sys.stdin.readlines()
  for k in range(len(L)):
    L[k] = L[k].rstrip()
  return L

def printHeader(rows, cols):
  print '%!PS-Adobe-3.0'
  print '%%BoundingBox: 0 0 ' + \
    str((1+cols)*2*CellRadius) + ' ' + \
    str((1+rows)*2*CellRadius)
  print '%%Pages: 0\n%%EndComments'
  print '/OriginX 0 def\n/OriginY 0 def'

L = getLines()
for line in L:
  for x in line.strip():
    print x,
  print ''

printHeader(2,2)
print goPoint(0,1)
print goPoint(0,0)
