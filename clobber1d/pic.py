# convert Go diagram to .eps file
import sys
CellRadius    = 10
Blackchars = 'bBxX'
Whitechars = 'wWoO'
Emptychars = '.-_'
Diacritchars = 'v\\/'

def getDiagram():
  hasDia = False
  L = sys.stdin.readlines()
  for k in range(len(L)): 
    L[k] = ' '.join(L[k])
    L[k] = L[k].strip()
  for item in L:
    for c in item:
      if c in Diacritchars:
        hasDia = True
  return L, len(L), len(L[0].split()), hasDia

def printHead(rows, cols):
  print('%!PS-Adobe-3.0')
  print('%%BoundingBox: 0 0',(cols+.5)*2*CellRadius, (rows+.75)*2*CellRadius)
  print('%%Pages: 0\n%%EndComments')
  print('/OriginX 0 def\n/OriginY 0 def')
  print('/Rows', rows, 'def\n/Cols', cols,'def')
  print('/CellDiameter ', 2*CellRadius)

def printBody():
  f = open('body.eps','r')
  for line in f: print(line, end='')

def printTail(L, rows, cols, hasDia):
  start = 1 if hasDia else 0
  for r in range(start, rows):
    for c in range(cols):
      s = L[r].split()[c]
      if s in Blackchars: print(c+1, rows-r, 'B')
      elif s in Whitechars: print(c+1, rows-r, 'W')
      elif s in Emptychars: pass
      else: 
        print(c+1, rows-r, '('+s+')', len(s), end=' ')
        if 1==(int(s)%2): print('BL')
        else:             print('WL')
  if hasDia:
    for c in range(cols):
      s = L[0].split()[c]
      if s in Emptychars: pass
      elif s in Diacritchars: 
        if s=='/':
          print(c+1, 1, ' 1 Diacrit')
        elif s=='\\':
          print(c+1, 1, '-1 Diacrit')
        elif s=='v':
          print(c+1, 1, ' 1 Diacrit')
          print(c+1, 1, '-1 Diacrit')
  print('showpage')

L, rows, cols, hasDia = getDiagram()
printHead(1, cols) # linear clobber
printBody()
printTail(L, rows, cols, hasDia)
