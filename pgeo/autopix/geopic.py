#!/usr/bin/env python3

# geo: Schensted's geodesic-Y board, base 2 to 5
# start with cell centers
# RBH 2020
# TODO: round edge ends in dual graph, maybe with a perimeter of edges?

import sys
from math import sqrt, sin, cos, pi

root3 = 1.73205080757
rt3d2 = .86602540378

def getDiagram():
  L = sys.stdin.readlines()
  return L

L = getDiagram()
line0 = L.pop(0).split()
assert(line0[0] == "base")
base = int(line0[1])
#base    =  5    # CellsPerBase = [0, 1, 3, 9, 18, 30]

scale   = 15.0  # points, for postscript pic
stretch = 1.2   # smaller the value, the higher the geodesic pov
pad     = 5.0   # surrounding blank border for postscipt pic
Layer1  = ((0.0,1.0),(rt3d2, -.5),(-rt3d2, -.5))  # layer 1, diameter 1.0
m = scale*(1.0 + (base-1.5)*stretch)
mmx = (-rt3d2*m, (1.0-root3)*m, rt3d2*m, m)

def myround(r): return f'{round(1.0*r,3):10.5}'
def mypoint(p): return '[' + myround(p[0]) + myround(p[1]) + ']'
def radians(j): return 2*pi*j
def mysin(a): return sin(radians(a))
def mycos(a): return cos(radians(a))
def sumpoints(p1, p2): return [sum(x) for x in zip(p1, p2)]
def mulpoint(m, p): return [m*x for x in p]
def g(p, a1): return sumpoints(p, mulpoint(root3, [mysin(a1), mycos(a1)]))
def layerRadius(layer, gap): 
  if layer==0: return 0.0
  else: return 1.0 + (layer-1)*gap

def getMinMax(A):
  mmx = [0.0, 0.0, 0.0, 0.0]
  for pt in A:
    mmx[0] = min(mmx[0],pt[0])
    mmx[1] = min(mmx[1],pt[1])
    mmx[2] = max(mmx[2],pt[0])
    mmx[3] = max(mmx[3],pt[1])
  return mmx

def geoLayer(k, dia): # kth layer (so 3k nodes), diameter dia
  ndx = [2,0,1]
  if k==0:   return [0.0, 0.0] 
  elif k==1: return [ mulpoint(dia, Layer1[j]) for j in range(3)] 
  else:
    L = []
    for t in range(3):
      L +=  [ mulpoint(dia, g(Layer1[ndx[t]], 
              (1.0+t*4.0)/12 +j/(k*6.0))) for j in range(k) ]
    return L

def cellCenters(b, s, stch): # nodes in geo base b board, scale s, stretch 
  N = []
  for layer in range(1,b): 
    N += geoLayer(layer, s*layerRadius(layer,stch))
  return N

# this would be a better way to do things, maybe later
#def cellCorners(b, s, stch):
#  R = [(0.0, 0.0)]
#  R += geoLayer(b, s*layerRadius(2,.67*stch))
#  return R

def pretty(C, n):
  for k in range(n):
    print('[' + myround(C[k][0]) + myround(C[k][1]) + ']')

DE = [
  [[0,1],[0,2],[1,2]],  #layer 1
  [[0,3],[0,4],[0,8],[1,4],[1,5],[1,6],[2,6],[2,7],
   [2,8],[3,4],[3,8],[4,5],[5,6],[6,7],[7,8]], #layer 2
  [[3,9],[3,10],[3,17],[4,10],[4,11],[5,11],[5,12],[5,13],[6,13],[6,14],
   [7,14],[7,15],[7,16],[8,16],[8,17],[9,10],[9,17],[10,11],[11,12],
   [12,13],[13,14],[14,15],[15,16],[16,17]], #layer 3
  [[9,18],[9,19],[9,29],[10,19],[10,20],[11,20],[11,21],
   [12,21],[12,22],[12,23],[13,23],[13,24],[14,24],[14,25],
   [15,25],[15,26],[15,27],[16,27],[16,28],[17,28],[17,29],
   [18,19],[18,29],[19,20],[20,21],[21,22],[22,23],[23,24],     
   [24,25],[25,26],[26,27],[27,28],[28,29]] ] #terminal layer 4

