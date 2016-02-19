import sys

CellDiameter = 10

L = sys.stdin.readlines()
for k in range(len(L)):
  L[k] = L[k].rstrip()

def printHeader(rows, cols):
  print '%!PS-Adobe-3.0'
  print '%%BoundingBox: 0 0 ' + \
    str((1+cols)*CellDiameter) + ' ' + \
    str((1+rows)*CellDiameter)
  print '%%Pages: 0\n%%EndComments'

for line in L:
  for x in line.strip():
    print x,
  print ''

print L

printHeader(2,2)
