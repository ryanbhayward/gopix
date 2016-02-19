# convert Go diagram to .eps file
import sys
CellRadius    = 10 
Blackchars = 'bBxX'
Whitechars = 'wWoO'
Emptychars = '.-_'

def getDiagram():
  L = sys.stdin.readlines()
  for k in range(len(L)): L[k] = L[k].strip()
  return L, len(L), len(L[0].split())

def printHead(rows, cols):
  print '%!PS-Adobe-3.0'
  print '%%BoundingBox: 0 0', cols*2*CellRadius, rows*2*CellRadius
  print '%%Pages: 0\n%%EndComments'
  print '/OriginX 0 def\n/OriginY 0 def'
  print '/Rows', rows, 'def\n/Cols', cols,'def'
  print '/CellDiameter ', 2*CellRadius

def printBody():
  f = open('gopic.epsbody','r')
  for line in f: print line,

def printTail(L,rows,cols):
  for  c in range(cols):
    for r in range(rows):
      s = L[r].split()[c]
      if s in Blackchars: print c+1, rows-r, 'B'
      elif s in Whitechars: print c+1, rows-r, 'W'
      elif s in Emptychars: pass
      else: 
        print c+1,rows-r, '('+s+')', len(s),
        if 1==(int(s)%2): print 'BL'
        else:             print 'WL'
  print 'showpage'

L, rows, cols = getDiagram()
printHead(rows,cols)
printBody()
printTail(L,rows,cols)