Trips = [
  [[0,1,2]],  #layer 1
  [[0,3,4],[0,1,4],[1,4,5],[1,5,6],[1,2,6],[2,6,7],[2,7,8],[0,2,8],[0,3,8]],#2
  [[3,9,10],[3,4,10],[4,10,11],[4,5,11],[5,11,12],[5,12,13],[5,6,13],[6,13,14],
   [6,7,14],[7,14,15],[7,15,16],[7,8,16],[8,16,17],[3,8,17],[3,9,17]], #layer3
  [[9,18,19],[9,10,19],[10,19,20],[10,11,20],[11,20,21],[11,12,21],[12,21,22],
   [12,22,23],[12,13,23],[13,23,24],[13,14,24],[14,24,25],[14,15,25],
   [15,25,26],[15,26,27],[15,16,27],[16,27,28],[16,17,28],[17,28,29],
   [9,17,29],[9,18,29]]] #layer 4

# for each cell, the corners of its boundary
Poly = [
  [[0,8,9,1,2], [0,2,3,4,5], [0,5,6,7,8], 
  [1,9,21,10,11], [1,2,3,13,12,11], [3,4,15,14,13],
  [4,5,6,17,16,15], [6,7,19,18,17], [7,8,9,21,20,19]],   #base 3
  [[0,8,9,1,2], [0,2,3,4,5], [0,5,6,7,8],
  [1,9,23,24,10,11],[1,2,3,13,12,11],[3,4,16,15,14,13],
  [4,5,6,18,17,16],[6,7,21,20,19,18],[7,8,9,23,22,21],
  [10,24,42,25,26],[10,11,12,28,27,26],[12,13,14,30,29,28],
  [14,15,32,31,30],[15,16,17,34,33,32],[17,18,19,36,35,34],
  [19,20,38,37,36],[20,21,22,40,39,38],[22,23,24,42,41,40]], #b4
  [[0,8,9,1,2], [0,2,3,4,5], [0,5,6,7,8],
  [1,9,23,24,10,11],[1,2,3,13,12,11],[3,4,16,15,14,13],
  [4,5,6,18,17,16],[6,7,21,20,19,18],[7,8,9,23,22,21],
  [10,24,44,45,25,26],[10,11,12,28,27,26],[12,13,14,30,29,28],
  [14,15,33,32,31,30],[15,16,17,35,34,33],[17,18,19,37,36,35],
  [19,20,40,39,38,37],[20,21,22,42,41,40],[22,23,24,44,43,42],
  [25,47,46,69,45],[25,26,27,49,48,47],[27,28,29,51,50,49],[29,30,31,53,52,51],
  [31,32,55,54,53],[32,33,34,57,56,55],[34,35,36,59,58,57],[36,37,38,61,60,59],
  [38,39,63,62,61],[39,40,41,65,64,63],[41,42,43,67,66,65],[43,44,45,69,68,67]] #b5
  ]

def setDualEdges(b):
  edges = DE[0]
  for j in range(b-2):
    edges += DE[j+1]
  return edges

def setTriples(b):
  tr = Trips[0]
  for j in range(b-2):
    tr += Trips[j+1]
  return tr

CorEd = (  # corner edges form cell boundaries
  ((0,2),(0,5),(0,8)), # layer 0-1
  ((1,2),(1,9),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9)), #1-1
  ((1,11),(3,13),(4,16),(6,18),(7,21),(9,23)),  #1-2
  ((10,11),(11,12),(12,13),(13,14),(14,15),(15,16),(16,17),(17,18),(18,19),
   (19,20),(20,21),(21,22),(22,23),(23,24),(10,24)), #2-2
  ((10,26),(12,28),(14,30),(15,33),(17,35),(19,37),(20,40),(22,42),(24,44)),#2-3
  ((25,26),(26,27),(27,28),(28,29),(29,30),(30,31),(31,32), 
  (32,33),(33,34),(34,35),(35,36),(36,37),(37,38),(38,39),(39,40),
  (40,41),(41,42),(42,43),(43,44),(44,45),(25,45))) #3-3

