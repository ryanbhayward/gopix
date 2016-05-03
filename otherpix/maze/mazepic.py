# convert maze diagram to .eps file
import sys
CellRadius    = 10 
MazeChars = ' _|'

def getDiagram():
  L = sys.stdin.readlines()
  rows, cols = len(L)-1, len(L[0])
  #print 'rows', rows, 'cols', cols
  for k in range(len(L)): L[k] = L[k].strip('\n')
  Floors, Walls = [], []
  for f in range(len(L)):
    floor, wall = '', ''
    for k in range(len(L[0])):
      if 0==(k%2): wall   += L[f][k]
      else:        floor  += L[f][k]
    Floors.append(floor)
    Walls.append(wall)
  rows, cols = len(L)-1, (len(L[0])-1)/2
  return L, Floors, Walls, rows, cols

def showDiagram(L):
  for j in L: print j
  print ''

def printHead(rows, cols):
  print '%!PS-Adobe-3.0'
  print '%%BoundingBox: 0 0', cols*2*CellRadius, rows*2*CellRadius
  print '%%Pages: 0\n%%EndComments'
  print '/OriginX 0 def\n/OriginY 0 def'
  print '/Rows', 1+rows, 'def\n/Cols', 1+cols,'def'

def printBody():
  f = open('mzpic.epsbody','r')
  for line in f: print line,

def printTail(F,W,rows,cols):
  for  c in range(cols):
    for r in range(rows+1):
      if F[r][c] == '_': 
        print c+1,rows+1-r, 1, 'H'
  for  c in range(cols+1):
    for r in range(rows+1):
      if W[r][c] == '|': 
        print c+1, rows+1-r, 1, 'V'
  print 'showpage'

L, F, W, rows, cols = getDiagram()
printHead(rows,cols)
printBody()
printTail(F,W,rows,cols)
#print ''
#showDiagram(L)
#showDiagram(F)
#showDiagram(W)
#print rows, cols