PerimEd = (     # edges to perimeter nodes
  ((0,2),(0,4),(0,6)), # when base is 2, perimeter nodes 1-6
  ((1,11),(3,13),(4,15),(6,17),(7,19),(9,21)), #base 3, p-nodes 10-21
  ((10,26),(12,28),(14,30),(15,32),(17,34),(19,36),(20,38),
   (22,40),(24,42)), #base 4, p-nodes 25-36
  ((25,47),(27,49),(29,51),(31,53),(32,55),(34,57),(36,59),(38,61),
   (39,63),(41,65),(43,67),(45,69))) #base 5, p-nodes 46-60

# REPEATING SOME CORNERS TO MAKE CENTROID MORE CENTRAL
CellCors = [ # corners of each cell
  [(0,1,2,6), (0,2,3,4), (0,4,5,6)],   # base 2
  [(0,2,1,9,8),(0,2,3,4,5),(0,5,6,7,8),(1,9,21,10,11),(1,2,3,13,12,11), #base 3
   (3,4,15,14,13),(4,5,6,17,16,15),(6,7,19,18,17),(7,8,9,21,20,19)],
  [(0,0,1,9),(0,0,3,4),(0,0,6,7),        #base 4
   (1,9,24,10),(2,12),(3,4,14,15),(5,17),(6,7,19,20),(8,22),
   (10,10,24,24,25,25,25),(11,27),(13,29),
   (14,14,15,15,31,31,31),(16,33),(18,35),
   (19,19,20,20,37,37,37),(21,39),(23,41)],
  [(0,0,1,9),(0,0,3,4),(0,0,6,7),     #base 5
   (1,9,10,24),(2,12),(3,4,14,15),(5,17),(6,7,19,20),(8,22),
   (10,24,25,45),(11,27),(13,29),
   (14,15,31,32),(16,34),(18,36),
   (19,20,38,39),(21,41),(23,43),
   (25,25,45,45,46,46,46),(26,48),(28,50),(30,52),
   (31,31,32,32,54,54,54),(33,56),(35,58),(37,60),
   (38,38,39,39,62,62,62),(40,64),(42,66),(44,68)]
  ]

def setCornerEdges(b):
  if b==2: 
    ced = PerimEd[0]
  elif b==3:
    ced = CorEd[0]+CorEd[1]+PerimEd[1]
  elif b==4:
    ced = CorEd[0]+CorEd[1]+CorEd[2]+CorEd[3]+PerimEd[2]
  elif b==5:
    ced = CorEd[0]+CorEd[1]+CorEd[2]+CorEd[3]+CorEd[4]+CorEd[5]+PerimEd[3]
  return ced

def centroid(V, Ndx):
  ttl = [0.0, 0.0]
  n = len(Ndx)
  for j in range(2):
    for k in range(n):
      ttl[j]+= V[Ndx[k]][j]
  return [s / (1.0*n) for s in ttl]

def meetpoint(Cens, tp): # set meet points of cell triples
  A = []
  for j in range(2):
    A.append((Cens[tp[0]][j] + Cens[tp[1]][j] + Cens[tp[2]][j])/3.0)
  return A

def emitNodes(N,label,num):
  print('/',label,'[', sep='')
  pretty(N, num)
  print('] def')
  print('')

def emitTuples(E,label,num):
  print('/',label,'[', sep='')
  #for ee in E: print('[', ee[0], ee[1], ']')
  for ee in E: 
    print('[' + ' '.join([str(j) + ' ' for j in ee]) + ']')
  print('] def')

def showCenters(b, s, d):
  N = cellCenters(b, s, d)
  for n in N:
    print( mypoint(n) )

C = cellCenters(base+1, scale, stretch)

def setCorners(C, b):
  Triples = setTriples(b)
  #print('triples')
  #for ttt in Triples:
  #  print(ttt)
  corners = []
  for t in Triples:
    corners.append(meetpoint(C, t))
  if b==2:
    outerlayer = geoLayer(b, scale*layerRadius(b-.5,stretch))
    Select = [j for j in range(6)]
  elif b==3:
    outerlayer = geoLayer(b+1,scale*layerRadius(b-.5,stretch) )
    #Select = [0,1, 3,4,5, 7,8,9, 11]
    Select = [j for j in range(12)]
  elif b==4:
    outerlayer = geoLayer(b+2,scale*layerRadius(b-.5,stretch) )
    #Select = [0,1, 3,  5,6,7, 9, 11,12,13, 15, 17]
    Select = [j for j in range(18)]
  elif b==5:
    outerlayer = geoLayer(b+3,scale*layerRadius(b-.5,stretch) )
    #Select = [0,1, 3,  5, 7,8,9, 11, 13, 15,16,17, 19, 21, 23]
    Select = [j for j in range(24)]
  for j in range(len(Select)):
    corners.append(outerlayer[Select[j]])
  for j in range(len(Select)):
    corners.append(outerlayer[Select[j]])
  return corners
   
def setNewCenters(b, OldCenters):
  NewC = []
  NbrList = CellCors[b-2]
  for cellNbrs in NbrList:
    NewC.append(centroid(OldCenters, cellNbrs))
  return NewC
      
def printHead(minx, miny, maxx, maxy):
  print('%!PS-Adobe-3.0 EPSF-3.0')
  print('%%Creator: RBH')
  print('%%BoundingBox:', myround(minx-pad), myround(miny-pad), myround(maxx+pad), myround(maxy+pad))
  print('%%Pages: 0\n%%EndComments')
  print('%%Origin: [eg: 0 0]')
  print('%%LanguageLevel: 2 [could be 1 2 or 3]')
  print('%%Pages: 1')
  print('%%Page: 1 1')
  print('%%EOF')
  print('')
  print('/Scale', scale, 'def')

def printBody():
  f = open('geo-body.eps','r')
  for line in f: print(line, end='')

def printData():
  #print('/Centers [')
  #showCenters(base, scale, stretch)
  #print('] def')
  Centers = cellCenters(base, scale, stretch)
  Corners = setCorners(Centers,base)
  emitNodes(Centers,'Centers',len(Centers))
  NewCenters = setNewCenters(base, Corners)
  emitNodes(NewCenters,'NewCenters',len(NewCenters))
  emitNodes(Corners,'Corners',len(Corners))
  DualEdges = setDualEdges(base)
  emitTuples(DualEdges,'DualEdges',len(DualEdges))
  CornerEdges = setCornerEdges(base)
  emitTuples(CornerEdges,'CornerEdges',len(CornerEdges))
  emitTuples(Poly[base-3],'Polygons',len(Poly[base-3]))

def printTail(maxx, L):
  print('gsave', maxx, '2.0 FillGray BoardPerimFill grestore')
  #print('Centers ShowNodes')                 #uncomment for centers
  #print('NewCenters ShowNodes')           
  #print('NewCenters DualEdges ShowEdges')    #uncomment for new-center dual
  #print('Centers DualEdges ShowEdges')       #uncomment for original dual
  #print('Corners ShowNodes')                 #uncomment for corner nodes
  print('false false FontSelect')
  for instr in L:
    print(instr, end='')
  print('Corners CornerEdges ShowEdges')
  print(maxx, '2 0 BoardPerimOnly')

printHead(mmx[0], mmx[1], mmx[2], mmx[3])
printBody()
printData()
printTail(mmx[3], L)

